// genereaza SVG-ul logoului Kronos la momentul t (secunde, bucla de 6 s)
function logo(t, W, transp){
  W=W||720; const C=W/2, T=6, ph=(t%T)/T, TAU=Math.PI*2;
  const mods=[
    ['CYBER-GPU','driver'],['CYBER UNIVERSE','sistem'],['MEMORIE','date'],
    ['REȚEA','internet'],['UNELTE','agenți'],['ANTRENARE','învățare']];
  const R=W*0.36; let s='';
  s+=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${W}" viewBox="0 0 ${W} ${W}">
<defs>
<radialGradient id="bg" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#1a2230"/><stop offset="1" stop-color="#05070a"/></radialGradient>
<linearGradient id="steel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f7fb"/><stop offset=".28" stop-color="#9aa6b6"/><stop offset=".5" stop-color="#e6ebf2"/><stop offset=".72" stop-color="#6b7686"/><stop offset="1" stop-color="#c9d1dc"/></linearGradient>
<linearGradient id="steel2" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#3b4452"/><stop offset=".5" stop-color="#aab4c2"/><stop offset="1" stop-color="#2a313c"/></linearGradient>
<linearGradient id="txt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".48" stop-color="#c3ccd8"/><stop offset=".52" stop-color="#7d8898"/><stop offset="1" stop-color="#dfe5ec"/></linearGradient>
<radialGradient id="core" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#7fe3ff" stop-opacity=".9"/><stop offset=".55" stop-color="#1b8cff" stop-opacity=".25"/><stop offset="1" stop-color="#1b8cff" stop-opacity="0"/></radialGradient>
</defs>
${transp?"":`<rect width="${W}" height="${W}" fill="url(#bg)"/>`}`;
  // stele
  let seed=7; const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
  for(let i=0;i<(transp?0:90);i++){const x=rnd()*W,y=rnd()*W,r=rnd()*1.3+.3,tw=.35+.65*Math.abs(Math.sin(TAU*(ph*2+rnd())));s+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${r.toFixed(2)}" fill="#cfe7ff" opacity="${(tw*.7).toFixed(2)}"/>`;}
  // orbite
  s+=`<circle cx="${C}" cy="${C}" r="${R}" fill="none" stroke="#5b6676" stroke-width="1.2" stroke-dasharray="3 7" transform="rotate(${(ph*360).toFixed(2)} ${C} ${C})"/>`;
  s+=`<circle cx="${C}" cy="${C}" r="${R*0.62}" fill="none" stroke="#3d4654" stroke-width="1" stroke-dasharray="1 9" transform="rotate(${(-ph*360).toFixed(2)} ${C} ${C})"/>`;
  // module + legaturi + impulsuri
  const rot=ph*TAU/6;
  mods.forEach((m,i)=>{
    const a=-Math.PI/2+i*TAU/6+rot, x=C+R*Math.cos(a), y=C+R*Math.sin(a);
    const x0=C+W*0.135*Math.cos(a), y0=C+W*0.135*Math.sin(a);
    s+=`<line x1="${x0.toFixed(1)}" y1="${y0.toFixed(1)}" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" stroke="#4fa8ff" stroke-opacity=".45" stroke-width="1.4"/>`;
    for(let k=0;k<2;k++){const p=((ph*2+i/6+k*.5)%1), px=x0+(x-x0)*p, py=y0+(y-y0)*p;
      s+=`<circle cx="${px.toFixed(1)}" cy="${py.toFixed(1)}" r="${W*0.009}" fill="#9fe9ff" opacity="${(Math.sin(Math.PI*p)).toFixed(2)}"/>`;}
    const hr=W*0.052, pts=[...Array(6)].map((_,j)=>{const b=Math.PI/6+j*TAU/6;return (x+hr*Math.cos(b)).toFixed(1)+','+(y+hr*Math.sin(b)).toFixed(1)}).join(' ');
    const pulse=.5+.5*Math.sin(TAU*(ph*2-i/6));
    s+=`<polygon points="${pts}" fill="#11161e" stroke="url(#steel)" stroke-width="3"/>`;
    s+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(hr*0.35).toFixed(1)}" fill="#4fd2ff" opacity="${(.35+.6*pulse).toFixed(2)}"/>`;
    const ly=y+hr+W*0.032;
    s+=`<text x="${x.toFixed(1)}" y="${ly.toFixed(1)}" text-anchor="middle" font-family="Orbitron" font-weight="700" font-size="${(W*0.021).toFixed(1)}" letter-spacing="1.5" fill="#d7dee8">${m[0]}</text>`;
  });
  // miezul
  const g=.75+.25*Math.sin(TAU*ph*2);
  s+=`<circle cx="${C}" cy="${C}" r="${(W*0.2*g).toFixed(1)}" fill="url(#core)"/>`;
  const hr=W*0.13, hex=[...Array(6)].map((_,j)=>{const b=-Math.PI/2+j*TAU/6;return (C+hr*Math.cos(b)).toFixed(1)+','+(C+hr*Math.sin(b)).toFixed(1)}).join(' ');
  const hr2=W*0.112, hex2=[...Array(6)].map((_,j)=>{const b=-Math.PI/2+j*TAU/6;return (C+hr2*Math.cos(b)).toFixed(1)+','+(C+hr2*Math.sin(b)).toFixed(1)}).join(' ');
  s+=`<polygon points="${hex}" fill="url(#steel2)" stroke="url(#steel)" stroke-width="5"/>`;
  s+=`<polygon points="${hex2}" fill="#0b0f15" stroke="#4fd2ff" stroke-opacity="${(.4+.5*g).toFixed(2)}" stroke-width="1.5"/>`;
  s+=`<text x="${C}" y="${(C+W*0.012).toFixed(1)}" text-anchor="middle" font-family="Orbitron" font-weight="900" font-size="${(W*0.036).toFixed(1)}" letter-spacing="2" fill="url(#txt)">KRONOS</text>`;
  s+=`<text x="${C}" y="${(C+W*0.048).toFixed(1)}" text-anchor="middle" font-family="Orbitron" font-weight="700" font-size="${(W*0.014).toFixed(1)}" letter-spacing="3" fill="#4fd2ff">NUCLEUL AI</text>`;
  s+='</svg>'; return s;
}
if(typeof module!=='undefined') module.exports=logo;
