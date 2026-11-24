# os-389 pe placa reală — pasul de antrenare pe bucăți, 24 nov 2026 05:22

`test-placa --antrenare-mini --vram`, semnal 05:12. Raport: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-0522.txt`.

**TRECE (aceleași numere).** Pasul întreg 370,2 ms (median): planul lotului 0,03 · lotul sus 0,05 · lista 0,07 · **trimitere + așteptare 270,0** · **pierderile + norma jos 100,0 ms**. Trimiterea pe bucăți: pushbuffer 0,004 · **golirea în VRAM 102,0** · **TLB 67,4** · **soneria 33,4** · **așteptarea 33,4** (placa lucrează doar 3,65) · înregistrările citite 16,9 ms.

**Observația centrului de comandă:** aproape toate bucățile lente sunt multipli de ~33,4 ms (33 / 67 / 100 / 17 ≈ ½) — semn al unei pauze/ceas cu pasul de ~33 ms (ex. o așteptare cu „sleep” la granulația ceasului, sau o citire care așteaptă o întrerupere de ceas), nu al plăcii. De verificat în P6-174: așteptarea prin interogare strânsă (spin) sau semafor, nu prin pauză.
