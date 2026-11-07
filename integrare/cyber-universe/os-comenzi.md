# Comenzi pentru Cyber Universe OS (rulate de OS pe workstation)

Aici scrie Adrian (sau centrul de comandă, pentru el) ce să ruleze OS-ul singur. În OS: `hub ruleaza` (sau la fiecare
pornire, dacă pe stick există fișierul gol `hub/la-pornire`). Raportul ajunge în `rezultate/os-automat/<data>/hub-….txt`.

Reguli (P6-64, comanda C-87 pct. 2):
- un rând = o comandă: `- [ ] K-<număr>: <comandă>` (numărul nu se refolosește; fiecare rulează **o singură dată**);
- rulează **doar** lista albă: `test tot`, `raport`, `trimite`, `hw`, `hw lista`, `lspci`, `lsusb`, `net`, `mem`, `uptime`,
  `log …`, `ls`/`cat …`, `cpu`, `gpu`, `gpu identifica`, `gpu tur`, `gpu plan`, `run kronos --profil …`, `run kronos --control`;
- **refuzate mereu**: `gpu lant`, orice `--gpu` sau `--scrie`, `reboot`, `DA`, ștergeri, actualizări, alte programe —
  acestea le pornește doar Adrian, la tastatură;
- `- [x]` = sărit (bifat de mână). Cel mult 20 de comenzi pe o rulare.

Exemplu: un rând `K-1: test tot` și unul `K-2: run kronos --control`, fiecare începând cu „- [ ] ” (liniuță, spațiu, paranteze
pătrate cu spațiu între ele, spațiu). Blocurile de cod (între ```) sunt ignorate de OS.

## Comenzi
