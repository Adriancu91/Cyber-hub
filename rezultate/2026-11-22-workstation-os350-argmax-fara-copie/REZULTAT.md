# os-350 pe placa reală — simbolul ales pe placă (argmax fără copie), 22 nov 2026 15:06

`test-placa --argmax-fara-copie` (lista implicită `lipita-ln-32`), semnal 15:02. Raportul NU a urcat singur în hub (de verificat de OS); copiat de centrul de comandă de pe stick: `raport-de-pe-stick.txt`.

**TRECE:** simbolul plăcii = procesorului 18/18; argmax 16 µs; 16 simboluri identice, 0 poziții lente. Mediana pe simbol: placa 1 076, **driver 608** (os-346: 825), jurnal 64 = 1 778 µs. **Media cu driverul 568,28 simb/s** (os-346: 508,74; DEDUS 650–685 — driverul încă 608 µs). Windows/PyTorch 129,12 → ×4,4 (limita: PyTorch fără memoria pașilor).
