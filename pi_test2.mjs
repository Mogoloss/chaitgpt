import { complete, stream } from 'file:///C:/OpenClaw/npm-global/node_modules/openclaw/node_modules/@mariozechner/pi-ai/dist/index.js';
const model={provider:'minimax',api:'anthropic-messages',baseUrl:'https://api.minimaxi.com/anthropic',id:'MiniMax-M2.5-highspeed',name:'MiniMax',reasoning:false,input:['text'],cost:{input:0.3,output:1.2,cacheRead:0.03,cacheWrite:0.12},contextWindow:200000,maxTokens:8192};
const apiKey='sk-cp-4HnmHh1gmo9BiUjEGzUZgts7Jk1dd_MUTZbdFJCJh2dwj3_t94kOkN1F73DubaEx39PkgEY0j207hPPtYd_Lht0rnEbqSoR1WjeU79Mofya1cnpeqCTzupE';
const body={messages:[{role:'user',content:'Reply with OK only.',timestamp:Date.now()}]};
const opts={apiKey,maxTokens:256};
console.log('start complete');
const t0=Date.now();
try{const out=await complete(model,body,opts); console.log('complete ms',Date.now()-t0,JSON.stringify(out));}catch(e){console.error('complete err',Date.now()-t0,e?.stack||e)}
console.log('start stream');
const t1=Date.now();
try{const s=await stream(model,body,opts); for await (const ev of s){ console.log('ev',Date.now()-t1,ev.type); if(ev.type==='done'||ev.type==='error') console.log(JSON.stringify(ev)); }}catch(e){console.error('stream err',Date.now()-t1,e?.stack||e)}
