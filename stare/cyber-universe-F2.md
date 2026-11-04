# Stare: Cyber Universe OS — F2 remote text (sesiune paralelă, `cyber-universe-F2`)

**Actualizat:** 2026-11-04 (seara, ora României) · **de:** sesiunea paralelă F2 (programată 21:07 UTC) · **ramura:** `wip/P7-F2-remote` (din `main` la `f41bf22`)
Sarcina din repo: **P6-49 (F2)** din C-68. Nu am atins `main`, `docs/STATE.md`, `docs/TASKS.md`. Sesiunea principală integrează ramura.

## Ce e gata (pe ramură)
- **Server TCP în nucleu:** `tcp::listen / accept / unlisten` (starea SYN-RECEIVED, SYN-ACK retrimis, cel mult 4 conexiuni în așteptare).
- **Serviciul `remote`** (`kernel/src/net/remote.rs`): `remote porneste [port]` (implicit 2323), `remote stare`, `remote opreste`.
  Cheia din `remote.cheie` (stick `/usb`, apoi disc `/disk`; min. 16 caractere; **niciodată în repo**) — fără cheie nu pornește.
  Cheia comparată în timp constant; 3 greșite la rând → pauză 60 s; 10 greșite → serviciul se oprește singur; o sesiune odată; 30 min inactiv → închide.
  Sesiunea = un shell propriu, **doar comenzile din lista albă** (lista buclei automate + `help`, `exit`, `remote stare|opreste`): fără `--scrie`, `gpu i6`, `gpu lant`, `reboot`, alte programe.
  Fiecare comandă și refuz în jurnal (`log remote`). `remote.cheie` adăugat la fișierele secrete (`cat` și raportul nu o arată).
  Pornire automată la boot doar dacă există `remote.porneste` lângă cheie (pentru mașina virtuală).
- **Clientul** `tools/remote-client.py` (doar biblioteca standard Python, Windows/Linux): interactiv sau `-c comanda`; cheia doar din fișier (`-k`) sau cerută ascuns.
- **Mașina virtuală:** `vm-pornire.ps1` redirecționează portul 2323 doar pe `127.0.0.1` (`-PortRemote`). Ghid: `docs/REMOTE.md`; README-uri `net/` și `shell/`.

## Teste
- Scenariu nou **`remote`** (QEMU, rețea user cu `hostfwd` 127.0.0.1:12323→2323, cheie aleatoare pusă pe discul de test de `tools/before-remote.sh`):
  fără cheie refuzat → pornire automată → 3 chei greșite refuzate → pauza → cheia bună: `uptime`, `help` răspund; `gpu i6 --scrie`, `reboot` REFUZAT; `cat` pe cheie = secret;
  `remote opreste` din sesiune oprește serviciul; cheia nu apare pe serial. **Trece local de 3 ori la rând.**
- Regresie locală: `log net tcp appnet terminal shell raport drepturi https claude-app auto` — **11/11 trec**; build-ul normal compilează.
- **CI pe ramură: VERDE** (run 41916249362, commit `fe1a1fa`): toate scenariile QEMU, inclusiv `remote`, plus testul mașinii virtuale cu `vm-pornire.ps1`.

## Ce urmează
- Sesiunea principală: integrează `wip/P7-F2-remote` în `main`, bifează P6-49 în TASKS.md.
- Adrian (când vrea să-l folosească): pune `remote.cheie` (și opțional `remote.porneste`) pe stick / discul mașinii — pași în `docs/REMOTE.md`.
- Pasul următor F2: criptare (TLS, biblioteca `tls/` există) înainte de folosirea pe rețea care nu e de încredere.
