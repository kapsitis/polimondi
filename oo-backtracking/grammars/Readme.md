# Polimondu virkņu ģenerēšana ar gramatikām

Šajā sadaļā aplūkojam kā bezgalīgas perfektu-maģisku polimondu virknes (malu virzienu kodējumā) var konstruēt 


Aplūkosim polimondu virkni malu skaitam $m=11, 15, 19, \ldots$:

![Bilde](https://kapsitis.github.io/polimondi/inductive_sequences/SEQUENCE_4_3_A.svg)

Pierakstīsim šos polimondus ar virzienu vektoriem (šoreiz lietojam mazos burtus, 
lai tie būtu neterminālie simboli). Kodējumā sāk ar visgarāko malu garumā $n$, pēc tam malu garumu pa vienai 
vienībai samazina līdz $1$.

``` plain
a cb d fe d fe a c
a cbc d fef d fef a cb
a cbcb d fefe d fefe a cbc
a cbcbc d fefef d fefef a cbcb
```

Aprakstīsim šo virkni ar [kontekstjūtīgu gramatiku](https://en.wikipedia.org/wiki/Context-sensitive_grammar). 

Uzģenerē garu virknīti "aXXXDYYY"

* S → aXTY
* S → aXDY
* T → XTY
* T → XDY

Pārvērš virknīti par "a GHGHGH D IJIJIJ"

* X → GH
* Y → IJ

Gramatikas produkcijas, lai mainītu vietām burtus "GH" un "IJ" (ja tie nepareizā secībā)
  
* HG → HK
* HK → LK
* LK → LH
* LH → GH
  
* JI → JM
* JM → NM
* NM → NJ
* NJ → IJ

Uz robežas starp "GH" ievieto jaunu netermināli "D", bet starp "IJ" ievieto netermināli "A". 
Ja to izdara par ātru (iekams visi "G" sašķiroti pirms "H" un visi "I" - pirms "J", 
nav iespējams atbrīvoties no neterminālajiem simboliem). 
  
* GH → JDH
* IJ → IAJ

Burts pašā vārda sākumā ("a") "apēd" visus "G" un pārtaisa tos par virknīti "cbcb...".
Tad, kad "G" netermināļi beidzas un nāk "D", iesprauž vēl vienu papildu burtu ("c" vai "b" - 
atkarībā no paritātes). Neterminālis "D" pārvēršas par termināli "d". 

* aG → ac
* cG → cb
* bG → bc
* cD → cbd
* bD → bcd

"Apēd" visus "H" un pārtaisa tos par virknīti "fefe...". Pirms beigu "D"  iesprauž 
vienu papildu burtu ("f" vai "e"). Neterminālis "D" pārvēršas par termināli "d".

* dH → df
* dH → fe
* eH → ef
* eD → efd
* fD → fed

"Apēd" visus "I" un pārtaisa tos par virknīti "fefe...". Pirms beigu "A"  iesprauž 
vienu papildu burtu ("f" vai "e"). Neterminālis "A" pārvēršas par termināli "a".

* dI → df
* fI → fe
* eI → ef
* eA → efa
* fA → fea 

"Apēd" visus "J" un pārtaisa tos par virknīti "cbc...". Šoreiz papildu burtu 
neiesprauž, jo pēdējā virknīte mums vajadzīgajā polimonda kodējumā ir par 1 īsāka nekā cita.

* aJ → ac
* cJ → cb
* bJ → bc

Pilns izvedums ar šo gramatiku polimondam $n=19$:

``` plain
S →
aXTY →
aXXTYY → 
aXXXDYYY →
aGHXXDYYY →
aGHGHXDYYY →
aGHGHGHDYYY →
aGHGHGHDIJYY →
aGHGHGHDIJIJY →
aGHGHGHDIJIJIJ →
...
aGGGHHHDIIIJJJ →
aGGGDHHHDIIIJJJ →
aGGGDHHHDIIIAJJJ →
acGGDHHHDIIIAJJJ →
acbGDHHHDIIIAJJJ →
acbcDHHHDIIIAJJJ →
acbcbdHHHDIIIAJJJ →
acbcbdfHHDIIIAJJJ →
acbcbdfeHDIIIAJJJ →
acbcbdfefDIIIAJJJ →
acbcbdfefedIIIAJJJ →
acbcbdfefedfIIAJJJ →
acbcbdfefedfeIAJJJ →
acbcbdfefedfefAJJJ →
acbcbdfefedfefeaJJJ →
acbcbdfefedfefeacJJ →
acbcbdfefedfefeacbJ →
acbcbdfefedfefeacbc
```

**Hipotēze:** Nav iespējams ģenerēt bezgalīgu perfekti-maģisku polimondu virkni, izmantojot 
[bezkonteksta gramatikas](https://en.wikipedia.org/wiki/Context-free_grammar).


