# Cross-Cutting Principles

Principles that apply to all skills. Read as a mandatory checklist during any skill creation or regeneration.

---

## Active Principles

### 1. Declared is not enforced
A behaviour stated in instructions, memory or a context injection decays under task load and loses to competing instructions. Anything that must hold needs a structural trigger tied to an event (a hook, a checkpoint, mechanical injection at session start) and a measurable trip-wire, not text alone.
Source: observation 0001, 0002, 0006, 0010, 0022, 0028

### 2. Enforcement state is not writable by the agent it constrains
A gate the agent can reset or clear itself is advisory. Keep gate state outside the agent's write reach.
Source: observation 0017

### 3. Absence claims need the raw record and named probes
A shallow or summarised probe that finds nothing is evidence about the probe, not about the world. Before saying something does not exist, check the rawest record that would hold it (decision docs, full listings, branches, open items, the source's own access path) and report what was checked. Subagent reports describe their batch, not what exists.
Source: observation 0007, 0008, 0016, 0024

### 4. A defect is fixed only where it happens
Verify a fix on the path where the defect was reported. A clean run on a different path is not evidence.
Source: observation 0035

### 5. Confirmations come from the component that did the work
A "done" or "recorded" message must be produced from the actual result of the step it reports, and must say only what this input changed. Static success text in a layer that did nothing is a false positive the agent will trust. Test any loosened parser against real message shapes.
Source: observation 0031, 0037

### 6. Check delegate capability against the rule at spawn time
A rule that requires a delegate to write, read or report something is void if the delegate is created without that capability. Match the delegate type to the rule before spawning.
Source: observation 0023

### 7. Approval is per item and lasts per task
A general assent covers only what was unambiguous; deletion or other destructive approval must name the item. Conversely, an approved gate should last for the approved task, not reset on routine conversation. Decision requests offer fixed options the reader can answer once.
Source: observation 0019, 0036, 0038

### 8. Deferral needs a named reason and a visible cost
A deferral without a blocking reason is unfinished work moved to the next session. A carry-over path that costs nothing becomes the default, so make carrying an item visible to the operator.
Source: observation 0020, 0030

### 9. A handoff note is a pointer, not authority
Treat notes, backlog items and prior-session claims as leads to confirm, and keep edits to the scope actually verified. A skill must not state a platform limit as fact unless it was tested, and the operator's vendor documentation outranks an untested claim.
Source: observation 0009, 0011

### 10. Inventory what exists before building or proposing
Before building a capability or proposing a rule, enumerate the existing scripts, hooks and enforcement for it, and read what the project says about the platform before the first install. Duplicates break dependents and hide the real gap.
Source: observation 0005, 0013, 0029

### 11. Destructive steps depend on verified state and stated value
Condition cleanup on the success state it assumes (for example MERGED), not on a process ending. Check that exclusion patterns match before a broad operation runs, and state each item's value before offering to delete it. Identity questions (same model, same record) are not answered by byte hashes alone.
Source: observation 0014, 0021, 0032, 0038

### 12. Interrupted procedures leave a progress marker; scratch is for intermediates
Write an on-disk marker for any multi-step procedure so a partial run and a never-started run look different. Move anything a future session needs out of ephemeral working directories into durable storage.
Source: observation 0008, 0015

### 13. Partitioned stores need pinned anchors and cross-partition queries
Where state is split by folder, project or account, a "latest" query must span every partition, and the canonical location must be pinned literally in config rather than re-derived each session.
Source: observation 0003, 0012

### 14. Inspection must not leak secrets
Reading configuration can print secrets into the transcript. Redact by default, treat an accidental print as requiring rotation, fail closed on empty secret values, and write commands for the shell the person actually runs.
Source: observation 0004, 0025

### 15. Use the operator's words
Labels coined during work are private shorthand. Quote the operator's ask, define any term in one plain sentence, and never present their request back as a new proposal under a new name.
Source: observation 0034

### 16. Validate cheaply before spending heavily; verify gates exist
Check inputs before long compute and make long jobs resumable. Auto-merge and similar automation wait only for required checks, so confirm the gate exists before relying on it.
Source: observation 0026, 0027
