# Agentul viu: Claude conduce OS-ul nostru pas cu pas (studiu A / B / C și alegerea)

- **Propus de:** centrul de comandă, la cererea lui Adrian (21 nov 2026 08:18) · **Data:** 2026-11-21
- **Proiecte implicate:** `cyber-universe` (tot codul), centrul de comandă (capătul celălalt al canalului)
- **Stare:** aprobat de Adrian în chat, 21 nov 2026 08:18 („alege una din aceste variante, cea mai bună pentru noi, și începe și această implementare ca implementare importantă pentru uneltele OS-ului”) → C-159
- **Leagă:** `idei/2026-11-19_unelte-independenta-os.md` (uneltele 3, 4, 8, 9), `cyber-universe/docs/REMOTE.md`, sarcinile OS P6-04…06, P6-49/54, P6-64, P6-73, P6-75

## Ce a cerut Adrian
- **A.** Claude pus în interiorul OS-ului. Dacă nu se poate:
- **B.** Un mic agent în OS care îi raportează tot lui Claude și face fiecare acțiune pe care i-o dă Claude, „literă cu literă, click cu click, fără greșeală”.
- **C.** Sau un program remote cu fereastră în Windows, pe laptopul ASUS TUF, de unde Claude controlează OS-ul 100 %.

## Ce există deja în OS (citit din `cyber-universe/docs/TASKS.md`)
| Varianta | Ce avem | Ce îi lipsește |
|---|---|---|
| **A** | Din octombrie: `/bin/claude` și aplicația „Claude” cu fereastră (P6-04, P6-05), cu unelte — citește/scrie fișier, listează dosar, rulează comandă — fiecare cu confirmare pe ecran (P6-06). Vorbește direct cu serviciul Claude prin HTTPS-ul nostru. | N-a rulat niciodată pe bune: cere o cheie API (`/usb/claude.key`). API-ul se plătește separat de abonament; pagina de ajutor Anthropic spune că planul Max include credite API lunare, legate de o organizație din Console. E **alt Claude**: nu știe conversația din centrul de comandă, doar ce citește din hub. Cineva trebuie să apese „Da” pe ecran. |
| **B** | `hub asculta` (P6-73): OS-ul ia comenzi din hub și pune răspunsul în hub; `ciclu-test` cu cele două chei (P6-75); actualizarea de sine cu revenire (P6-50). | Lent (o trecere la 1–60 de minute), doar lista albă de citiri, fără taste / mouse / ecran, fără sesiune „vie”. |
| **C** | Consola remote criptată (P6-49, P6-54): `remote porneste`, clientul `tools/remote-client.py`, cheia pe stick. | Merge doar din rețeaua de acasă, de pe alt calculator cu Windows; doar lista albă. Centrul de comandă nu e legat de laptop, ci de workstation — iar când workstation-ul rulează OS-ul nostru, legătura aceea e oprită. Controlul prin „fereastră” ar însemna poze de ecran și clicuri pe pixeli: lent și mai puțin exact decât comenzile scrise. Și păstrează un Windows la mijloc. |

## Alegerea: **B — agentul viu**, construit ca A să se poată porni peste el
1. **Fără costuri noi și cu un singur „creier”.** Agentul e condus de centrul de comandă (același Claude care știe planul, regulile și rezultatele), pe abonamentul existent.
2. **Fără Windows la mijloc.** Canalul trece prin hub (GitHub), singurul loc în care ajung și OS-ul, și centrul de comandă. Merge de oriunde, nu doar din rețeaua de acasă.
3. **Exact.** Comenzi scrise, numerotate, semnate, executate o singură dată, cu răspuns complet — nu clicuri ghicite pe o poză.
4. **„Mâinile” sunt aceleași pentru A.** Tot ce construim (rulează comandă, scrie, apasă, clic, citește ecranul, raportează) poate fi folosit și de Claude din OS (A), în ziua în care Adrian pune o cheie API. A devine un al doilea „șofer”, nu un proiect separat.
5. **C rămâne ce e azi:** o ușă de rezervă din rețeaua de acasă. O fereastră în care Adrian să vadă ce face agentul se poate adăuga mai târziu (hub-ul ține oricum toată convorbirea).

## Cum lucrează (forma 1 — sesiunea OS o poate îmbunătăți și scrie forma finală în `docs/LIVE.md`)
- **Pornire:** rândul `live <minute>` în `auto\teste.txt` (azi) sau la pornire, când comutatorul de pe stick va face din OS sistemul implicit. `<minute>` = cât stă fără nicio comandă până încheie singur (repornire în Windows).
- **Canalul:** ramura `os/live` din hub (nu `main` — fără zgomot în istorie), dosarul `live/<sesiune>/`. Fiecare parte doar **adaugă** fișiere, nu rescrie nimic: centrul de comandă `c-0001.json`, `c-0002.json`…; OS-ul `r-0001.json`, `r-0002.json`… și `puls.json` (starea la 60 s). OS-ul întreabă la 2–3 secunde, cu cerere condiționată (ETag), ca să nu consume limita GitHub.
- **Comanda:** `{nr, sesiune, fel, text, semnatura}`. `fel` = `comanda` (un rând de shell), `scrie` (text tastat), `tasta` (o tastă sau o combinație), `clic` / `muta` (mouse, x y), `ecran` (textul ecranului), `captura` (imagine micșorată urcată în hub), `stare`, `gata`.
- **Fără greșeală:** numărul trebuie să fie exact următorul; semnătura (HMAC-SHA-256 cu o cheie `hub/live.cheie` aflată doar pe stick și la centrul de comandă) trebuie să fie bună; fiecare număr se execută o singură dată (jurnal pe stick); altfel `REFUZAT` cu motivul. Răspunsul repetă comanda primită, apoi: codul de ieșire, durata, tot ce a scris comanda, textul ecranului după, starea (temperaturi, memorie, versiune).
- **Ce are voie:** tot ce are shell-ul OS-ului (nu doar lista albă a citirilor), inclusiv actualizarea la un Release cerut și repornirea cu reluarea sesiunii. **Rămân păzite de nucleu, ca azi:** fișierele secrete nu se arată niciodată; scrieri pe disc doar pe partiții `cyber.rw`; **placa video doar cu o cheie separată** `hub/permite-live-placa`, pusă cu „da”-ul lui Adrian (fără ea: `REFUZAT`, iar testele pe placă rămân pe ciclul automat).
- **Dacă se blochează:** ceasul de pază al plăcii de bază armat în modul viu (unealta 4), ca OS-ul înghețat să repornească singur; fără comenzi `<minute>` → încheie singur.

## Pașii (C-159)
1. Canalul viu + comenzile de shell + răspunsul complet + semnătura + „o singură dată” (QEMU, apoi Release).
2. Mâinile: `scrie`, `tasta`, `clic`, `muta`, `ecran`, `captura`.
3. Actualizarea și repornirea din sesiune (versiunea nouă ajunge pe stick fără Windows), fișiere, `puls`.
4. Ceasul de pază armat în modul viu.
5. Aceleași mâini pentru Claude din OS (A) — oprit până la „da”-ul lui Adrian și cheia API.

## Ce rămâne la Adrian
- „Da” separat pentru **comenzile pe placă din modul viu** (cheia `hub/permite-live-placa`). Până atunci placa rămâne doar pe ciclul automat.
- Dacă vrea și A: o cheie API făcută de el în Claude Console (pusă de el pe stick, `claude.key`) — nu e nevoie de ea pentru B.

## Discuție
- 2026-11-21 centrul de comandă: prima probă pe workstation = un rând `live 10` în lista de teste, cu comenzi doar de citire (`hw`, `net`, `gpu stare`), după ce pasul 1 e într-un Release cu CI verde.

## Surse
- Anthropic, „Why is Claude API usage billed separately from my paid Claude plan?”: https://support.claude.com/en/articles/9876003
- Anthropic, „Monthly API credits for Max, Ultra, and Team plans”: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans
- `cyber-universe`: `docs/TASKS.md` (P6-04…06, P6-49, P6-54, P6-64, P6-73, P6-75), `docs/REMOTE.md`
