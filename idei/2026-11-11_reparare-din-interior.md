# Idee (Adrian, 11 nov 2026): reparare „din interior”, automată, cu copie și revenire

**Propus de:** Adrian · **stare:** propus (de discutat cu sesiunile GPU și OS)

## Ideea lui Adrian
Să fim deja în OS: facem o copie, o modificăm/reparăm, o încercăm; dacă merge rămânem pe copie, dacă nu revenim automat, cu raport despre ce n-a mers.

## Ce se poate acum (pasul 1 — „variante pe stick”)
- În loc de UN singur driver per test, stick-ul de test aduce **mai multe variante** (ex. 3–5 seturi de parametri pentru GSP: GspSystemInfo, registry, argumente).
- OS-ul le încearcă **una după alta**, cu jurnal pentru fiecare; prima care trece rămâne aleasă (scrisă pe stick); cele care pică intră în raport.
- Limită reală: după o încercare eșuată placa cere **pornire rece** („WPR2 deja ridicat”). Până nu merge „recuperarea fără repornire” (propunerea `recover` din stare/cyber-universe.md),
  o încercare = o pornire. Varianta: la fiecare pornire OS-ul trece singur la următoarea variantă → Adrian doar repornește, restul e automat.
- Siguranță: scrierile pe placă rămân doar cu Adrian de față; un singur „DA” ar acoperi **lista de variante** afișată înainte.

## Mai târziu (pasul 2 — reparare reală în OS)
- Compilator Rust în OS + agent (Kronos) care scrie variante noi singur → ține de independența de Windows (C-84) și de Kronos mare. Nu acum.

## Decizii ale lui Adrian
1. Pasul 1 da/nu.
2. Un „DA” pentru toată lista de variante (în loc de un DA per încercare) da/nu.
