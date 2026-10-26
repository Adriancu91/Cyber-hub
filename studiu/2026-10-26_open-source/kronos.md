# Studiu: proiecte open-source ca inspirație pentru Kronos

*Scris de cercetător (Claude Code), 26 octombrie 2026. Am citit doar, n-am modificat niciun repo și n-am rulat cod descărcat.

**Cum să citești notițele.** Fiecare afirmație are una dintre etichete:
- **[CITIT]**: am citit-o eu în fișierul sau pagina indicată.
- **[MEMORIE]**: o știu din lucrări sau cunoștințe generale și n-am verificat-o acum. Trebuie verificată înainte să conteze într-o decizie.
- **[DEDUCȚIE]**: o concluzie a mea, pe care încă n-a măsurat-o nimeni.

**Ce am aflat despre Kronos, citind repo-ul `cyberspace` (doar citit).** Le-am folosit ca să potrivesc propunerile:
- Linia principală pe workstation (`config/ws_w2.toml`) are 12 straturi × 768, 12 capete, context 512 și vocabular 16.384, adică 98,0 M parametri. Lotul are 12 secvențe × 512 = **6.144 de simboluri pe pas**. Optimizatorul e AdamW (lr 0,00025 constant, weight_decay 0,1), cu tăierea gradientului la 1,0 și bf16 prin autocast. Fiecare noapte se termină cu o „copie răcită” de 30 de minute. **[CITIT]**
- Arhitectura e în stilul GPT-2 (`module/model_gpt.py`): poziții învățate (`emb_pozitie`), LayerNorm, GELU, `nn.MultiheadAttention` cu mască booleană și intrarea legată de ieșire (`cap.weight = emb_token.weight`). **[CITIT]**
- Viteza: ~21.265 de pași pe oră (raportul S12), deci ~5,9 pași/s ≈ **36.000 de simboluri/s**. Într-o noapte de 10 ore intră ~1,3 miliarde de simboluri. **[CITIT + calcul]**
- Amestecul de date: 45,9 % engleză simplă, 33,9 % română, 15,1 % cod Python și 5,1 % numere, în total 4,89 GB. **[CITIT, ws_w2.toml]**
- Memoria E3 (`unelte/e3_memorie.py`): SQLite FTS5, BM25 (k1 = 1,2, b = 0,75), tokenizerul `unicode61`, care scoate diacriticele, și ş/ţ → ș/ț. **Nu folosește rădăcini de cuvinte (stemming)**: „orașului” și „orașul” sunt cuvinte diferite pentru index. **[CITIT]**

---

## 1. Tabelul proiectelor

Licența e luată din fișierul LICENSE al fiecărui repo clonat, cu excepția rândurilor marcate „(pagina web)”.

| Proiect | Link | Licență | Ce am învățat (concret) | Unde se aplică la Kronos | Cod folosibil? |
|---|---|---|---|---|---|
| modded-nanogpt (speedrun-ul) | github.com/KellerJordan/modded-nanogpt | MIT | Lista ordonată a trucurilor care au scurtat antrenarea de la 45 la sub 2 minute, fiecare cu jurnal și test statistic. Un antrenor simplu de 372 de rânduri (`records/track_3_optimization/train_gpt_simple.py`). Muon are nevoie de ~3.500–3.600 de pași, AdamW de 5.625, pentru aceeași pierdere. | Antrenarea lui #415 și a unei linii noi (Propunerile 1 și 4) | Da, cu atribuire |
| Muon | github.com/KellerJordan/Muon | MIT | Muon se folosește doar pe matricile ascunse. Intrarea, ieșirea și parametrii mici rămân pe AdamW. De reglat sunt doar lr și wd; momentum 0,95, Nesterov și 5 pași Newton-Schulz merg de obicei. | Propunerea 1 | Da, cu atribuire (~60 de rânduri) |
| nanochat (Karpathy) | github.com/karpathy/nanochat | MIT | Măsura `val_bpb` (biți pe octet, aceeași idee ca la examenul Kronos). Un singur „buton”, adâncimea, de care depind toate celelalte setări. Arhitectura „modernă” (RoPE, QK-norm, ReLU², RMSNorm fără parametri, fără bias, GQA). RL simplificat (REINFORCE cu media ca bază). | Propunerile 1, 4 și 5 | Da, cu atribuire |
| nanoGPT | github.com/karpathy/nanoGPT | MIT | Strămoșul celorlalte. L-am clonat, dar nu l-am studiat în detaliu, pentru că modded-nanogpt și nanochat sunt versiunile lui moderne. | — | Da, cu atribuire |
| llama2.c | github.com/karpathy/llama2.c | MIT | `run.c` (973 de rânduri) face toată inferența cu libc, math și mmap. `runq.c` folosește cuantizare Q8_0 pe grupuri: 4× mai mic, de ~3× mai rapid (7B: 4,6 → 14 simboluri/s, după README). Un tokenizer mic (4.096) ajunge la aceeași lungime de secvență ca unul de 32.000 pe textul lui. | Inferența în Cyber Universe (Propunerea 3) | Da, cu atribuire |
| llm.c | github.com/karpathy/llm.c | MIT | Corectitudinea se verifică cu o „stare de control”: PyTorch scrie logits și pierderea, iar implementarea C trebuie să le reproducă (README, r. 105). | Propunerea 3 (metoda de testare) | Da, cu atribuire |
| ggml (formatul GGUF) | github.com/ggml-org/ggml | MIT | Q8_0 = blocuri de 32 de valori cu o scară fp16 (34 de octeți la 32 de greutăți). Q4_0 = 18 octeți la 32 (`src/ggml-common.h`). GGUF are antet cu chei-valori, e little-endian și are aliniere 32 (`docs/gguf.md`). | Formatul fișierului de model pentru OS | Doar ideea formatului (cod prea mare pentru no_std) |
| bm25s | github.com/xhluca/bm25s | MIT | BM25 „eager”: scorurile se calculează la indexare și se țin într-o matrice rară. Are 5 variante de formulă (Robertson, Lucene, ATIRE, BM25L, BM25+). **Nu are cuvinte de legătură românești** (`stopwords.py` are EN, DE, NL, FR, ES, PT, IT, RU, SV). | Memoria (E3), ca alternativă la FTS5 | Da, cu atribuire |
| Pyserini / Anserini | github.com/castorini/pyserini | Apache-2.0 | Tabele oficiale pe MS MARCO (`docs/2cr/msmarco-v1-passage.html`). **Extinderea documentelor cu întrebări generate (doc2query)** a urcat MRR@10 de la 0,184 la 0,272. RM3 a urcat recall@1000, dar a **coborât** MRR@10 (0,184 → 0,157). Fuziunea RRF are k = 60 (`pyserini/fusion/_base.py`). | Propunerea 2 | Da, cu atribuire și notița Apache |
| ColBERT v2 / PLAID | github.com/stanford-futuredata/ColBERT | MIT | Interacțiunea „târzie”: câte un vector pe cuvânt, iar scorul e MaxSim. Cere un encoder BERT antrenat supervizat. | (vezi „Ce NU merită”) | Doar idei, pentru acum |
| SmolLM (Hugging Face) | github.com/huggingface/smollm | Apache-2.0 | Modelul de 135M e adânc și subțire: 30 de straturi × 576, GQA 9/3, intrarea legată de ieșire, lr 0,003. Rata merge WSD (constantă, apoi scade liniar pe ultimii 20 %). FineWeb-Edu e filtrat cu un clasificator antrenat pe note date de Llama 3. | Forma modelului (Propunerea 4). Filtrarea datelor doar fără LLM străin. | Da, cu atribuire |
| MobileLLM (Meta) | github.com/facebookresearch/MobileLLM | **FAIR Noncommercial Research License** | La sub 1B parametri contează: SwiGLU, adâncime mare și lățime mică, intrarea și ieșirea comune, GQA. Varianta cu straturi repetate (LS) a câștigat: 125M de la 46,3 la 47,0 media pe 8 teste (README). | Propunerea 4 (doar idei) | **Doar idei** (licența nu permite cod comercial) |
| TinyLlama | github.com/jzhang38/TinyLlama | Apache-2.0 | 1,1B parametri pe 3T de simboluri. Viteza (24k simboluri/s pe A100, 56 % MFU) vine din kernel-uri contopite (flash-attn, fused layernorm, swiglu, cross-entropy). | Puțin. Nu are rețetă pentru 8 GB. | Da, cu atribuire |
| RWKV-LM | github.com/BlinkDL/RWKV-LM | Apache-2.0 | O rețea recurentă (RNN) fără atenție: memoria la inferență e constantă (fără cache KV). Are o demonstrație RNN de 380 de rânduri și una în numpy. Pentru modele mici: adânc și îngust, dropout mic. | Inferența în OS, pe termen lung | Da, cu atribuire |
| rStar / rStar2-Agent (Microsoft) | github.com/microsoft/rStar | MIT | Modele de 14B, RL cu unelte de cod. Verificatorul e **executabil** (rulează cod sau teste), nu un model. | Doar principiul verificatorului | Doar idei (scara nepotrivită) |
| STaR (lucrarea) | arxiv 2203.14465 (am citit-o prin ar5iv) | — (n-am găsit repo; clonarea a cerut autentificare) | Bucla: generează, păstrează doar ce iese corect, „raționalizează” cu răspunsul dat ca indiciu și **reantrenează de fiecare dată de la modelul inițial**. **Condiția: modelul trebuie să fie deja peste nivelul întâmplării; GPT-2 n-a reușit să pornească bucla nici la aritmetică.** | Propunerea 5 și înțelegerea lui E1 | Doar idei |
| kNN-LM (lucrarea) | iclr.cc/virtual/2020/poster/1815 | — | Perplexitatea pe Wikitext-103 coboară la 15,79, adică 2,9 puncte, **fără antrenare în plus** (rezumatul lucrării). | Memorie la nivel de cuvânt (idee pentru mai târziu) | Doar idei |
| Romanian-Transformers | github.com/dumitrescustefan/Romanian-Transformers | MIT (repo-ul; modelele au licențele lor) | Lista modelelor românești. RoGPT2-base (124M) are perplexitatea **52,34** pe testul wiki-ro (stride 512). Modelele dumitrescustefan cer ș/ț cu virgulă: cu sedilă (ş/ţ) devin cuvinte necunoscute. | Referință de evaluare și normalizare | Lista: da. Modelele: nu (LLM străin). |
| OpenLLM-Ro (RoLlama etc.) | huggingface.co/OpenLLM-Ro (pagina web) | Repo-ul de cod: Llama 2 Community License | Seturi de test românești: ro_arc_challenge, ro_mmlu, ro_winogrande, ro_hellaswag, ro_gsm8k, LaRoSeDa, WMT EN-RO, **XQuAD (EM/F1)**, STS, RoMT-Bench, RoCulturaBench. | Teste externe pentru Kronos | Doar seturile de date (fiecare cu licența lui) |
| FineWeb-2, partea `ron_Latn` | huggingface.co/datasets/HuggingFaceFW/fineweb-2 (pagina web) | **ODC-By 1.0** (pagina web) | Partea românească: **54.128.784 de documente, 81,30 GB**. | Mai multă română de calitate (Propunerea 4) | Date: da, cu atribuire |
| rost-73m-base | huggingface.co/rostlabs/rost-73m-base (pagina web) | CC-BY-NC-4.0 (pagina web) | Cineva a rulat nanochat pe 30 % română (FineWeb2-ro filtrat) și 70 % engleză, cu tokenizer bilingv de 32.768. Pagina nu are cifre de evaluare. | Doar dovada că rețeta nanochat a mai fost încercată pe română | Nu (NC; în plus, filtrul „edu” vine de la un LLM) |

---

## 2. Lecțiile

1. **Pierderile mici se confirmă statistic.** Speedrun-ul nu acceptă un record fără destule rulări pentru p < 0,01 față de prag. De exemplu, recordul „softcap 15” a avut 80 de rulări, cu deviație 0,0019 (`records/track_1_short/2025-01-04_SoftCap/README.md`). Pentru Kronos: un câștig de val_bpb sub ~2× zgomotul (`prag_zgomot = 0,005`) nu înseamnă nimic fără repetări. **[CITIT]**

2. **Ordinea câștigurilor din speedrun (45 → ~1,7 min):** lr reglat + rotary (45 → 31,4 min), **Muon** (→ 24,9), apoi ReLU² + QK-norm + proiecții pornite de la zero (→ 15,2). Au urmat intrarea separată de ieșire, legăturile directe de la intrare la fiecare strat, softcap pe logits, U-net, atenție pe ferestre și „value embeddings” (tabelul din `README.md`). Multe altele sunt doar de viteză pe H100 (FP8, FlashAttention-3, CUDA graphs) și nu ne folosesc. **[CITIT]**

3. **Muon câștigă ~1,5× la pași, dar autorii avertizează la loturi mici.** Pe pista de optimizare, Muon atinge pierderea 3,28 în 3.500–3.600 de pași, AdamW în 5.625 (`records/track_3_optimization/README.md`). Codul vechi spune: *„We believe it is unlikely to work well for training with small batch size”* (`records/track_1_short/2024-12-04_ValueEmbed/train_gpt2.py`, r. 71). Kronos are doar 6.144 de simboluri pe pas, față de 524.288 în speedrun, adică de 85× mai puțin. **[CITIT]** Probabil va trebui adunat gradientul pe mai multe loturi înainte de fiecare pas Muon. **[DEDUCȚIE]**

4. **Cum se folosește Muon corect:** doar pe matricile din straturi. Intrarea, ieșirea și scalarii merg pe AdamW, cu rate diferite (în `train_gpt_simple.py`: intrare lr 0,7, ieșire 0,004, scalari 0,015, Adam betas 0,8/0,95; Muon lr 0,025, wd 0,05). Newton-Schulz rulează în bf16. Muon ține un singur buffer de momentum (Adam ține două), deci **folosește mai puțină memorie** (README Muon). **[CITIT]**

5. **Răcirea (cooldown) lungă e câștig ieftin.** Speedrun-ul și nanochat scad rata pe 45–70 % din antrenare (`cooldown_frac=0.7` în antrenorul simplu; `--warmdown-ratio 0.65` în `scripts/base_train.py`; record #26: „increase cooldown frac to .45”). SmolLM folosește WSD, cu scădere pe ultimii 20 %. **[CITIT]** Kronos răcește 30 de minute din 10 ore, adică 5 %. Merită testat 20–40 %. **[DEDUCȚIE]**

6. **Arhitectura „modernă” la scară mică** (nanochat `gpt.py`; antrenorul simplu din speedrun): rotary în loc de poziții învățate, RMSNorm, QK-norm (normalizare pe q și k înainte de atenție), ReLU² în loc de GELU, proiecțiile de ieșire pornite de la zero, fără bias și logits limitate cu softcap (`15 * x / sqrt(x² + 15²)`). **[CITIT]** Kronos are încă poziții învățate, LayerNorm și GELU, deci toate acestea îi lipsesc. **[CITIT în model_gpt.py]**

7. **Forma modelului mic: adânc și subțire.** SmolLM-135M și MobileLLM-125M folosesc exact aceeași formă: 30 de straturi × 576, 9 capete, 3 capete KV (`config_smollm2_135M.yaml`, `configs/125M/config.json`). Kronos are 12 × 768. **[CITIT]** MobileLLM-LS repetă fiecare strat de două ori, fără parametri în plus, și câștigă +0,7 puncte la 125M (README). **[CITIT]**

8. **„Tabele de memorie” ieftine în model.** Bigram-hash embedding: un tabel indexat după perechea (simbolul anterior, simbolul curent), pornit de la zero și adunat în fiecare strat cu un coeficient învățat. A scurtat recordul cu 5,1 s, cu 165 de pași mai puțin. Adunarea directă a mers mai bine decât variantele cu porți (`records/track_1_short/2026-01-19_BigramHashEmbedding/README.md`). **[CITIT]** Pentru română, cu terminații lungi, poate ajuta mai mult decât în engleză. **[DEDUCȚIE]**

9. **Un tokenizer mai bun e câștig „gratuit” de parametri.** Un tokenizer cu vocabular aproape înjumătățit, care păstra aceiași octeți pe simbol, a dat un record neoficial de 2,77 min (README speedrun, „Notable runs”). În llama2.c, un tokenizer de 4.096 adaptat textului comprimă cât unul de 32.000 (README, „custom tokenizers”). **[CITIT]** Kronos are deja tokenizer propriu de 16.384. Merită măsurat câți octeți are în medie un simbol, separat pe română și pe engleză. **[DEDUCȚIE]**

10. **Biți pe octet e măsura corectă.** nanochat `loss_eval.py` împarte suma pierderilor la suma octeților și nu numără simbolurile speciale. Examenul Kronos (`module/examen_bpb.py`) face deja asta. **[CITIT]** Ca să comparăm cu RoGPT2 (perplexitatea 52,34 pe simbol), cifra trebuie convertită în biți pe octet pe același text. Altfel comparația e greșită. **[DEDUCȚIE]**

11. **La căutare, extinderea documentelor bate extinderea întrebării.** Pe MS MARCO dev: BM25 0,1840 MRR@10. BM25+RM3 (întrebarea extinsă automat): 0,1566, mai rău, deși recall@1000 urcă 0,8526 → 0,8606. BM25 cu doc2query (la fiecare pasaj se adaugă întrebările prezise de un model): **0,2723** (`docs/2cr/msmarco-v1-passage.html`). **[CITIT]** În lucrare, doc2query a folosit T5 antrenat supervizat. **[MEMORIE]** Noi ar trebui să folosim modelul nostru.

12. **Fuziunea mai multor căutări** se face simplu, cu RRF: scor = Σ 1/(60 + loc) (`pyserini/fusion/_base.py`). E robustă și nu cere ponderi reglate. **[CITIT]**

13. **Româna are nevoie de normalizare la căutare.** ș/ț cu virgulă vs ş/ţ cu sedilă: Kronos o face deja. **[CITIT]** Rădăcinile cuvintelor nu sunt tratate deloc. bm25s nu are listă românească de cuvinte de legătură. **[CITIT]** Snowball are un algoritm public de stemming pentru română, licență BSD. **[MEMORIE]**

14. **Auto-îmbunătățirea pornește doar peste nivelul întâmplării.** STaR, la GPT-J 6B: CommonsenseQA 36,6 % → 72,5 %. Totuși, *„GPT-2 could not bootstrap … even on arithmetic”*. La fiecare iterație se reantrenează **de la modelul inițial**, ca să evite supra-învățarea (lucrarea, prin ar5iv). **[CITIT]** La ~100M, bucla trebuie restrânsă la sarcini unde Kronos e deja peste întâmplare, de exemplu „răspuns din text” (S12: 50/50 pe ce știa). Asta explică probabil și rezultatul NECLAR al lui E1. **[DEDUCȚIE]**

15. **Verificatorul bun e executabil, nu un model.** rStar2 folosește un „judecător de cod” care rulează testele. nanochat RL folosește `train_task.reward(...)`, adică verificarea exactă a răspunsului GSM8K, și avantajul = recompensa − media, fără KL și fără PPO (`scripts/chat_rl.py`, r. 1–15, 141–144). **[CITIT]** Pentru Kronos, verificatorul executabil natural e „răspunsul se găsește în bucata găsită și trece verificatorul de text propriu”. **[DEDUCȚIE]**

16. **Inferența fără dependențe e realistă.** `run.c` are nevoie doar de malloc, mmap și funcții math (`#include`-urile din `run.c`). **[CITIT]** Kronos are poziții învățate, deci nu-i trebuie sin/cos pentru RoPE, doar exp, sqrt și tanh (sau erf) pentru GELU. **[DEDUCȚIE, din model_gpt.py]** Mărimea pentru 98M: fp32 ~392 MB, Q8_0 ~104 MB (98M × 34/32 octeți), Q4_0 ~55 MB. **[CALCUL, după ggml-common.h]**

17. **Testarea unei implementări noi: starea de control.** llm.c compară logits și pierderea cu PyTorch, apoi 10 pași de antrenare (README, r. 105). **[CITIT]** Pentru motorul Rust al OS-ului: fișier de control scris din Python și comparație cu toleranță la fiecare strat. **[DEDUCȚIE]**

18. **RWKV ține memoria constantă la inferență.** Formula stării pentru 7B e L·(2D + 64D) (README, r. 25). Starea trebuie ținută în fp32 (README, r. 261). **[CITIT]** E atractiv pentru un OS cu memorie fixă, dar ar cere un model nou de la zero. **[DEDUCȚIE]**

19. **Date românești deschise.** FineWeb-2 ron_Latn are 54,1 M documente, 81,30 GB, ODC-By 1.0. **[CITIT, pagina web]** Kronos are acum ~1,66 GB de română în amestec (33,9 % din 4,89 GB). **[CALCUL]** Pentru teste externe: XQuAD (are română, întrebări cu răspuns extras din text) și Belebele `ron_Latn` (înțelegere cu variante). **[MEMORIE: XQuAD ~1.190 de perechi, CC BY-SA 4.0; Belebele 900 de întrebări, CC BY-SA 4.0. De verificat licența exactă înainte de folosire.]**

---

## 3. Propunerile (ordonate după câștig / cost)

Toate respectă regulile: niciun LLM străin, cod scris de noi (inspirat, cu atribuire unde copiem idei din cod MIT/Apache), fiecare piesă ca **modul nou** cu MANIFEST și teste de contract, pre-înregistrare cu prag și **reversibil** (#415 și linia w2 rămân neatinse).

### Propunerea 1: Muon + răcire lungă, pe continuarea lui #415 (cel mai bun raport câștig/cost)

- **Ce e:** un modul optimizator nou (`module/optimizator_muon.py`, port „optimizator” sau setare a modelului, după cum permite contractul). Muon (Newton-Schulz în bf16, momentum 0,95 Nesterov) pe matricile din straturi, AdamW pe intrare, ieșire, LayerNorm și bias. Gradientul se adună pe **8 loturi** (~49k simboluri pe pas Muon), din cauza avertismentului despre loturile mici. Răcirea finală crește de la 5 % la ~25 % din antrenare.
- **De ce ar fi mai bun:** ~1,5× mai puțini pași pentru aceeași pierdere pe pista de optimizare (lecția 3) și mai puțină memorie decât Adam. Răcirea lungă e câștigul cel mai sigur din toate rețetele citite (lecția 5). Nu schimbă arhitectura, deci pornește direct din #415.
- **Cost:** ~5–6 ore pe placă. A = AdamW ca acum, 2 h din #415. B = Muon, 2 h din #415. Fiecare cu 30 min de răcire, pe aceleași date și cu aceeași sămânță. Plus ~2 h de cod și teste pe procesor.
- **Primul pas mic, testabil:** pe procesor, un test unitar: Muon pe un MLP mic scade pierderea, iar matricea de update are valorile singulare în ~[0,6; 1,2]. Apoi o probă de 10 minute pe placă, care să arate că memoria rămâne sub 7.000 MB.
- **Cum se măsoară (de pre-înregistrat):** val_bpb pe validarea românească și pe TinyStories R2, plus examenele obișnuite (fapte, cod). **Confirmat** dacă B ≤ A − 0,010 la română (2× pragul de zgomot) **și** nicio regresie > 0,005 pe celelalte. **Infirmat** dacă B ≥ A. Între ele: neclar, se repetă cu altă sămânță.
- **Riscuri:** la lot mic, Muon poate să nu ajute (avertismentul autorilor). Trecerea de la AdamW la Muon la mijlocul antrenării poate da un „șoc” la început (momentumul pornește de la zero). Ratele din speedrun sunt pentru alt model, deci trebuie probat lr 0,01 / 0,02.

### Propunerea 2: memoria E3 mai bună, fără LLM: rădăcini românești + reordonare cu modelul propriu + RRF

- **Ce e:** trei piese mici, fiecare măsurată separat:
  - (a) **un stemmer românesc propriu**, după descrierea publică a algoritmului Snowball pentru română, ca a doua coloană în index. Căutarea se face pe ambele coloane și se unește cu **RRF** (k = 60).
  - (b) **reordonare prin „probabilitatea întrebării”**: pentru primele 20 de bucăți găsite de BM25, #415 calculează log p(întrebare | bucată), iar bucățile se reordonează după scor. Modelul nostru devine astfel judecător de relevanță, fără niciun model străin. **[Ideea „UPR”, Sachan et al. 2022: MEMORIE.]**
  - (c) mai târziu, **doc2query propriu**: Kronos generează offline 2–3 întrebări pentru fiecare bucată și le adaugă la index (lecția 11).
- **De ce ar fi mai bun:** azi răspunsul e în primele 3 bucăți la 72 % și în primele 5 la 80 %. Diferența de 8 puncte între k = 3 și k = 5 arată că **ordinea** e problema, adică exact ce repară (b). Pyserini arată că extinderea documentelor bate extinderea întrebării (+48 % MRR@10 relativ). Toate sunt reversibile: indexul vechi rămâne.
- **Cost:** (a) ~0 ore pe placă, câteva ore pe procesor. (b) 20 de evaluări × 100 de întrebări, adică câteva minute pe placă. (c) generarea pentru ~1–2 M de bucăți ar cere multe ore (de estimat după o probă pe 1.000 de bucăți), de aceea vine ultima.
- **Primul pas mic:** (b) pe setul de **validare** existent (500 + 500 de întrebări): bune la k = 3 înainte și după reordonare. Fără model nou, fără antrenare.
- **Cum se măsoară:** pe un **set nou, neatins** (alt seed, ca la S26). Pragul (de scris înainte): k = 3 urcă **≥ 5 puncte** față de BM25 simplu, iar k = 20 nu scade (reordonarea nu poate pierde ce n-a găsit). Opțional, XQuAD-ro ca test extern, dacă licența se confirmă.
- **Riscuri:** #415 poate fi prea slab ca judecător, iar scorul poate favoriza bucățile scurte. Se normalizează pe simbol și se compară ambele variante pe validare. Stemmerul poate amesteca înțelesuri. De aceea e coloană separată, unită prin RRF, nu înlocuire.

### Propunerea 3: un motor de inferență de referință, fără PyTorch, pregătit pentru Cyber Universe

- **Ce e:** un modul `module/inferenta_bruta.py`, în Python pur sau numpy, care citește un fișier binar propriu (antet cu chei-valori, ca ideea GGUF, little-endian, aliniere 32) și face forward-ul lui #415 strat cu strat. Variante fp32 și **Q8_0** (blocuri de 32, o scară). Exportul îl face o unealtă separată. Fișierul e apoi contractul pentru motorul Rust no_std din OS.
- **De ce ar fi mai bun:** desparte „ce face modelul” de PyTorch și dă OS-ului o țintă exactă, testată. Q8_0 reduce fișierul de la ~392 MB la ~104 MB (lecția 16), iar llama2.c raportează ~3× viteză pe procesor la int8 (lecția din tabel).
- **Cost:** 0 ore pe placă. ~1–2 zile de lucru pe procesor.
- **Primul pas mic:** starea de control (lecția 17). PyTorch scrie logits pentru 3 texte fixe. Motorul trebuie să le reproducă: diferență maximă < 1e-4 la fp32, iar la Q8_0 val_bpb nu crește cu mai mult de 0,005.
- **Cum se măsoară:** teste automate (identitatea logits-urilor) + val_bpb Q8_0 vs fp32 + simboluri/s pe laptopul fără GPU.
- **Riscuri:** `nn.MultiheadAttention` are o ordine proprie a greutăților (in_proj combinat), ușor de greșit. Testul strat cu strat prinde asta. Q8_0 pe activări poate pierde mai mult decât pe greutăți, deci se începe doar cu greutăți Q8_0.

### Propunerea 4: o linie nouă „w3” de la zero: arhitectură modernă + mai multă română

- **Ce e:** o rețea nouă (`module/model_gpt_v2.py`, alături de cel vechi): rotary, RMSNorm, QK-norm, ReLU², proiecții pornite de la zero, softcap 15, fără bias, Muon. Forma e adâncă și subțire (de probat: 24–30 de straturi × 576–640, ~aceiași 98M), cu bigram-hash embedding (lecția 8). Datele au mai multă română din FineWeb-2 (ODC-By), filtrată **fără LLM**: un clasificator mic propriu care învață „seamănă cu Wikipedia românească” vs „pagină web oarecare”. **[Ideea filtrului „ca referința” e din GPT-3: MEMORIE.]**
- **De ce ar fi mai bun:** toate trucurile din lecțiile 2, 6, 7 și 8 sunt validate statistic la ~124M, adică exact scara Kronos. Româna e 33,9 % din date, iar sursa deschisă e de ~50× mai mare.
- **Cost:** mare. Pregătirea datelor pe procesor (~1 zi) + o noapte de 10 h pe placă. Comparația se face cu curba w2 din jurnal **la același număr de simboluri** (nu e nevoie de o noapte în plus pentru w2).
- **Primul pas mic:** o probă de 30 de minute „w3-mic” (nanochat folosește `--depth=12` pentru astfel de probe): pierderea scade normal, memoria e < 7.000 MB, iar val_bpb la 30 min e comparat cu w2 la 30 min (din jurnal).
- **Cum se măsoară:** val_bpb română și TinyStories R2 la 1, 3 și 10 ore. **Confirmat** dacă w3 atinge val_bpb-ul lui w2 de după 10 h în ≤ 6 h. Altfel w2 rămâne linia principală.
- **Riscuri:** pierde tot ce s-a învățat pe w2 (conversație, „răspuns din text”), care trebuie refăcut. Multe schimbări deodată: dacă iese mai prost, nu știm din ce cauză. De aceea proba de 30 min se poate face și pe bucăți (doar arhitectură, apoi și Muon). Adâncimea mare încetinește pasul.

### Propunerea 5: auto-joc restrâns la „răspuns din text”, cu verificator executabil (după rezultatul S27)

- **Ce e:** o buclă STaR adaptată (lecțiile 14 și 15). (1) Din Wikipedia ro se aleg bucăți. Întrebările vin din reguli (șabloane pe propoziții cu nume sau numere, fără model) sau din generatorul E1. (2) Kronos răspunde folosind primele 3 bucăți găsite. (3) **Verificatorul executabil** păstrează doar răspunsurile care apar în bucată și trec verificatorul propriu de text (97,6 % acord). (4) Se reantrenează **de la #415 de fiecare dată**, nu în lanț. Opțional, apoi: REINFORCE cu media ca bază, ca în nanochat.
- **De ce ar fi mai bun:** e singura formă de auto-îmbunătățire care are șanse la ~100M. Sarcina e deja peste întâmplare (S12: 50/50 pe ce știa), iar verificarea nu cere niciun model.
- **Cost:** generarea + verificarea pentru ~5.000 de întrebări (≤ 1 h pe placă) + 2–3 h de antrenare pe iterație. 2 iterații = ~8 h.
- **Primul pas mic:** pe procesor, generatorul de întrebări din reguli + verificatorul pe 200 de exemple, cu răspunsul corect pus de noi. Verificatorul trebuie să accepte ≥ 95 % din ele și să respingă ≥ 95 % din răspunsurile greșite construite.
- **Cum se măsoară:** pe un examen nou de „răspuns din text” (alt seed). **Confirmat** dacă iterația 1 urcă ≥ 5 puncte față de S27 fără regresie > 0,005 val_bpb. **Infirmat** dacă iterația 1 nu urcă cu nimic.
- **Riscuri:** modelul poate învăța să copieze bucăți lungi, care „trec” verificatorul fără să răspundă. Trebuie o limită de lungime și verificarea tipului de răspuns (număr, nume). Întrebările din șabloane pot fi prea ușoare față de cele reale.

---

## 4. Ce NU merită (acum) și de ce

- **FP8, FlashAttention-3, CUDA graphs, kernel-urile Triton din speedrun:** sunt făcute pentru H100. RTX 3070 Ti (Ampere) nu are FP8, iar FA3 e doar pentru Hopper. **[MEMORIE, sigur în mare]** Câștigul lor e de viteză, nu de calitate.
- **Trucurile foarte noi și complicate din speedrun** (multi-token prediction, sampled softmax, ANVIL, MUDD, paired heads etc.): câștigurile sunt de ordinul secundelor dintr-o rulare de ~100 s pe 8 GPU-uri. Codul e greu de întreținut. Propunerile 1 și 4 iau doar trucurile vechi, mari și simple.
- **ColBERT / SPLADE / encodere dense:** câștigul lor vine din antrenare supervizată pe MS MARCO, cu modele BERT. Pentru română nu avem date de antrenare de relevanță, iar BERT-urile românești existente sunt modele străine. Propunerea 2 (reordonare cu modelul propriu) dă o parte din câștig fără ele.
- **Filtrul FineWeb-Edu așa cum e:** notele de antrenare vin de la Llama 3, deci ar încălca regula „fără LLM străin” (`text/data/fineweb-edu/README.md`). La fel rost-73m, care folosește FineWeb2-ro filtrat „edu ≥ 3”.
- **Codul MobileLLM:** licența FAIR e necomercială. Folosim doar ideile (adâncime, straturi repetate).
- **rStar / rStar2-Agent, RL în stil DeepSeek:** sunt la 1,5–14B. La 100M, STaR spune clar că bucla nu pornește dacă modelul nu e deja competent (lecția 14).
- **RWKV sau Mamba ca înlocuitor acum:** ar cere o linie nouă de la zero, iar avantajul lor (context lung, memorie constantă) nu contează la context 512. RWKV rămâne o idee bună pentru motorul din OS, mai târziu.
- **ggml / llama.cpp întregi în OS:** sunt prea mari și cu prea multe dependențe pentru no_std. Luăm doar ideea Q8_0 și antetul cu chei-valori.
- **Modelele românești existente** (RoGPT2, RoLlama, BERT-urile ro): ca profesor sau judecător ar încălca regula. Rămân utile doar **seturile lor de test** (XQuAD, LaRoSeDa, STS etc.) și cifra de referință RoGPT2 (52,34 perplexitate), convertită corect în biți pe octet.
- **TinyStories ca sursă de date nouă:** TinyStories a fost generat cu GPT-3.5/GPT-4. **[MEMORIE]** Kronos îl folosește deja (inclusiv validarea R2 a examenului oficial). Nu e un model în buclă, deci probabil nu încalcă litera regulii din 22 oct, dar **e o decizie pentru Adrian** dacă vrea și datele „curate” de LLM străin.
- **OpenLLM-Ro llama-recipes:** cod pentru ajustarea modelelor Llama (licența Llama 2) și declarat învechit chiar în README.

---

## Surse citite efectiv (fișiere)

- modded-nanogpt: `README.md`; `records/track_3_optimization/README.md` și `train_gpt_simple.py`; `records/track_1_short/2025-01-04_SoftCap/README.md`, `2024-12-04_ValueEmbed/train_gpt2.py`, `2026-01-19_BigramHashEmbedding/README.md`; `train_gpt.py` (doar căutare).
- Muon: `README.md`. nanochat: `README.md`, `nanochat/gpt.py` (antet), `nanochat/loss_eval.py`, `scripts/base_train.py` (setările), `scripts/chat_rl.py`.
- llama2.c: `README.md` (int8, modele, tokenizer), `run.c` / `runq.c` (căutare). llm.c: `README.md`. ggml: `src/ggml-common.h`, `docs/gguf.md`.
- bm25s: `README.md`, `bm25s/stopwords.py`, `bm25s/scoring.py`. Pyserini: `docs/conceptual-framework.md`, `docs/experiments-rm3-rocchio-python.md`, `docs/2cr/msmarco-v1-passage.html`, `pyserini/fusion/_base.py`.
- SmolLM: `README.md`, `text/data/fineweb-edu/README.md`, `train_edu_bert.py`, `text/pretraining/README.md`, `smollm1|2/config_*_135M.yaml`. MobileLLM: `README.md`, `configs/125M/config.json`, `utils/modeling_llama.py` (layer_sharing), `LICENSE`. TinyLlama: `README.md`. RWKV-LM: `README.md`, lista din `RWKV-v7/`. rStar: `README.md`. Romanian-Transformers: `README.md`.
- Pagini web: STaR (ar5iv 2203.14465), kNN-LM (pagina ICLR 2020), FineWeb-2 README, OpenLLM-Ro RoLlama3.1-8b-Instruct-DPO, rostlabs/rost-73m-base.
- Kronos (doar citit): `config/ws_w2.toml`, `module/model_gpt.py`, `module/examen_bpb.py`, `unelte/e3_memorie.py` (antet), `docs/rapoarte/2026-10-21_2235_S12_noaptea12.md`, `docs/rapoarte/2026-10-23_2335_S25_E3_cautare.md`.
