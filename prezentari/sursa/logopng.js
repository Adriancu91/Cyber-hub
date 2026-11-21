const { chromium } = require('playwright'); const logo=require('./logo.js');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:900}});
await p.setContent('<html><head><link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap&subset=latin-ext" rel="stylesheet"><style>html,body{margin:0;background:transparent}</style></head><body><div id="d"></div></body></html>',{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);
await p.evaluate(s=>{document.getElementById('d').innerHTML=s},logo(0.8,900,true));
await p.screenshot({path:'logo-transparent.png',omitBackground:true,clip:{x:0,y:0,width:900,height:900}});await b.close();})();
