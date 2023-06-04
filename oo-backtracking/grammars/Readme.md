# Polimondu virkņu ģenerēšana ar gramatikām

Aplūkosim polimondu virkni malu skaitam $m=11, 15, 19, \ldots$:

![Bilde](docs/inductive_sequences/SEQUENCE_4_3_A.svg)

Pierakstīsim šos polimondus ar virzienu vektoriem (šoreiz lietojam mazos burtus, 
lai tie būtu neterminālie simboli). 

``` plain
A CB D FE D FE A C
A CBC D FEF D FEF A CB
A CBCB D FEFE D FEFE A CBC
A CBCBC D FEFEF D FEFEF A CBCB
```

Aprakstīsim šo virkni ar [kontekstjūtīgu gramatiku](https://en.wikipedia.org/wiki/Context-sensitive_grammar). 

* S → aXTY
* S → aXDY
* T → XTY
* T → XDY
  
* HG → HK
* HK → LK
* LK → LH
* LH → GH
  
* JI → JM
* JM → NM
* NM → NJ
* NJ → IJ
  
* GH → JDH
* IJ → IAJ

* aG → ac
* cG → cb
* bG → bc
* cD → cbd
* bD → bcd

* dH → df
* dH → fe
* eH → ef
* eD → efd
* fD → fed

* dI → df
* fI → fe
* eI → ef
* eA → efa
* fA → fea 

* aJ → ac
* cJ → cb
* bJ → bc

Šo gramatiku var izmantot sekojošam izvedumam (piemērs polimondam $n=19$)

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




