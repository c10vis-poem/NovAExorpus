"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => MemVaultPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");

// src/sync.ts
function decideAction(memory, existing) {
  if (!existing) return "create";
  const existingTime = Date.parse(existing.updatedAt);
  const remoteTime = Date.parse(memory.updated_at);
  if (Number.isNaN(existingTime) || Number.isNaN(remoteTime) || remoteTime > existingTime) {
    return "update";
  }
  return "skip";
}
function detectOrphans(indexEntries, remoteIds) {
  return indexEntries.filter((e) => !remoteIds.has(e.memvaultId));
}
function buildIdIndex(entries) {
  const map = /* @__PURE__ */ new Map();
  for (const e of entries) {
    map.set(e.memvaultId, e);
  }
  return map;
}
function slugify(text, maxLen = 60) {
  const base = text.toLowerCase().trim().replace(/[^a-z0-9一-龥]+/g, "-").replace(/^-+|-+$/g, "");
  return (base || "memory").slice(0, maxLen);
}
function fileNameFor(memory) {
  const shortId = memory.id.replace(/^mem_/, "").slice(0, 8);
  return `${slugify(memory.content)}--${shortId}.md`;
}
function folderFor(memory) {
  switch (memory.memory_type.toLowerCase()) {
    case "episode":
      return "10-Daily";
    case "entity":
      return "20-Entities";
    case "skill":
      return "40-Skills";
    default:
      return "30-Memories";
  }
}
function yamlList(items) {
  return `[${items.map((t) => JSON.stringify(t)).join(", ")}]`;
}
function buildFrontmatter(memory) {
  const lines = [
    "---",
    `memvault_id: ${memory.id}`,
    `memvault_updated_at: ${memory.updated_at}`,
    `priority: ${memory.priority}`,
    `type: ${memory.memory_type}`,
    `layer: ${memory.layer}`,
    `tags: ${yamlList(memory.tags)}`,
    `namespace: ${memory.namespace}`,
    `human_reviewed: ${memory.human_reviewed}`,
    "---"
  ];
  return lines.join("\n");
}
function buildNoteContent(memory) {
  let body = memory.content;
  if (memory.instruction) {
    body += `

## Instruction
${memory.instruction}`;
  }
  return `${buildFrontmatter(memory)}

${body}
`;
}

// src/main.ts
var VIEW_TYPE = "memvault-panel";
var DEFAULT_SETTINGS = {
  serverUrl: "http://127.0.0.1:8080",
  refreshInterval: 10,
  apiKey: "",
  syncFolder: "MemVault",
  syncDeleteOrphans: false
};
function asMessage(e) {
  return e instanceof Error ? e.message : String(e);
}
var MemVaultPlugin = class extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    this.settings = DEFAULT_SETTINGS;
    this.refreshTimer = null;
  }
  async onload() {
    await this.loadSettings();
    this.registerView(VIEW_TYPE, (leaf) => new MemVaultView(leaf, this));
    this.addRibbonIcon("database", "MemVault", () => this.activateView());
    this.addCommand({
      id: "open-panel",
      name: "Open memory panel",
      callback: () => this.activateView()
    });
    this.addCommand({
      id: "search",
      name: "Search memories",
      callback: () => new MemVaultSearchModal(this.app, this).open()
    });
    this.addCommand({
      id: "search-insert",
      name: "Search and insert memory",
      editorCallback: (editor) => {
        new MemVaultInsertModal(this.app, this, editor).open();
      }
    });
    this.addCommand({
      id: "save-selection",
      name: "Save selection as memory",
      editorCallback: async (editor) => {
        const text = editor.getSelection();
        if (!text) {
          new import_obsidian.Notice("No text selected");
          return;
        }
        await this.saveMemory(text, "REFERENCE", "fact");
      }
    });
    this.addCommand({
      id: "save-selection-must",
      name: "Save selection as MUST rule",
      editorCallback: async (editor) => {
        const text = editor.getSelection();
        if (!text) {
          new import_obsidian.Notice("No text selected");
          return;
        }
        await this.saveMemory(text, "MUST", "preference");
      }
    });
    this.addCommand({
      id: "extract-selection",
      name: "Extract memories from selection",
      editorCallback: async (editor) => {
        const text = editor.getSelection();
        if (!text) {
          new import_obsidian.Notice("No text selected");
          return;
        }
        try {
          const result = await this.api("POST", "/api/extract", {
            text,
            mode: "rule",
            auto_save: true
          });
          const candidates = result.memories?.length ?? 0;
          if (candidates === 0) {
            new import_obsidian.Notice("No extractable memories found in selection");
            return;
          }
          const saved = result.saved_ids?.length ?? 0;
          new import_obsidian.Notice(
            saved > 0 ? `${candidates} candidate(s) extracted \u2014 ${saved} saved to review inbox` : `${candidates} candidate(s) extracted`
          );
        } catch (e) {
          new import_obsidian.Notice(`Extraction failed: ${asMessage(e)}`);
        }
      }
    });
    this.addCommand({
      id: "mark-read",
      name: "Mark memory as read",
      callback: () => {
        new SimplePromptModal(this.app, {
          title: "Mark as read (refresh access recency \u2014 decay weighs it)",
          placeholder: "mem_...",
          submitLabel: "Mark as read",
          onSubmit: async (id) => {
            const trimmed = id.trim();
            if (!trimmed) {
              new import_obsidian.Notice("Memory ID required");
              return;
            }
            try {
              await this.api("POST", "/api/confirm-read", { memory_ids: [trimmed] });
              new import_obsidian.Notice("Marked as read (access_count bumped)");
            } catch (e) {
              new import_obsidian.Notice(`Mark as read failed: ${asMessage(e)}`);
            }
          }
        });
      }
    });
    this.addCommand({
      id: "sync-vault",
      name: "Sync memories to vault",
      callback: async () => {
        try {
          await this.syncVaultFromServer();
        } catch (e) {
          new import_obsidian.Notice(`Sync failed: ${asMessage(e)}`);
        }
      }
    });
    this.addSettingTab(new MemVaultSettingTab(this.app, this));
  }
  onunload() {
    if (this.refreshTimer) {
      window.clearInterval(this.refreshTimer);
    }
  }
  /// Every REST response is wrapped as `{ ok, data, error }` — unwrap `data`
  /// here so every caller below just gets the real payload, and throw on
  /// `ok: false` so callers can rely on try/catch instead of checking `ok`.
  async api(method, path, body) {
    const url = `${this.settings.serverUrl}${path}`;
    const options = { url, method };
    const headers = {};
    if (body !== void 0) {
      options.body = JSON.stringify(body);
      headers["Content-Type"] = "application/json";
    }
    if (this.settings.apiKey) {
      headers["X-MemVault-Api-Key"] = this.settings.apiKey;
    }
    if (Object.keys(headers).length) {
      options.headers = headers;
    }
    const resp = await (0, import_obsidian.requestUrl)(options);
    const parsed = resp.json;
    if (parsed && typeof parsed === "object" && parsed.ok !== void 0) {
      if (!parsed.ok) {
        throw new Error(parsed.error || "MemVault API error");
      }
      return parsed.data;
    }
    return parsed;
  }
  async listMemories(limit = 50) {
    const raw = await this.api("GET", `/api/memories?limit=${limit}`);
    return raw.map(({ type, ...rest }) => ({ ...rest, memory_type: type ?? rest.memory_type ?? "" }));
  }
  async writeVaultFile(path, content) {
    const existing = this.app.vault.getAbstractFileByPath(path);
    if (existing instanceof import_obsidian.TFile) {
      await this.app.vault.modify(existing, content);
    } else {
      await this.app.vault.create(path, content);
    }
  }
  async searchMemories(query, topK = 10) {
    const raw = await this.api("POST", "/api/search", { query, top_k: topK });
    return raw.map(({ memory, score }) => {
      const { type, ...rest } = memory;
      return { memory: { ...rest, memory_type: type ?? rest.memory_type ?? "" }, score };
    });
  }
  async saveMemory(content, priority, type) {
    try {
      const result = await this.api("POST", "/api/memories", {
        content,
        priority,
        type,
        agent_id: "obsidian",
        agent_type: "note-editor",
        namespace: "global"
      });
      new import_obsidian.Notice(`Saved: ${result.id}`);
    } catch (e) {
      new import_obsidian.Notice(`Save error: ${asMessage(e)}`);
    }
  }
  async deleteMemory(id) {
    await this.api("DELETE", `/api/memories/${id}`);
  }
  async ensureFolder(path) {
    const existing = this.app.vault.getAbstractFileByPath(path);
    if (!existing) {
      await this.app.vault.createFolder(path).catch(() => {
      });
    }
  }
  /** One-way DB → vault sync (see docs/INSTALL.md and README for the frontmatter schema). */
  async syncVaultFromServer() {
    const folder = this.settings.syncFolder || "MemVault";
    await this.ensureFolder(folder);
    const memories = await this.listMemories(1e4);
    const existingFiles = this.app.vault.getMarkdownFiles().filter((f) => f.path === folder || f.path.startsWith(`${folder}/`));
    const indexEntries = [];
    for (const file of existingFiles) {
      const fm = this.app.metadataCache.getFileCache(file)?.frontmatter;
      const memvaultId = fm?.memvault_id;
      if (typeof memvaultId === "string" && memvaultId) {
        const updatedAt = fm?.memvault_updated_at;
        indexEntries.push({
          path: file.path,
          memvaultId,
          updatedAt: typeof updatedAt === "string" ? updatedAt : ""
        });
      }
    }
    const index = buildIdIndex(indexEntries);
    let created = 0;
    let updated = 0;
    let skipped = 0;
    for (const mem of memories) {
      const existing = index.get(mem.id);
      const action = decideAction(mem, existing);
      if (action === "skip") {
        skipped++;
        continue;
      }
      const content = buildNoteContent(mem);
      if (action === "create") {
        const sub = folderFor(mem);
        await this.ensureFolder(`${folder}/${sub}`);
        const path = `${folder}/${sub}/${fileNameFor(mem)}`;
        await this.app.vault.create(path, content);
        created++;
      } else if (existing) {
        const file = this.app.vault.getAbstractFileByPath(existing.path);
        if (file instanceof import_obsidian.TFile) {
          await this.app.vault.modify(file, content);
          updated++;
        }
      }
    }
    let archived = 0;
    if (this.settings.syncDeleteOrphans) {
      const remoteIds = new Set(memories.map((m) => m.id));
      const orphans = detectOrphans(indexEntries, remoteIds);
      for (const o of orphans) {
        const file = this.app.vault.getAbstractFileByPath(o.path);
        if (file instanceof import_obsidian.TFile) {
          await this.app.fileManager.trashFile(file);
          archived++;
        }
      }
    }
    new import_obsidian.Notice(
      `MemVault sync: ${created} created, ${updated} updated, ${skipped} unchanged` + (archived ? `, ${archived} removed` : "")
    );
  }
  refreshOpenViews() {
    for (const leaf of this.app.workspace.getLeavesOfType(VIEW_TYPE)) {
      leaf.view.refresh();
    }
  }
  async activateView() {
    const existing = this.app.workspace.getLeavesOfType(VIEW_TYPE);
    if (existing.length) {
      await this.app.workspace.revealLeaf(existing[0]);
      return;
    }
    const leaf = this.app.workspace.getRightLeaf(false);
    if (leaf) {
      await leaf.setViewState({ type: VIEW_TYPE, active: true });
      await this.app.workspace.revealLeaf(leaf);
    }
  }
  async loadSettings() {
    const data = await this.loadData();
    this.settings = { ...DEFAULT_SETTINGS, ...data };
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};
var MemVaultSearchModal = class extends import_obsidian.SuggestModal {
  constructor(app, plugin) {
    super(app);
    this.results = [];
    this.plugin = plugin;
    this.setPlaceholder("Search memories...");
  }
  async getSuggestions(query) {
    if (query.length < 2) return [];
    try {
      this.results = await this.plugin.searchMemories(query);
      return this.results;
    } catch {
      return [];
    }
  }
  renderSuggestion(result, el) {
    const mem = result.memory;
    el.createDiv({
      text: `[${mem.layer}] ${mem.content.slice(0, 80)}`,
      cls: "memvault-suggestion-title"
    });
    el.createEl("small", {
      text: `${mem.priority} \xB7 ${mem.memory_type} \xB7 ${mem.tags.join(", ")} \xB7 score: ${result.score.toFixed(2)}`,
      cls: "memvault-suggestion-meta"
    });
  }
  onChooseSuggestion(result) {
    const mem = result.memory;
    const content = mem.instruction || mem.content;
    navigator.clipboard.writeText(content).then(() => new import_obsidian.Notice("Copied to clipboard")).catch(() => new import_obsidian.Notice("Copy failed \u2014 clipboard unavailable"));
  }
};
var MemVaultInsertModal = class extends import_obsidian.SuggestModal {
  constructor(app, plugin, editor) {
    super(app);
    this.plugin = plugin;
    this.editor = editor;
    this.setPlaceholder("Search and insert memory...");
  }
  async getSuggestions(query) {
    if (query.length < 2) return [];
    try {
      return await this.plugin.searchMemories(query);
    } catch {
      return [];
    }
  }
  renderSuggestion(result, el) {
    const mem = result.memory;
    el.createDiv({
      text: `${mem.content.slice(0, 80)}`,
      cls: "memvault-suggestion-title"
    });
    el.createEl("small", {
      text: `${mem.priority} \xB7 ${mem.memory_type} \xB7 ${mem.layer}`,
      cls: "memvault-suggestion-meta"
    });
  }
  onChooseSuggestion(result) {
    const mem = result.memory;
    const text = mem.instruction || mem.content;
    this.editor.replaceSelection(text);
  }
};
var SimplePromptModal = class extends import_obsidian.Modal {
  constructor(app, opts) {
    super(app);
    this.title = opts.title;
    this.value = opts.initialValue ?? "";
    this.placeholder = opts.placeholder ?? "";
    this.multiline = opts.multiline ?? false;
    this.submitLabel = opts.submitLabel ?? "Submit";
    this.onSubmit = opts.onSubmit;
  }
  onOpen() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.createEl("h2", { text: this.title });
    const setting = new import_obsidian.Setting(contentEl);
    if (this.multiline) {
      setting.addTextArea((t) => t.setPlaceholder(this.placeholder).setValue(this.value).onChange((v) => this.value = v));
    } else {
      setting.addText((t) => t.setPlaceholder(this.placeholder).setValue(this.value).onChange((v) => this.value = v));
    }
    new import_obsidian.Setting(contentEl).addButton(
      (b) => b.setButtonText(this.submitLabel).setCta().onClick(async () => {
        try {
          await this.onSubmit(this.value);
          this.close();
        } catch (e) {
          new import_obsidian.Notice(`Failed: ${asMessage(e)}`);
        }
      })
    );
  }
  onClose() {
    this.contentEl.empty();
  }
};
var MemVaultView = class extends import_obsidian.ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.refreshTimer = null;
    this.plugin = plugin;
  }
  getViewType() {
    return VIEW_TYPE;
  }
  getDisplayText() {
    return "MemVault";
  }
  getIcon() {
    return "database";
  }
  async onOpen() {
    await this.render();
    this.startAutoRefresh();
  }
  onClose() {
    if (this.refreshTimer) {
      window.clearInterval(this.refreshTimer);
      this.refreshTimer = null;
    }
    return Promise.resolve();
  }
  refresh() {
    void this.render();
  }
  startAutoRefresh() {
    const interval = this.plugin.settings.refreshInterval * 1e3;
    if (interval > 0) {
      this.refreshTimer = window.setInterval(() => void this.render(), interval);
    }
  }
  async render() {
    const container = this.containerEl.children[1];
    container.empty();
    const header = container.createDiv({ cls: "memvault-panel-header" });
    header.createSpan({ text: "MemVault", cls: "memvault-panel-title" });
    const syncBtn = header.createEl("button", { text: "Sync", cls: "mod-cta" });
    syncBtn.setAttr("aria-label", "Sync memories to vault");
    syncBtn.onclick = async () => {
      try {
        await this.plugin.syncVaultFromServer();
      } catch (e) {
        new import_obsidian.Notice(`Sync failed: ${asMessage(e)}`);
      }
    };
    await this.renderMemories(container);
  }
  async renderMemories(container) {
    try {
      const memories = await this.plugin.listMemories();
      if (!memories.length) {
        container.createEl("p", { text: "No memories stored.", cls: "mod-muted" });
        return;
      }
      const list = container.createDiv({ cls: "memvault-list" });
      for (const mem of memories) {
        this.renderMemoryItem(list, mem);
      }
      container.createEl("small", {
        text: `${memories.length} memories \xB7 auto-refresh ${this.plugin.settings.refreshInterval}s`,
        cls: "mod-muted"
      });
    } catch (e) {
      container.createEl("p", {
        text: `Connection error: ${asMessage(e)}
Ensure MemVault server is running on ${this.plugin.settings.serverUrl}`,
        cls: "mod-warning"
      });
    }
  }
  renderMemoryItem(container, mem) {
    const item = container.createDiv({ cls: "memvault-item" });
    item.setAttr("data-priority", mem.priority);
    const header = item.createDiv({ cls: "memvault-item-header" });
    const priority = (mem.priority || "BACKGROUND").toUpperCase();
    header.createSpan({
      text: priority,
      cls: `memvault-priority memvault-priority-${priority.toLowerCase()}`
    });
    header.createSpan({ text: mem.layer, cls: "memvault-layer" });
    header.createSpan({ text: mem.memory_type, cls: "memvault-type" });
    item.createDiv({
      text: mem.content.slice(0, 120) + (mem.content.length > 120 ? "..." : ""),
      cls: "memvault-item-content"
    });
    if (mem.instruction && mem.instruction !== mem.content) {
      item.createDiv({
        text: `\u2192 ${mem.instruction.slice(0, 100)}`,
        cls: "memvault-instruction"
      });
    }
    if (mem.skill_meta) {
      const skill = item.createDiv({ cls: "memvault-skill" });
      if (mem.skill_meta.trigger) {
        skill.createSpan({ text: mem.skill_meta.trigger });
      }
      if (mem.skill_meta.steps.length) {
        skill.createSpan({ text: ` \xB7 ${mem.skill_meta.steps.length} steps` });
      }
    }
    if (mem.tags.length) {
      const tags = item.createDiv({ cls: "memvault-tags" });
      for (const tag of mem.tags) {
        tags.createSpan({ text: tag, cls: "memvault-tag" });
      }
    }
    const actions = item.createDiv({ cls: "memvault-actions" });
    const deleteBtn = actions.createEl("button", { text: "Delete", cls: "memvault-delete" });
    deleteBtn.onclick = () => {
      new ConfirmModal(this.app, "Delete this memory? This cannot be undone.", async () => {
        try {
          await this.plugin.deleteMemory(mem.id);
          new import_obsidian.Notice("Deleted");
          void this.render();
        } catch (e) {
          new import_obsidian.Notice(`Delete failed: ${asMessage(e)}`);
        }
      }).open();
    };
  }
};
var ConfirmModal = class extends import_obsidian.Modal {
  constructor(app, message, onConfirm) {
    super(app);
    this.message = message;
    this.onConfirm = onConfirm;
  }
  onOpen() {
    this.contentEl.createDiv({ text: this.message, cls: "mod-warning" });
    new import_obsidian.Setting(this.contentEl).addButton(
      (b) => b.setButtonText("Delete").setWarning().onClick(async () => {
        await this.onConfirm();
        this.close();
      })
    );
  }
  onClose() {
    this.contentEl.empty();
  }
};
var MemVaultSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian.Setting(containerEl).setName("Server URL").setDesc("MemVault MCP server HTTP address (requires --transport http / REST mode)").addText((text) => text.setPlaceholder("http://127.0.0.1:8080").setValue(this.plugin.settings.serverUrl).onChange(async (value) => {
      this.plugin.settings.serverUrl = value;
      await this.plugin.saveSettings();
    }));
    new import_obsidian.Setting(containerEl).setName("Auto-refresh interval").setDesc("How often to refresh the sidebar (seconds, 0 to disable)").addText((text) => text.setPlaceholder("10").setValue(String(this.plugin.settings.refreshInterval)).onChange(async (value) => {
      this.plugin.settings.refreshInterval = parseInt(value) || 10;
      await this.plugin.saveSettings();
    }));
    new import_obsidian.Setting(containerEl).setName("API key").setDesc("Sent as X-MemVault-Api-Key for admin-protected REST routes (leave empty if the server has no admin key configured)").addText((text) => text.setPlaceholder("").setValue(this.plugin.settings.apiKey).onChange(async (value) => {
      this.plugin.settings.apiKey = value;
      await this.plugin.saveSettings();
    }));
    new import_obsidian.Setting(containerEl).setName("Vault sync").setHeading();
    new import_obsidian.Setting(containerEl).setName("Sync folder").setDesc('Vault folder that "Sync Memories to Vault" writes notes into').addText((text) => text.setPlaceholder("MemVault").setValue(this.plugin.settings.syncFolder).onChange(async (value) => {
      this.plugin.settings.syncFolder = value || "MemVault";
      await this.plugin.saveSettings();
    }));
    new import_obsidian.Setting(containerEl).setName("Delete orphaned notes on sync").setDesc("If a synced note's memory no longer exists on the server, delete the local note too. Off by default so manual edits are never silently lost.").addToggle((toggle) => toggle.setValue(this.plugin.settings.syncDeleteOrphans).onChange(async (value) => {
      this.plugin.settings.syncDeleteOrphans = value;
      await this.plugin.saveSettings();
    }));
  }
};
//# sourceMappingURL=main.js.map

/* nosourcemap */