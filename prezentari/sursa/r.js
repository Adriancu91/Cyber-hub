const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:960,height:540}});
const f=process.argv[2],o=process.argv[3];
await p.goto('file:///home/claude/prez2/'+f,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:o,width:'960px',height:'540px',printBackground:true});await b.close();})();
