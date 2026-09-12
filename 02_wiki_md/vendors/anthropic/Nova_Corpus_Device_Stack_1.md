---
source: Nova Corpus — Device Stack (1).html
type: html
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

window.__FRAME_PREAMBLE={"capabilities":{"artifact":"artifact.BWD0CGLd.js","assets":"assets.BkxVItX2.js","comments":"comments.CqCXYViZ.js","db":"db.5PgiKS-2.js","downloads":"downloads.C3GSvEDP.js","mcp":"mcp.D3B2EyQu.js","permissions":"permissions.BNySkLV5.js","room":"room.BgXZkiYR.js","sample":"sample.B5DdHYz7.js","self":"artifact.BWD0CGLd.js","user":"user.BpKav-Rf.js"},"transforms":"_transforms.BI3gXbbT.js","comments":"_comments.DOfpa5nr.js","translate":"_translate.5HCW4BJh.js"}(function(){"use strict";var ce=["light","dark","system"],ue=/^[A-Za-z0-9_-]{1,64}$/,V=/^[a-zA-Z_:][a-zA-Z0-9_:.-]{0,127}$/,fe=new Set(["class","hidden","value","checked"]);function de(e){const t=e.toLowerCase();return t.startsWith("data-")||t.startsWith("aria-")||fe.has(t)}var pe="http://www.w3.org/1999/xhtml",me="http://www.w3.org/2000/svg",ge=new Set(["script","style","iframe","noscript","noframes","noembed","xmp","plaintext","template","title","textarea","object","embed"]),_e=new Set(["script","style"]);function ve(e){const t=e.localName.toLowerCase();return e.namespaceURI===pe?!ge.has(t):e.namespaceURI===me?!_e.has(t):!1}function he(e){if(e===null||typeof e!="object")return!1;const t=e.__frame_patch;if(t===null||typeof t!="object")return!1;const{seq:n,elements:a}=t;if(typeof n!="number"||!Number.isSafeInteger(n)||!Array.isArray(a)||a.length===0||a.length>64)return!1;for(const i of a){if(i===null||typeof i!="object")return!1;const r=i;if(typeof r.target!="string"||!ue.test(r.target)||r.text!==void 0&&typeof r.text!="string")return!1;if(r.attrsSet!==void 0){if(r.attrsSet===null||typeof r.attrsSet!="object")return!1;for(const[l,c]of Object.entries(r.attrsSet))if(!V.test(l)||typeof c!="string")return!1}if(r.attrsRemoved!==void 0){if(!Array.isArray(r.attrsRemoved))return!1;for(const l of r.attrsRemoved)if(typeof l!="string"||!V.test(l))return!1}}return!0}function ye(e){if(e===null||typeof e!="object")return!1;const t=e.__frame_init;return t!==null&&typeof t=="object"}function be(e){return e!==null&&typeof e=="object"&&e.__frame_size_poke===!0}function Ee(e){if(e===null||typeof e!="object")return!1;const t=e.__frame_theme;if(t===null||typeof t!="object")return!1;const n=t.theme;return typeof n=="string"&&ce.includes(n)}function we(e){try{typeof reportError=="function"?reportError(e):setTimeout(()=>{throw e},0)}catch{}}var X=["#62744c","#b04e72","#5b7596","#a3651f","#7a6ba8","#3f7a75"];function J(e){let t=0;for(let n=0;n<e.length;n++)t=t*31+e.charCodeAt(n)>>>0;return X[t%X.length]??"#788c5d"}var Z="#c7c9d1",Ae=["data:image","/svg+xml,"].join("");function Q(e){return Ae+"%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 2 2'%3E%3Ccircle cx='1' cy='1' r='1' fill='"+encodeURIComponent(e)+"'/%3E%3C/svg%3E"}var Se=Object.freeze({id:null,name:"",avatarUrl:Q(Z),color:Z,email:null,isOwner:!1,canEdit:!1});function je(...e){const t=e[0],n=typeof t=="string"?[t]:Array.isArray(t)?t.filter(i=>typeof i=="string"):[],a=Object.create(null);for(const i of n)a[i]={id:i,name:"",avatarUrl:Q(J(i)),color:J(i),email:null,isMe:!1};return a}var ee=Object.freeze(Object.assign(Object.create(null),{user:Object.freeze(Object.assign(Object.create(null),{id:null,isOwner:!1,canEdit:!1,me:Se,profiles:je,name:"",avatarUrl:null,search:Object.freeze([]),email:null}))})),Re={sample:"sample"};function te(){const e=new Uint8Array(20);try{crypto.getRandomValues(e)}catch{for(let n=0;n<e.length;n++)e[n]=Math.floor(Math.random()*256)}let t="";for(const n of e)t+=(n%36).toString(36);return t}function Oe(e,t){const n=r=>{const l={path:r},c=r.split("/");return{id:c[c.length-1],path:r,get:()=>t("get",[l]),set:d=>t("set",[l,d]),update:d=>t("update",[l,d]),delete:()=>t("delete",[l]),acquire:d=>t("acquire",[l,d]),onSnapshot:(d,E)=>t("subscribe",[l,d,E]),collection:d=>i(r+"/"+String(d))}},a=r=>({where:(l,c,d)=>a({...r,where:[...r.where??[],{f:String(l),op:String(c),v:d}]}),orderBy:(l,c)=>a({...r,orderBy:{f:String(l),dir:c===void 0?"asc":String(c)}}),limit:l=>a({...r,limit:Number(l)}),get:()=>t("query",[r]),onSnapshot:(l,c)=>t("subscribe",[r,l,c])}),i=r=>({...a({collection:r}),path:r,doc:l=>n(r+"/"+(l===void 0?te():String(l))),add:l=>{const c=n(r+"/"+te());return Promise.resolve(c.set(l)).then(()=>c)}});e.doc=r=>n(String(r)),e.collection=r=>i(String(r))}var Pe=Object.freeze([]);function Te(e,t){let n=null,a=null;const i=()=>e.__settled;e.peers=()=>Pe,e.connected=()=>!1,e.emit=()=>i()?.()??Promise.resolve(),e.presence=r=>{const l=i();if(l)return l();let c=null;if(r!==null&&typeof r=="object")try{Array.isArray(r)||(c={...r})}catch{}return c===null?Promise.reject({code:"invalid_argument",message:"presence takes an object"}):(n===null&&(n=Object.create(null),a=Promise.resolve(t("presence",[n]))),Object.assign(n,c),a)}}var B="__frame_scroll",Me=150,Le=310,ke=160,Ce=3e4;function Ne(){let e=0,t=!1,n=!1,a=!1,i=0,r=null;const l=u=>{try{sessionStorage.setItem(B,JSON.stringify({y:u}))}catch{}},c=()=>{if(clearTimeout(e),r===null)return;const u=r;r=null,l(u)},d=()=>{if(t){t=!1;return}n=!0,r=scrollY,clearTimeout(e),e=setTimeout(c,Me)};try{addEventListener("scroll",d,{passive:!0}),addEventListener("pagehide",c)}catch{}const E=()=>{let u;try{u=sessionStorage.getItem(B)}catch{return null}if(u===null)return null;let g;try{g=JSON.parse(u)}catch{g=null}const f=g?.y;if(!(typeof f=="number"&&Number.isFinite(f)&&f>=0)){try{sessionStorage.removeItem(B)}catch{}return null}return f};let T=!1;const h=u=>{try{const g=scrollY;scrollTo({top:u,left:0,behavior:"instant"}),i=u,a=!0,clearTimeout(e),r=null,l(u);const f=scrollY;f!==g&&(t=!0),f!==u&&!T&&(T=!0,addEventListener("load",()=>{try{if(scrollY===f){const p=E();h(p!==null?p:i)}}catch{}},{once:!0}))}catch{}},R=()=>{try{return!!location.hash}catch{return!0}};let A=!1;const O=()=>{try{if(A||innerWidth>Le||innerHeight>ke)return;A=!0;const u=Date.now(),g=()=>{try{removeEventListener("resize",g)}catch{}if(Date.now()-u>Ce||n||R())return;const f=E();h(f!==null?f:i)};addEventListener("resize",g)}catch{}};let M=!1,o=!1;return{restore(){if(M||(M=!0,R()))return;const u=E();u!==null&&(h(u),O())},promoted(){if(o||(o=!0,R()))return;const u=E();u!==null?(h(u),O()):a&&h(i)}}}var Ye="modulepreload",We=function(e){return"/"+e},Ke={},Ue=function(t,n,a){let i=Promise.resolve();function r(l){const c=new Event("vite:preloadError",{cancelable:!0});if(c.payload=l,window.dispatchEvent(c),!c.defaultPrevented)throw l}return i.then(l=>{for(const c of l||[])c.status==="rejected"&&r(c.reason);return t().catch(r)})};(function(){const e=Object.defineProperty,t=globalThis,n=["RTCPeerConnection","webkitRTCPeerConnection","RTCDataChannel","RTCIceCandidate","RTCSessionDescription","RTCRtpSender","RTCRtpReceiver"];let a=0;for(let i=0;i<n.length;i++){const r=n[i];try{e(t,r,{value:void 0,writable:!1,configurable:!1})}catch{try{delete t[r]}catch{}try{e(t,r,{value:void 0,writable:!1,configurable:!0})}catch{}}typeof t[r]=="function"&&a++}if(a&&window!==top)try{parent.postMessage({__frame_rtc_lockdown_failed:a},"*")}catch{}})();var qe=1e4,Ie=Object.freeze([...window.__FRAME_PREAMBLE?.origins??["https://claude.ai","https://preview.claude.ai"]]);function re(e){for(const t of Ie)if(t.endsWith(":*"))try{const n=new URL(e);if(`${n.protocol}//${n.hostname}:*`===t)return!0}catch{}else if(e===t)return!0;return!1}var k=Object.freeze({...window.__FRAME_PREAMBLE?.capabilities}),x=window.__FRAME_PREAMBLE?.transforms,$=window.__FRAME_PREAMBLE?.comments,z=window.__FRAME_PREAMBLE?.translate,q=/^[\w.-]+\.js$/,De=/^[a-z][a-z0-9_-]{0,63}$/;function I(e){return Ue(()=>import("/_runtime/"+e),void 0)}function Be(e,t){return{contract:e.contract,changes:new Set(e.changes??[]),flags:new Set(e.flags??[]),capabilities:e.capabilities??{},capBudgets:e.capBudgets??{},transforms:new Map,shellOrigin:t,mount:Y,pipe:()=>({wrap:(n,a)=>(...i)=>{try{return a(...i)}catch(r){return Promise.reject(r)}}})}}var ne=null,C=null;function F(e,t,n){try{Object.defineProperty(e,t,{value:n,writable:!1,configurable:!1,enumerable:!0})}catch{try{Object.defineProperty(e,t,{value:n,writable:!1,configurable:!0,enumerable:!0})}catch{}}}var H=!1;function xe(e,t){const n=[];for(const a of e.elements){const i=document.querySelector(`[data-id="${a.target}"]`);if(!i){parent.postMessage({__frame_patch_miss:{seq:e.seq}},t);return}if([...Object.keys(a.attrsSet??{}),...a.attrsRemoved??[]].some(r=>!de(r))){parent.postMessage({__frame_patch_miss:{seq:e.seq}},t);return}if(a.text!==void 0&&!ve(i)){parent.postMessage({__frame_patch_miss:{seq:e.seq}},t);return}for(const[r,l]of Object.entries(a.attrsSet??{}))if(!oe(i,r)){try{i.setAttribute(r,l)}catch{}se(i,r,l)}for(const r of a.attrsRemoved??[])oe(i,r)||(i.removeAttribute(r),se(i,r,null));typeof a.text=="string"&&(i.textContent=a.text),n.push(a.target)}try{document.dispatchEvent(new CustomEvent("claude:edit",{detail:{seq:e.seq,targets:n}}))}catch{}}function se(e,t,n){if(!(e instanceof HTMLInputElement))return;const a=t.toLowerCase();a==="checked"?e.checked=n!==null:a==="value"&&e.type!=="file"&&(e.value=n??"")}function oe(e,t){const n=t.toLowerCase(),a=e;return n==="data-id"||(n==="value"||n==="checked")&&(a.__artifactSecret===!0||/^(password|hidden|file)$/.test(a.type??"")||/(^|\s)(cc-|one-time-code|current-password|new-password)/i.test(`${e.getAttribute("autocomplete")??""} ${a.autocomplete??""}`))}function ae(e){const t=document.documentElement;e==="light"||e==="dark"?(t.dataset.theme=e,t.style.colorScheme=e,H=!0):H&&(delete t.dataset.theme,t.style.colorScheme="",H=!1)}var ie=256,N=Object.assign(Object.create(null),{mcp:Object.assign(Object.create(null),{watchTool:{handlerArg:3}}),db:Object.assign(Object.create(null),{subscribe:{handlerArg:1,errArg:2}}),room:Object.assign(Object.create(null),{on:{handlerArg:1,errArg:2},onPeers:{handlerArg:0,errArg:1},onConnection:{handlerArg:0,errArg:1}})}),$e=Object.assign(Object.create(null),{db:(e,t)=>Oe(e,t),room:(e,t,n)=>Te(e,n)}),j=new Map;function Y(e,t){const n=j.get(e);if(!n)return;const a=Object.assign(Object.create(null),t);Object.assign(n.impl,a),n.r(n.ns),n.impl.__settled=()=>Promise.reject({code:"capability_removed",message:`${e}: method not in this runtime`});const i=n.queue;n.queue=[];for(const r of i){const l=a[r.method];if(l)if(N[e]?.[r.method])try{r.resolve(l(...r.args))}catch{U(r,N[e][r.method],{code:"transform_error",message:`${e}.${r.method} rejected its arguments`})}else l(...r.args).then(r.resolve,r.reject);else{const c={code:"capability_removed",message:`${e}.${r.method} is not in this runtime`},d=N[e]?.[r.method];if(d){U(r,d,c);continue}r.reject(c)}}}function ze(e,t){const n=j.get(e);if(!n)return;n.impl.__settled=()=>Promise.reject(t),n.r(null);const a=n.queue;n.queue=[];for(const i of a){const r=N[e]?.[i.method];if(r){U(i,r,t);continue}i.reject(t)}}function le(e,t){if(typeof e=="function")try{return e(...t)}catch{return Object.create(null)}return Array.isArray(e)?[...e]:e!==null&&typeof e=="object"?{...e}:e}function D(e,t){const n=ee[e];if(!n){ze(e,t);return}j.get(e)?.r(null),Y(e,Object.fromEntries(Object.entries(n).map(([a,i])=>[a,(...r)=>Promise.resolve(le(i,r))])))}function U(e,t,n){if(e.syncState?.dead)return;const a=t.errArg===void 0?void 0:e.args[t.errArg],i=t.errArg===void 0?e.args[t.handlerArg]:a;typeof i=="function"&&queueMicrotask(()=>{if(!e.syncState?.dead)try{i(t.errArg===void 0?{type:"error",error:n}:n)}catch(r){we(r)}})}var W=Object.getOwnPropertyDescriptor(window,"claude");if(window!==top&&!(W&&W.writable===!1)){const e=x&&q.test(x)?I(x).catch(()=>{}):Promise.resolve(void 0),t=o=>{if(o.type==="auxclick"&&o.button!==1)return;const u=o.target,g=u&&u.closest?u.closest("a[href],area[href]"):null;if(!g)return;const f=g.getAttribute("href");if(!f)return;let p,P;try{p=new URL(f,document.baseURI),P=new URL(document.baseURI).origin}catch{return}if((p.protocol==="http:"||p.protocol==="https:")&&p.origin!==P){o.preventDefault();const w=(g.getAttribute("target")??"").toLowerCase(),y=o.type==="auxclick"||o.metaKey||o.ctrlKey||o.shiftKey||o.altKey||!["","_self","_top","_parent"].includes(w);parent.postMessage({__frame_nav:!0,url:p.href,newTab:y},"*")}};addEventListener("click",t,!0),addEventListener("auxclick",t,!0);const n={},a=o=>{o.isTrusted&&(n.pointer=!0)},i=o=>{o.isTrusted&&(n.click=!0)};addEventListener("pointermove",a,{capture:!0,passive:!0}),addEventListener("click",i,{capture:!0,passive:!0}),e.then(o=>{o?.wireNav&&(o.wireNav(),removeEventListener("click",t,!0),removeEventListener("auxclick",t,!0),removeEventListener("pointermove",a,!0),removeEventListener("click",i,!0),o.wireEngagement?.(n))});let r=null;try{r=Ne()}catch{}const l=W?.value??{};F(window,"claude",l);const c=o=>{let u;const g=new Promise(v=>{u=v}),f={impl:Object.create(null),queue:[],u:g,r:u,ns:null};j.set(o,f);const p=f.impl,P=v=>({code:"queue_overflow",message:`${o}.${v}: pre-init call queue is full`}),w=(v,s)=>{if(f.queue.length>=ie){const m=ee[o];return m&&v in m?Promise.resolve(le(m[v],s)):Promise.reject(P(v))}return new Promise((m,_)=>{f.queue.push({method:v,args:s,resolve:m,reject:_})})},y=Re[o],L=new Proxy(y===void 0?p:(()=>{}),{apply:(v,s,m)=>{const _=y,b=p[_]??p.__settled;return b?b(...m):w(_,m)},get:(v,s)=>{if(typeof s!="string"||s==="then"||s==="toJSON"||s==="valueOf")return;if(s==="toString")return Object.prototype.toString;if(y!==void 0&&(s==="call"||s==="apply"||s==="bind"))return Function.prototype[s];const m=N[o]?.[s];return m?(..._)=>{if(typeof _[m.handlerArg]!="function")throw new TypeError(`${o}.${s} requires a handler function`);const b=p[s];if(b)return b(..._);if(p.__settled){const S={dead:!1},Fe={args:[..._],syncState:S};return p.__settled().catch(He=>U(Fe,m,He)),()=>{S.dead=!0}}if(f.queue.length>=ie){const S={dead:!1};return U({args:[..._],syncState:S},m,P(s)),()=>{S.dead=!0}}let K=null;const G={dead:!1};return f.queue.push({method:s,args:_,resolve:S=>{K=typeof S=="function"?S:null,G.dead&&K?.()},reject:()=>{},syncState:G}),()=>{G.dead=!0,K?.()}}:(..._)=>{const b=p[s]??p.__settled;return b?b(..._):w(s,_)}},set:()=>!1});$e[o]?.(p,(v,s)=>L[v](...s),w),f.ns=L,F(l,o,L)};for(const o of Object.keys(k)){if(l[o]!==void 0){F(l,o,l[o]);continue}c(o)}if(l.use===void 0){const o=u=>{if(typeof u!="string"||!Object.hasOwn(k,u))return Promise.resolve(null);const g=j.get(u);return g?g.u:Promise.resolve(l[u]??null)};try{Object.defineProperty(l,"use",{value:o,writable:!0,configurable:!0,enumerable:!1})}catch{}}let d=null,E=null,T=0;const h=o=>{o.source!==parent||!re(o.origin)||ye(o.data)&&(d=o.data.__frame_init,C=o.origin,removeEventListener("message",h),clearTimeout(T),E?.())};addEventListener("message",h),parent.postMessage({__frame_connect:!0},"*");const R=new Promise(o=>{E=o,T=setTimeout(()=>{removeEventListener("message",h),o()},qe)}),A=document.readyState==="loading"?new Promise(o=>document.addEventListener("DOMContentLoaded",()=>o(),{once:!0})):Promise.resolve();A.then(()=>{try{r?.restore()}catch{}});const O={cb:null},M=o=>{if(!(o.source!==parent||!re(o.origin))&&be(o.data)){try{r?.promoted()}catch{}O.cb?.()}};addEventListener("message",M),R.then(async()=>{if(!d||!C){for(const s of j.keys())D(s,{code:"not_granted",message:"frame initialization did not arrive - capability unavailable"});return}ae(d.theme);const o=C;let u=!1,g=!1;addEventListener("message",s=>{if(s.source!==parent||s.origin!==o)return;Ee(s.data)&&ae(s.data.__frame_theme.theme),he(s.data)&&xe(s.data.__frame_patch,o);const m=s.data?.__fc_mode;m&&typeof m=="object"&&!u&&$&&q.test($)&&(u=!0,I($).then(b=>b.install?.(o,m.on===!0)).catch(()=>{}));const _=s.data?.__ft_cmd;_&&typeof _=="object"&&!g&&z&&q.test(z)&&(g=!0,I(z).then(b=>b.install?.(o,_)).catch(()=>{}))});const f=Object.keys(d.capabilities??{});for(const s of f)Object.hasOwn(k,s)||De.test(s)&&l[s]===void 0&&(c(s),D(s,{code:"capability_disabled",message:"capability not in this runtime generation"}));const p=f.filter(s=>Object.hasOwn(k,s)).map(s=>[s,k[s]]).filter(s=>typeof s[1]=="string"&&q.test(s[1])),P=await Promise.allSettled(p.map(([,s])=>I(s))),w=await e,y=C;w?.buildBoot||parent.postMessage({__frame_cap_telemetry:{kind:"cap-load-error",cap:"_transforms"}},y),ne=w?.buildBoot?w.buildBoot(d,w.TRANSFORMS??{},{shellOrigin:y,mount:Y},s=>parent.postMessage({__frame_cap_telemetry:s},y)):Be(d,y);const L=s=>parent.postMessage({__frame_cap_telemetry:{kind:"cap-load-error",cap:s}},y),v=ne;P.forEach((s,m)=>{const _=p[m][0];if(s.status!=="fulfilled"){L(_);return}try{s.value?.install?.(v)}catch{L(_)}});for(const[s,m]of j)if(m.impl.__settled===void 0){if(f.includes(s)){D(s,{code:"capability_disabled",message:"capability not available in this session"});continue}D(s,{code:"not_granted",message:"capability not available in this session"})}await A,parent.postMessage({__frame_ready:!0},C),e.then(s=>s?.installSizeReporter?.(y,O))})}})();:root{color-scheme:light}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}img{max-width:100%}
Nova Corpus — Device Stack

:root {
  --bg:     #0B0E14;
  --surf:   #111620;
  --panel:  #141C28;
  --border: #1E2D44;
  --hi:     #253650;
  --text:   #C8DCF0;
  --mid:    #6E90B4;
  --dim:    #334E6E;
  --teal:   #0FCCA0;
  --amber:  #F0A020;
  --violet: #8B78F4;
  --red:    #F04858;
  --green:  #1ACC70;
  --mono: ui-monospace,'Cascadia Code','JetBrains Mono','Fira Code',Consolas,monospace;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg:#F0F4FA;--surf:#FAFCFF;--panel:#EEF4FB;--border:#C0D4EC;
    --hi:#D8EAF8;--text:#0A1828;--mid:#3A6090;--dim:#8AAED4;
    --teal:#0A7A60;--amber:#A06008;--violet:#4A38C0;
    --red:#C02030;--green:#0A7A40;
  }
}
:root[data-theme="dark"] {
  --bg:#0B0E14;--surf:#111620;--panel:#141C28;--border:#1E2D44;
  --hi:#253650;--text:#C8DCF0;--mid:#6E90B4;--dim:#334E6E;
  --teal:#0FCCA0;--amber:#F0A020;--violet:#8B78F4;--red:#F04858;--green:#1ACC70;
}
:root[data-theme="light"] {
  --bg:#F0F4FA;--surf:#FAFCFF;--panel:#EEF4FB;--border:#C0D4EC;
  --hi:#D8EAF8;--text:#0A1828;--mid:#3A6090;--dim:#8AAED4;
  --teal:#0A7A60;--amber:#A06008;--violet:#4A38C0;--red:#C02030;--green:#0A7A40;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{font-size:13px;}
body{
  background:var(--bg);
  color:var(--text);
  font-family:var(--mono);
  line-height:1.5;
  padding:20px;
  max-width:1000px;
  margin:0 auto;
}

/* ── System header bar ─────────────────────────────────────────── */
.sys-header {
  border:1px solid var(--teal);
  padding:10px 16px;
  margin-bottom:16px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  flex-wrap:wrap;
  gap:8px;
  background:color-mix(in srgb, var(--teal) 6%, var(--panel));
}
.sys-title { font-size:12px; letter-spacing:.14em; color:var(--teal); }
.sys-meta  { font-size:11px; color:var(--mid); display:flex; gap:16px; flex-wrap:wrap; }
.dot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; }
.dot.green  { background:var(--green); box-shadow:0 0 6px var(--green); }
.dot.amber  { background:var(--amber); }
.dot.red    { background:var(--red); }
.dot.dim    { background:var(--dim); }

/* ── Panel ─────────────────────────────────────────────────────── */
.panel {
  border:1px solid var(--border);
  margin-bottom:12px;
  background:var(--panel);
}
.panel-head {
  padding:6px 14px;
  border-bottom:1px solid var(--border);
  font-size:10px;
  letter-spacing:.16em;
  color:var(--mid);
  display:flex;
  align-items:center;
  justify-content:space-between;
  background:var(--surf);
}
.panel-head .ph-left { display:flex; align-items:center; gap:8px; }
.panel-head .tag {
  font-size:9px;
  padding:1px 6px;
  border:1px solid var(--border);
  color:var(--dim);
  letter-spacing:.08em;
}
.panel-body { padding:12px 14px; }

/* ── Node card ──────────────────────────────────────────────────── */
.node-grid {
  display:grid;
  grid-template-columns:1fr 1fr 1fr;
  gap:12px;
  margin-bottom:12px;
}
@media(max-width:700px){ .node-grid{ grid-template-columns:1fr; } }
@media(min-width:701px) and (max-width:900px){ .node-grid{ grid-template-columns:1fr 1fr; } }

.node-card {
  border:1px solid var(--border);
  background:var(--surf);
}
.node-card.alpha { border-top:2px solid var(--teal); }
.node-card.beta  { border-top:2px solid var(--amber); }
.node-card.gamma { border-top:2px solid var(--violet); }
.node-head {
  padding:8px 12px;
  border-bottom:1px solid var(--border);
  display:flex;
  justify-content:space-between;
  align-items:baseline;
}
.node-id   { font-size:10px; letter-spacing:.18em; font-weight:700; }
.alpha .node-id { color:var(--teal); }
.beta  .node-id { color:var(--amber); }
.gamma .node-id { color:var(--violet); }
.node-name { font-size:11px; color:var(--text); font-weight:700; }
.node-body { padding:10px 12px; }
.node-spec { font-size:11px; color:var(--mid); padding:3px 0; border-bottom:1px solid var(--border); display:flex; gap:6px; }
.node-spec:last-child { border-bottom:none; }
.nsk { color:var(--dim); font-size:10px; min-width:62px; flex-shrink:0; }
.nsv { color:var(--text); }
.node-roles { padding:8px 12px; border-top:1px solid var(--border); }
.role-line { font-size:11px; color:var(--mid); padding:2px 0; }
.role-line::before { content:'· '; color:var(--dim); }

/* ── ASCII / topology ───────────────────────────────────────────── */
.ascii {
  font-size:11px;
  line-height:1.65;
  color:var(--mid);
  overflow-x:auto;
  white-space:pre;
  padding:12px 14px;
  background:var(--surf);
  border:1px solid var(--border);
  margin-bottom:12px;
}
.ascii .ak { color:var(--teal); }
.ascii .aa { color:var(--amber); }
.ascii .av { color:var(--violet); }
.ascii .at { color:var(--text); font-weight:700; }
.ascii .ag { color:var(--green); }
.ascii .ad { color:var(--dim); }
.ascii .ar { color:var(--red); }

/* ── Log line ──────────────────────────────────────────────────── */
.log { font-size:11px; line-height:1.7; color:var(--mid); }
.log .lp { color:var(--dim); }
.log .lteal { color:var(--teal); }
.log .lamber { color:var(--amber); }
.log .lviolet { color:var(--violet); }
.log .lred { color:var(--red); }
.log .lgreen { color:var(--green); }
.log .ltext { color:var(--text); }

/* ── Status badge ──────────────────────────────────────────────── */
.st {
  display:inline-block;
  font-size:9px;
  padding:1px 6px;
  border-radius:2px;
  letter-spacing:.08em;
  font-weight:700;
  vertical-align:middle;
}
.st.built   { background:color-mix(in srgb,var(--green) 15%,transparent); color:var(--green); border:1px solid color-mix(in srgb,var(--green) 40%,transparent); }
.st.partial { background:color-mix(in srgb,var(--amber) 15%,transparent); color:var(--amber); border:1px solid color-mix(in srgb,var(--amber) 40%,transparent); }
.st.design  { background:color-mix(in srgb,var(--violet) 15%,transparent); color:var(--violet); border:1px solid color-mix(in srgb,var(--violet) 40%,transparent); }
.st.absent  { background:color-mix(in srgb,var(--red) 15%,transparent); color:var(--red); border:1px solid color-mix(in srgb,var(--red) 40%,transparent); }
.st.canon   { background:color-mix(in srgb,var(--teal) 15%,transparent); color:var(--teal); border:1px solid color-mix(in srgb,var(--teal) 40%,transparent); }
.st.private { background:color-mix(in srgb,var(--dim) 25%,transparent); color:var(--dim); border:1px solid color-mix(in srgb,var(--dim) 60%,transparent); }

/* ── Row ───────────────────────────────────────────────────────── */
.row {
  display:flex;
  gap:10px;
  padding:4px 0;
  border-bottom:1px solid var(--border);
  font-size:11px;
  align-items:baseline;
  flex-wrap:wrap;
}
.row:last-child { border-bottom:none; }
.rk { color:var(--mid); min-width:160px; flex-shrink:0; font-size:10px; letter-spacing:.04em; }
.rv { color:var(--text); }
.rv code {
  background:var(--hi);
  padding:1px 5px;
  border-radius:2px;
  font-size:10px;
  color:var(--teal);
}

/* ── Operator quote ────────────────────────────────────────────── */
.opq {
  border-left:2px solid var(--amber);
  padding:8px 12px;
  margin:10px 0;
  background:color-mix(in srgb,var(--amber) 5%,transparent);
  font-size:11px;
  color:var(--text);
  line-height:1.6;
}
.opq .ql { font-size:9px; color:var(--amber); letter-spacing:.12em; margin-bottom:4px; }

/* ── Grid 2 ─────────────────────────────────────────────────────── */
.grid-2 { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px; }
@media(max-width:640px){ .grid-2{ grid-template-columns:1fr; } }

/* ── Roadmap ────────────────────────────────────────────────────── */
.roadmap-item {
  display:flex;
  gap:12px;
  padding:8px 0;
  border-bottom:1px solid var(--border);
  font-size:11px;
  align-items:flex-start;
}
.roadmap-item:last-child { border-bottom:none; }
.rm-phase {
  min-width:24px;
  font-size:16px;
  font-weight:900;
  color:var(--dim);
  flex-shrink:0;
  line-height:1.4;
}
.rm-phase.current { color:var(--green); }
.rm-body { flex:1; }
.rm-label { color:var(--text); font-weight:700; margin-bottom:2px; }
.rm-desc { color:var(--mid); line-height:1.5; }

p { font-size:11px; color:var(--mid); line-height:1.6; margin-bottom:6px; }
.divider { height:1px; background:linear-gradient(90deg,var(--hi) 0%,transparent 100%); margin:16px 0; }
.chip {
  display:inline-block;
  background:var(--hi);
  border:1px solid var(--border);
  padding:1px 7px;
  font-size:10px;
  color:var(--mid);
  border-radius:2px;
  margin:1px;
}
.chip.teal  { color:var(--teal); border-color:color-mix(in srgb,var(--teal) 40%,transparent); }
.chip.amber { color:var(--amber); border-color:color-mix(in srgb,var(--amber) 40%,transparent); }
.chip.violet{ color:var(--violet); border-color:color-mix(in srgb,var(--violet) 40%,transparent); }
.chip.dim   { color:var(--dim); }



    NOVA CORPUS · DEVICE STACK

      modu14r_inc. · hardware mesh + network topology



    NODE_ALPHA · ONLINE
    NODE_BETA · CONFIGURING
    NODE_GAMMA · CONFIGURING
    2026-08-06






      P2P MESH TOPOLOGY

    TAILSCALE OVERLAY · ALL NODES


┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                               TAILSCALE OVERLAY — P2P MESH                              │
│          all nodes on the same network · NAT traversal · encrypted point-to-point          │
└──────────────────────────────────────────────────────────────────────────────────────────┘

        ┌───────────────────────────────────┐
        │  NODE_ALPHA · Razr Ultra          │
        │  SM8750 · 16 GB · ~45 TOPS        │
        │  Hexagon HTP v79                  │
        │  ● Horizons UI (lifecycle core)    │
        │  ● novus-agenti · NovA-Claw       │
        │  ● CCR on-device sessions         │
        └──────────────┬────────────────────┘
                       │
                       │  Tailscale · WiFi
                       │
        ┌──────────────┴────────────────────┐
        │  NODE_BETA · Jetson Orin Nano Super │
        │  8 GB · 512 GB DDR4 SSD · ~67 TOPS │
        │  MAIN COMPUTE HUB · headless        │
        │  ● peer-agent (Hydra rotation)     │
        │  ● utilities-agent (housekeeping)  │
        │  ● inference server                │
        └──────────────┬────────────────────┘
                       │
                       │  HIGH-SPEED DATA CABLE (wired · direct)
                       │
        ┌──────────────┴────────────────────┐
        │  NODE_GAMMA · Rubik Pi 3 / DragonWing │
        │  8 GB · ~128 GB SSD · ~14 TOPS     │
        │  VISUAL OS · dual monitor · keyboard │
        │  ● desk display (VNC server)       │
        │  ● DragonWing SoC on-board        │
        └──────────────┬────────────────────┘
                       │
                       │  Tailscale · WiFi (to ALPHA / mesh)
                       │
        ┌──────────────┴────────────────────┐
        │  THIN CLIENT (no compute node)    │
        │  Galaxy Tab S9 FE+ · Wi-Fi only   │
        │  · SSH → NODE_BETA (headless)      │
        │  · AVNC → NODE_BETA (desktop VNC)  │
        │  · Termux · SD card (Jetson flash) │
        └───────────────────────────────────┘





      NODE_ALPHA
      ACTIVE


      Motorola Razr Ultra 2025
      CHIPSM8750 · Snapdragon 8 Elite
      RAM16 GB
      STORAGE~512 GB
      AI TOPS~45 TOPS
      NPUHexagon HTP v79
      FORMPhone · primary user node


      SERVICES RUNNING
      Horizons UI — lifecycle core; nothing lives without it
      novus-agenti — phone agent, runtime manifests
      NovA-Claw — execution surface (nova-skills)
      CCR — claude.ai UI · on-device execution
      ONNX/ORT + Sherpa-ONNX voice layer (in-process)
      QAIRT/HTP inference (when models offloaded + bare metal)






      NODE_BETA
      CONFIGURING


      Jetson Orin Nano Super
      CHIPJetson Orin Nano Super
      RAM8 GB
      STORAGE512 GB DDR4 SSD (added)
      AI TOPS~67 TOPS
      FORMHeadless · main compute hub
      CONNECTTailscale WiFi ← ALPHA; wired → GAMMA


      SERVICES RUNNING
      peer-agent — twins with novus-agenti; Hydra cloud rotation
      utilities-agent — housekeeping, load/unload operator agents
      inference server — swappable backend (never hardcoded)
      AVNC server — portable desktop from Galaxy Tab
      GCP pipeline endpoint (files-inference-node secretary)






      NODE_GAMMA
      CONFIGURING


      Rubik Pi 3 · DragonWing SoC
      CHIPDragonWing SoC (on-board)
      RAM8 GB
      STORAGE~128 GB built-in SSD
      AI TOPS~14 TOPS
      FORMDesk unit · dual monitor · keyboard
      CONNECTwired ← BETA; Tailscale WiFi


      SERVICES RUNNING
      Visual OS — primary desk display output
      Dual monitor hookup
      Keyboard input layer
      Jetson direct pipe — high-speed data cable







      NETWORK LAYER

    CONFIG IN aesop-xi-protocol/infrastructure/



      JETSON ↔ DRAGONWING
      High-speed data cable · direct wired · no network hop


      RAZR ↔ HOME NODE
      Tailscale over WiFi · encrypted P2P tunnel


      MESH OVERLAY
      Tailscale — all three compute nodes on same virtual network; NAT traversal


      ALL NODES
      P2P servers · each node is a server · no hub-and-spoke


      LOOPBACK SHARED
      `127.0.0.1:8080` bound by app daemon · Termux shares loopback · NPU access no inversion needed


      INBOUND LISTENER
      App needs listener for mic/voice/WebView-OAuth from Termux — not yet built ABSENT


      CONFIG LOCATION
      Network config lives in `aesop-xi-protocol/` — infrastructure/pathways layer







      VOICE / NPU PATHWAY

    OPERATOR CANON · AUG 2 2026



      OPERATOR — NEURO MESH SESSION · AUG 2 2026
      "my APK already ships on device with an stt / TTS layer that's running a ONNX/ORT through a llama server. this also allows the model inside of my Termux to utilize the QAIRT model path that allows a GGUF model to run through llama to ggml to kotlin kernel and librc runtimes to land directly on the NPU through the HTP SDK net pathway — I said that pathway will only be utilized when my on device models or my on-device agent through the Horizons UI is offloaded and the APK is running bare metal"



STT / TTS (in-process · always)
ONNX/ORT ── llama server ── Sherpa-ONNX
   Moonshine STT (in-process on AAR) · Kokoro TTS (in-process)

NPU CHAIN (only when Horizons UI offloaded + bare metal)
GGUF → llama → ggml → Kotlin kernel → librc runtimes → Hexagon HTP SDK → NPU
   QAIRT model path · HTP pathway · Snapdragon 8 Elite · ~45 TOPS

DESIGN CONSTRAINT
never hardcode inference backend — keep swappable across all phases



      [ STT ] BROKEN MID-CHAIN — points at `127.0.0.1:8091`, nothing binds it. Fix: Moonshine in-process on AAR already shipping UNVERIFIED ON DEVICE
      [ TTS ] works in-process — Sherpa AAR · Kokoro
      [ LLM ] falls to llmRuntime.streamAudio — looks like model problem, is STT problem







      CCR ON-DEVICE EXECUTION

    TERMUX → CLAUDE.AI



NODE_ALPHA (Razr Ultra)
Termux ── start `claude` ────────────────────────────────────────────── session spawns
  │
  claude.ai = user interface (phone browser / app)
  execution environment = on-device container (not cloud)
  │
  repo access · Drive MCP · GitHub MCP · all tool calls run on device



When `claude` runs in Termux, the session is an on-device container. The user's phone is both the UI and the execution host. Drive MCP, file reads/writes, git pushes — all run on NODE_ALPHA. The claude.ai web interface is just the chat layer.






      THIN CLIENT — NO COMPUTE NODE

    SETUP DOCS IN home-node/jetson-orin/ · termux-environment/



      DEVICE
      Samsung Galaxy Tab S9 FE+ · Wi-Fi only · no SIM


      ROLE
      SSH into NODE_BETA · AVNC into NODE_BETA for portable desktop from couch


      CONNECT
      NODE_BETA only — Rubik Pi 3 handles desk, Tab handles couch/portable via VNC


      TOOLS
      Termux (installed) · SD card used to flash Jetson Nano


      CONFIG DOCS
      `home-node/jetson-orin/` (VNC server config) · `termux-environment/` (AVNC client setup)






      MESH TOTALS


      TOTAL AI TOPS~126 TOPS combined
      TOTAL RAM32 GB across 3 nodes
      TOTAL STORAGE~1.1 TB (SSD + NVMe + flash)
      COMPUTE NODES3 active · all P2P servers
      THIN CLIENTS1 · Galaxy Tab S9 FE+





      REPOS ON THIS STACK


      horizons-ui`c10vis-poem/Horizons-UI`
      novus-agenti`c10vis-poem/novus-agenti`
      aesop protocol`c10vis-poem/aesop`
      nova-skills`c10vis-poem/nova-skills`
      home-node/Jetson + DragonWing · configs
      termux-env/Termux scripts · CLI
      node-gamma-rubik-pidevice node (name confirmed)







      BUILD ROADMAP (IN ORDER)

    DESIGN CONSTRAINT: NEVER HARDCODE INFERENCE BACKEND




      1

        Home node running on all cylinders CURRENT PHASE
        NODE_BETA + NODE_GAMMA configured · Tailscale mesh stable · voice layer closed (Moonshine in-process) · Termux backend listener built · runtime params first-class




      2

        AEC application — communications + safety layer DESIGNED
        Communications workflow · software bridging · safety layer protocol. Target: prototype in 6–8 months




      3

        ARM64 + commercial GPU DESIGNED
        Modular TBD form factor — PCIe attach or external enclosure. GOAL: home node replaces the laptop. Operator's own custom design.




      4

        Broader modular hardware ecosystem PRIVATE
        Metamaterials designs · novel thermal management systems. At least 2 potentially patentable designs. ⚠ NOT documented in any public or shared repo until filed.









      BUILD LEDGER · DEVICE STACK

    RULE 6 · DESIGNED ≠ BUILT


    [ALPHA] built-verified    Razr Ultra hardware + Horizons UI APK
    [ALPHA] built-verified    Sherpa-ONNX Kokoro TTS in-process
    [ALPHA] built-verified    Tailscale node — mesh enrolled
    [ALPHA] built-unverified  Moonshine STT in-process on AAR (CI green · not device-tested)
    [ALPHA] built-unverified  NPU HTP pathway (QAIRT/HTP chain · bare metal only)
    [ALPHA] absent            Termux inbound listener (mic/voice/OAuth)
    [ALPHA] absent            runtime params first-class (temperature/verbosity/cores)
    [BETA ] built-verified    Jetson Orin Nano Super hardware + DDR4 SSD
    [BETA ] built-unverified  Tailscale enrollment · mesh connectivity to ALPHA
    [BETA ] absent            peer-agent deployment
    [BETA ] absent            utilities-agent deployment
    [BETA ] absent            AVNC server config (for Tab access)
    [GAMMA] built-verified    Rubik Pi 3 hardware · DragonWing SoC
    [GAMMA] built-unverified  high-speed data cable to BETA
    [GAMMA] absent            visual OS fully configured · dual monitor active
    [NET  ] built-verified    Tailscale overlay — all three nodes enrolled
    [NET  ] absent            full mesh routing verified (all paths tested)
