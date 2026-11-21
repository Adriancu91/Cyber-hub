#!/usr/bin/env python3
"""Capatul centrului de comanda al canalului viu (C-159, cyber-universe/docs/LIVE.md, forma cyber-live-1).
Scrie c-NNNN.json pe ramura os/live din hub, asteapta r-NNNN.json, compara ecoul octet cu octet."""
import base64, hmac, json, subprocess, sys, time, os

REPO = "Adriancu91/Cyber-hub"
BRANCH = "os/live"
FORM = "cyber-live-1"
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = open(os.path.join(HERE, "live.cheie"), "rb").read()
assert len(KEY) >= 32
TRAILER = "\n\nCo-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01CjEVdPnw2fqsmLxdNSSKYi"

def gh(args, inp=None):
    p = subprocess.run(["gh", "api"] + args, input=inp, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

def sign(session, nr, kind, text, key=KEY):
    return hmac.new(key, f"{FORM}\n{session}\n{nr}\n{kind}\n{text}".encode(), "sha256").hexdigest()

def command_bytes(session, nr, kind, text, signature=None, ascii_only=False, newline=False):
    d = {"nr": nr, "sesiune": session, "fel": kind, "text": text,
         "semnatura": signature if signature is not None else sign(session, nr, kind, text)}
    s = json.dumps(d, ensure_ascii=ascii_only)
    return (s + ("\n" if newline else "")).encode()

def sessions():
    rc, out, err = gh([f"repos/{REPO}/contents/live?ref={BRANCH}"])
    if rc != 0:
        return []
    return sorted(e["name"] for e in json.loads(out) if e["type"] == "dir")

def get(path):
    rc, out, err = gh([f"repos/{REPO}/contents/{path}?ref={BRANCH}"])
    if rc != 0:
        return None
    d = json.loads(out)
    return base64.b64decode(d["content"])

REPO_DIR = os.path.join(HERE, "repo")
def _git(*args, check=False):
    return subprocess.run(["git", "-C", REPO_DIR, "-c", "user.name=Centrul de comanda", "-c", "user.email=adriancu91@users.noreply.github.com"] + list(args), capture_output=True, text=True, check=check)

def put(path, data, msg):
    """Scrie un fisier NOU pe ramura os/live prin git (scrierea prin API e oprita de proxy). Nu rescrie nimic."""
    if not os.path.isdir(REPO_DIR):
        subprocess.run(["git", "clone", "-q", "--depth", "20", "-b", BRANCH, f"https://github.com/{REPO}", REPO_DIR], check=True)
    full = os.path.join(REPO_DIR, path)
    last = ""
    for attempt in range(8):
        _git("pull", "-q", "--rebase")
        if attempt == 0 and os.path.exists(full):
            raise RuntimeError(f"{path} exista deja: nu rescriu nimic")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        if not os.path.exists(full):
            open(full, "wb").write(data)
            _git("add", "-A"); _git("commit", "-q", "-m", msg + TRAILER)
        p = _git("push", "-q")
        if p.returncode == 0:
            return True
        last = p.stderr
        time.sleep(1 + attempt)
    raise RuntimeError(f"nu am putut urca {path}: {last[:300]}")

def wait(path, timeout=120, every=2.0):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = get(path)
        if d is not None:
            return d, time.time() - t0
        time.sleep(every)
    return None, time.time() - t0

def fname(prefix, nr):
    return f"{prefix}-{nr:04d}.json"

def check(sent: bytes, reply: bytes, session, file_nr, expect):
    """expect = ("ok", None) sau ("REFUZAT", inceputul motivului, nr asteptat in raspuns sau 'acelasi'/None)"""
    problems = []
    try:
        r = json.loads(reply.decode("utf-8"))
    except Exception as e:
        return None, [f"raspunsul nu e JSON: {e}"]
    if r.get("forma") != FORM: problems.append(f"forma {r.get('forma')!r}")
    if r.get("sesiune") != session: problems.append(f"sesiune {r.get('sesiune')!r}")
    echo = r.get("ecou")
    if not isinstance(echo, str) or echo.encode("utf-8") != sent:
        problems.append("ECOUL DIFERA de ce am trimis")
    if expect[0] == "ok":
        if r.get("stare") != "ok": problems.append(f"stare {r.get('stare')!r} motiv {r.get('motiv')!r}")
        if r.get("nr") != file_nr: problems.append(f"nr {r.get('nr')!r} (asteptat {file_nr})")
        for k in ("cod", "durata_ms", "iesire", "ecran", "sistem"):
            if k not in r: problems.append(f"lipseste {k}")
    else:
        if r.get("stare") != "REFUZAT": problems.append(f"NU a fost refuzat: stare {r.get('stare')!r}")
        if not str(r.get("motiv", "")).startswith(expect[1]): problems.append(f"motiv {r.get('motiv')!r} (asteptat: {expect[1]!r}…)")
        if "iesire" in r or "cod" in r: problems.append("un refuz nu trebuie sa aiba iesire/cod")
    return r, problems
