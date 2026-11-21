const { chromium } = require('playwright'); const logo=require('./logo.js'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:720}});
await p.setContent('<html><head><link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap&subset=latin-ext" rel="stylesheet"><style>html,body{margin:0;background:#05070a}</style></head><body><div id="d"></div></body></html>',{waitUntil:'networkidle'});
await p.evaluate(()=>document.fonts.ready);
fs.mkdirSync('fr',{recursive:true});
const N=+process.argv[2]||180;
for(let i=0;i<N;i++){const svg=logo(i*6/N,720);await p.evaluate(s=>{document.getElementById('d').innerHTML=s},svg);
 await p.waitForTimeout(5); await p.screenshot({path:`fr/f${String(i).padStart(4,'0')}.png`});}
fs.writeFileSync('logo-static.svg',logo(0.8,720));
await b.close();})();
