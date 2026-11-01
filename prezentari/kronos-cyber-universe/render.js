const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('file://'+__dirname+'/prezentare.html');
await p.pdf({path:__dirname+'/Kronos-Cyber-Universe-unde-suntem.pdf',width:'1280px',height:'720px',printBackground:true});
const n=await p.$$('.s');for(let i=0;i<n.length;i++){await n[i].screenshot({path:__dirname+`/d${i+1}.png`});}
await b.close();})();
