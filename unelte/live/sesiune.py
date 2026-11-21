#!/usr/bin/env python3
"""Proba agentului viu pe workstation: sesiunea A (se incheie cu `gata`) sau B (se incheie singura, la timp)."""
import json, os, secrets, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import live

which = sys.argv[1]
known = set(sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else set()
OUT = os.path.join(live.HERE, "rezultate")
def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)

# 1. astept sesiunea noua
t0 = time.time(); S = None
while time.time() - t0 < 1500:
    new = [s for s in live.sessions() if s not in known]
    if new:
        head = live.get(f"live/{new[-1]}/sesiune.json")
        if head:
            S = new[-1]; break
    time.sleep(5)
if not S:
    log("NICIO SESIUNE in 25 de minute"); sys.exit(2)
D = os.path.join(OUT, S); os.makedirs(D, exist_ok=True)
open(os.path.join(D, "sesiune.json"), "wb").write(head)
log("sesiunea", S, head.decode()[:300])

OK = ("ok",)
def R(p): return ("REFUZAT", p)
sent = {}; rows = []; nr = 0
def step(kind, text, expect, raw=None, note="", must=None):
    """Trimite fisierul cu numarul urmator, asteapta raspunsul, verifica."""
    global nr
    nr += 1
    data = raw(S, nr) if raw else live.command_bytes(S, nr, kind, text)
    sent[nr] = data
    open(os.path.join(D, live.fname("c", nr)), "wb").write(data)
    t = time.time()
    live.put(f"live/{S}/{live.fname('c', nr)}", data, f"live: {live.fname('c', nr)} (centrul de comanda)")
    reply, waited = live.wait(f"live/{S}/{live.fname('r', nr)}", timeout=150)
    return record(nr, kind, text, expect, data, reply, time.time() - t, note, must)

def record(n, kind, text, expect, data, reply, secs, note="", must=None):
    if reply is None:
        rows.append({"nr": n, "fel": kind, "text": text[:80], "asteptat": expect[0], "probleme": ["FARA RASPUNS"], "s": round(secs, 1), "nota": note})
        log(f"c-{n:04d} {kind} {text[:40]!r}: FARA RASPUNS dupa {secs:.0f}s"); return None
    open(os.path.join(D, live.fname("r", n)), "wb").write(reply)
    r, problems = live.check(data, reply, S, n, expect)
    if live.KEY in reply or live.KEY.hex().encode() in reply or live.KEY.hex().upper().encode() in reply:
        problems.append("CHEIA VIE APARE IN RASPUNS")
    if must and r is not None and not any(m in (r.get("iesire") or "") for m in must):
        problems.append(f"iesirea nu contine niciuna din {must!r}: {(r.get('iesire') or '')[:120]!r}")
    row = {"nr": n, "fel": kind, "text": text[:80], "asteptat": expect[0] + (": " + expect[1] if len(expect) > 1 else ""),
           "stare": r and r.get("stare"), "motiv": r and r.get("motiv"), "nr_raspuns": r and r.get("nr"), "cod": r and r.get("cod"),
           "durata_ms": r and r.get("durata_ms"), "iesire_octeti": r and len(r.get("iesire", "") or ""), "s": round(secs, 1), "probleme": problems, "nota": note}
    rows.append(row)
    log(f"c-{n:04d} {kind} {text[:40]!r}: {row['stare']} {('cod '+str(row['cod'])) if row['cod'] is not None else (row['motiv'] or '')!s:.70} [{secs:.1f}s] {'OK' if not problems else 'PROBLEME: '+'; '.join(problems)}")
    return r

other_key = secrets.token_bytes(48)
def bad_sig(s, n): return live.command_bytes(s, n, "comanda", "mem", signature="0" * 64)
def wrong_nr(s, n): return live.command_bytes(s, n + 77, "comanda", "mem")
def other_session(s, n): return live.command_bytes("s-19990101-0000", n, "comanda", "mem")
def with_other_key(s, n): return live.command_bytes(s, n, "comanda", "mem", signature=live.sign(s, n, "comanda", "mem", key=other_key))
def not_json(s, n): return b"salut, eu nu sunt JSON"

if which == "A":
    for c in ["hw", "mem", "uptime", "net", "lspci", "discuri", "lsusb", "cpu", "log --sumar", "ls /", "ls /usb", "cat /usb/VERSIUNE",
              "gpu identifica", "gpu stare", "help", "hw lista", "wifi", "remote stare"]:
        if nr == 0: step("stare", "", OK)
        step("comanda", c, OK)
    step("stare", "", OK)
    # probele de refuz
    step("comanda", "mem", R("semnatura gresita"), raw=bad_sig, note="semnatura din zerouri")
    step("comanda", "mem", R(f"numar gresit: astept nr {nr + 1}"), raw=wrong_nr, note="nr din fisier = numarul bun + 77")
    step("comanda", "hw", R("comanda repetata: nr 2"), raw=lambda s, n: sent[2], note="copia exacta a lui c-0002")
    step("comanda", "gpu lant", R("comanda scrie in placa video"))
    step("comanda", "test-placa", R("comanda scrie in placa video"))
    step("comanda", "run kronos --gpu --n 4 Ana", R("comanda scrie in placa video"))
    step("comanda", "live 5", R("o sesiune vie nu porneste alta sesiune vie"))
    step("clic", "10 10", R("felul acesta vine la pasul 2"))
    step("comanda", "mem", R("fisierul comenzii nu e JSON valid"), raw=not_json, note="fisier care nu e JSON")
    step("comanda", "mem", R("alta sesiune"), raw=other_session, note="semnata pentru alta sesiune")
    step("comanda", "mem", R("semnatura gresita"), raw=with_other_key, note="semnata cu alta cheie")
    # dupa refuzuri, sirul merge mai departe
    for c in ["mem", "uptime"]:
        step("comanda", c, OK)
    step("stare", "", OK)
    step("gata", "", OK)
elif which == "C":
    step("stare", "", OK)
    for c in ["hw", "mem", "uptime", "net", "lspci", "discuri", "lsusb", "cpu", "ls /usb", "ls /usb/hub", "cat /usb/VERSIUNE", "gpu stare",
              "cat /usb/KRONOS/kronos_651_q8_0.kgr.sha256"]:
        step("comanda", c, OK)
    SEC = ["secret", "nu exista", "refuz"]
    step("comanda", "cat /usb/hub/live.cheie", OK, must=SEC, note="cheia nu se arata")
    step("comanda", "cat /usb/hub/LIVE.CHEIE", OK, must=SEC, note="cu litere mari")
    step("comanda", "cat /usb/hub/../hub/./live.cheie", OK, must=SEC, note="cale ocolita")
    step("comanda", "cat /usb/hub/LIVE~1.CHE", OK, must=SEC, note="numele scurt al fisierului")
    step("comanda", "cat /usb/hub/live/../live.cheie", OK, must=SEC, note="cale ocolita prin subdosar")
    step("comanda", "compara /usb/hub/live.cheie /usb/VERSIUNE", OK, must=SEC, note="compara cu cheia")
    step("comanda", "cat /usb/hub/permite-live-placa", OK, must=SEC, note="cheia placii (nu exista inca)")
    step("comanda", "mem", R("semnatura gresita"), raw=bad_sig, note="semnatura din zerouri")
    step("comanda", "gpu lant", R("comanda scrie in placa video"))
    for c in ["mem", "uptime"]:
        step("comanda", c, OK)
    step("stare", "", OK)
    step("gata", "", OK)
else:
    step("stare", "", OK)
    # 10 comenzi puse deodata, intr-un singur commit: trebuie luate in ordine, fiecare o data
    batch = ["hw", "mem", "uptime", "net", "lsusb", "lspci", "discuri", "cpu", "log --sumar", "ls /usb/hub"]
    repo = os.path.join(live.HERE, "repo")
    if not os.path.isdir(repo):
        subprocess.run(["git", "clone", "-q", "--depth", "1", "-b", live.BRANCH, f"https://github.com/{live.REPO}", repo], check=True)
    subprocess.run(["git", "-C", repo, "pull", "-q", "--rebase"], check=True)
    os.makedirs(os.path.join(repo, "live", S), exist_ok=True)
    first = nr + 1; items = []
    for c in batch:
        nr += 1
        data = live.command_bytes(S, nr, "comanda", c); sent[nr] = data; items.append((nr, c, data))
        open(os.path.join(repo, "live", S, live.fname("c", nr)), "wb").write(data)
        open(os.path.join(D, live.fname("c", nr)), "wb").write(data)
    subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
    subprocess.run(["git", "-C", repo, "-c", "user.name=Centrul de comanda", "-c", "user.email=adriancu91@users.noreply.github.com", "commit", "-q", "-m",
                    f"live: c-{first:04d}..c-{nr:04d} deodata (centrul de comanda)" + live.TRAILER], check=True)
    t = time.time()
    for i in range(4):
        if subprocess.run(["git", "-C", repo, "push", "-q"]).returncode == 0: break
        subprocess.run(["git", "-C", repo, "pull", "-q", "--rebase"]); time.sleep(2)
    log(f"lot de {len(batch)} comenzi urcat intr-un singur commit")
    for n, c, data in items:
        reply, waited = live.wait(f"live/{S}/{live.fname('r', n)}", timeout=240)
        record(n, "comanda", c, OK, data, reply, time.time() - t, note="din lotul de 10")
    # ecoul: semne speciale, forme diferite de JSON
    special = 'help ăîâșț ĂÎÂȘȚ „ghilimele” "drepte" \\ linie / {acolade} [paranteze] é ñ 漢字 😀 <&> %s $x'
    step("comanda", special, OK, note="semne speciale, UTF-8 direct")
    step("comanda", special, OK, raw=lambda s, n: live.command_bytes(s, n, "comanda", special, ascii_only=True, newline=True), note="aceleasi semne ca \\uXXXX + rand nou la sfarsit")
    step("comanda", "  uptime  ", OK, note="spatii in jur")
    step("comanda", "help " + "x" * 3000, OK, note="text lung (3 000 de semne)")
    def pretty(s, n):
        return json.dumps({"semnatura": live.sign(s, n, "comanda", "mem"), "text": "mem", "fel": "comanda", "sesiune": s, "nr": n}, indent=2).encode()
    step("comanda", "mem", OK, raw=pretty, note="JSON asezat altfel (alta ordine, randuri)")
    r = step("comanda", "comanda-care-nu-exista", OK, note="comanda necunoscuta: cod 127")
    step("comanda", "cat /usb/nu-exista.txt", OK, note="fisier care nu exista")
    step("comanda", special, R(f"comanda repetata: nr {first + 10}"), raw=lambda s, n: sent[first + 10], note="copia exacta a comenzii cu semne speciale")
    step("comanda", "mem", R(f"numar gresit: astept nr {nr + 1}"), raw=lambda s, n: live.command_bytes(s, n + 1, "comanda", "mem"), note="nr din fisier = urmatorul + 1")
    step("comanda", "mem", OK, note="numarul sarit mai sus e acum cel bun")
    step("comanda", "gpu i6 --scrie", R("comanda scrie in placa video"))
    step("comanda", "timp gpu recupereaza", R("comanda scrie in placa video"))
    step("comanda", "mem", R("semnatura gresita"), raw=bad_sig, note="semnatura din zerouri")
    step("comanda", "uptime", OK)
    step("stare", "", OK)
    last = time.time()
    log("nu mai trimit nimic: sesiunea trebuie sa se incheie singura dupa 2 minute")
    time.sleep(175)
    # o comanda sosita dupa sfarsit nu trebuie executata
    nr += 1
    late = live.command_bytes(S, nr, "comanda", "mem"); sent[nr] = late
    open(os.path.join(D, live.fname("c", nr) + ".tarzie"), "wb").write(late)
    live.put(f"live/{S}/{live.fname('c', nr)}", late, f"live: {live.fname('c', nr)} dupa sfarsitul sesiunii (proba)")
    reply, waited = live.wait(f"live/{S}/{live.fname('r', nr)}", timeout=75)
    rows.append({"nr": nr, "fel": "comanda", "text": "mem (trimisa dupa sfarsitul sesiunii)", "asteptat": "FARA RASPUNS",
                 "probleme": [] if reply is None else ["A RASPUNS dupa sfarsitul sesiunii"], "s": round(waited, 1), "nota": "comanda tarzie"})
    log(f"c-{nr:04d} tarzie: {'fara raspuns (corect)' if reply is None else 'A RASPUNS (gresit)'}")

bad = [r for r in rows if r["probleme"]]
ok_run = sum(1 for r in rows if r.get("stare") == "ok"); ref = sum(1 for r in rows if r.get("stare") == "REFUZAT")
summary = {"sesiune": S, "fel": which, "comenzi": len(rows), "executate": ok_run, "refuzate": ref, "cu_probleme": len(bad),
           "secunde_pe_comanda_median": sorted(r["s"] for r in rows)[len(rows) // 2]}
json.dump({"sumar": summary, "randuri": rows}, open(os.path.join(D, "raport.json"), "w"), ensure_ascii=False, indent=1)
log("SUMAR", json.dumps(summary, ensure_ascii=False))
for r in bad: log("PROBLEMA", json.dumps(r, ensure_ascii=False))
