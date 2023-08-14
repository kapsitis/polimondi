# polimondi

<a href="https://kapsitis.github.io/polimondi/">SVG attēli par polimondiem (GitHub Pages)</a>

## Faktu apkopojums

Polimondiem ar nelieliem malu garumiem apkopojam pamatinformāciju: 

**Skaits:** 
  Cik perfekto polimondu ir dažādiem malu garumiem? (Polimondus, kuri 
  atšķiras tikai ar rotācijām vai spoguļattēliem, uzskatām par vienādiem.)
**Max laukums:** 
  Starp visiem perfektajiem polimondiem atrasts lielākais iespējamais laukums izteikts
  mazo trijstūrīšu laukuma vienībās.


| $n$      | Skaits  | Laukums         | Šaurie leņķi
| -------- | ------- | --------------- | -------------
| 5        | 1       | [19,19]         | [3,3]
| 7        | 2       | [92,96]         | [3,3]
| 9        | 3       | [99,111]        | [3,9]
| 11       | 21      | [148,518]       | [1,7]
| 13       | 228     | [281,1029]      | [1,11]
| 15       | 1335    | [360,1568]      | [3,13]
| 17       | 8599    | [495,2775]      | [1,15]
| 19       | 67068   | [664,4406]      | [1,17]
| 21       | 526694  | [863,6429]      | [1,19]
| 23       | 4284617 | [1084,9318]     | [1,21]


## Vārdnīcas izmēri

Vārdnīcu veido oo-backgracking/NSturis_dictionary_creator.py - tajā glabājas 
visas vienkāršās (sevi nekrustojošās) lauztās līnijas, kuras sākas trijstūra režģu koordinātu sākumpunktā, 
visi to posmi iet pa trijstūra režģu līnijām un ir augošā garumā - $1,2,\ldots,m$. 
Šajā tabulā apkopojam to, cik dažādas lauztas līnijas var izveidot no $n$ posmiem. 
Vārdnīcā glabājas lauztās līnijas posmu virzieni un galapunkts, kurā tā nonākusi. 

Šī vārdnīca var būt noderīga, jo tajā kā "kešatmiņā" glabājas visi veidi, kā var pabeigt 
perfekto polimondu (uzzīmēt tā asti jeb pēdējos $m$ posmus) - atliek vien uzzīmēt pirmos $n-m$ posmus, 
tad apskatīties vārdnīcā 
visas lauztās līnijas, kuras atgriežas koordinātu sākumpunktā no tās vietas, kurā esam nonākuši. 
Un zīmēt vārdnīcā esošās "astes" no otra gala (ar posmu garumiem $m,\ldots,1$). 
Dažos gadījumos tas ļauj paātrināt polimondu pārlases algoritma ātrumu.

| $m$      | Skaits  | 
| -------- | ------- | 
| 1        | 4       | 
| 2        | 16      | 
| 3        | 64      | 
| 4        | 248     | 
| 5        | 936     | 
| 6        | 3456    | 
| 7        | 12424   | 
| 8        | 44472   | 


## Perfektie polimondu eži

Ir tādi perfekti polimondi, kuri sastāv tikai no šauriem leņķiem (60 vai 300 grādi - atkarībā no tā,
vai lauztā līnija ir izliekta uz iekšu vai uz āru). Tos ģenerē programma: 

```
python NSturis_magiskie_ezhi.py 9
python NSturis_magiskie_ezhi.py 27
python NSturis_magiskie_ezhi.py 29
```

Eksistē viens šāds 9-polimonds, pieci 27-polimondi un trīs 29-polimondi. Pavisam tātad ir zināmi deviņi polimondu eži. 
To virzienus (no garākās malas līdz īsākajai) apraksta šādi saraksti: 

```
['A', 'C', 'E', 'C', 'E', 'A', 'E', 'A', 'C'],
['A', 'C', 'A', 'C', 'E', 'C', 'E', 'C', 'E', 'A', 'E', 'C', 'E', 'A', 'E', 'A', 'C', 'A', 'E', 'A', 'C', 'A', 'E', 'A', 'E', 'A', 'E'], 
['A', 'C', 'A', 'C', 'E', 'C', 'E', 'C', 'E', 'A', 'E', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'C', 'A', 'E', 'A', 'C', 'A', 'C', 'A', 'C'],
['A', 'C', 'A', 'E', 'A', 'E', 'A', 'E', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'E', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'A', 'C'],
['A', 'C', 'A', 'E', 'A', 'E', 'A', 'E', 'C', 'E', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'E', 'C', 'A', 'C', 'A', 'C'],
['A', 'C', 'A', 'E', 'A', 'E', 'A', 'E', 'C', 'E', 'C', 'E', 'C', 'E', 'C', 'E', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C', 'A', 'C'],
['A', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'E', 'A', 'E', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'C']
['A', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'E', 'C', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'A', 'E', 'C', 'E', 'A', 'E', 'A', 'C']
['A', 'C', 'E', 'C', 'E', 'C', 'E', 'A', 'E', 'A', 'C', 'A', 'E', 'A', 'E', 'A', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'E', 'C', 'A', 'C', 'A', 'E']
```

Šie polimondi ir viegli pazīstami, jo tie izmanto tikai trīs (no sešiem) virzieniem trijstūru režģī - ir uzrakstāmi 
tikai ar burtiem "A", "C" un "E". 
Tie vēl nav uzzīmēti (tkinters programma tos skaidri nenodalīja), bet tos var izteikt dīvainajās Dekarta koordinātēs. 
Lai iegūtu šīs koordinātes, var ierakstīt NSturis.py programmas 111.rindiņā citu noklusēto vērtību: 
format='dekarta'. 


**Hipotēze:** Neeksistē tādi perfekti polimondi ar nepāra malu skaitu, 
kuros ir tieši viens plats leņķis (120 vai 240 grādi). 



## Maģisko polimondu neiespējamās permutācijas

Permutācijas pierakstām sākot ar elementu $1$. Otrajā pozīcijā rakstām skaitļa $1$ mazāko kaimiņu.
Tādējādi var analizēt permutācijas bez gadījumu atkārtošanās -- ievērojot rotācijas simetriju (un arī iespēju 
maģisko polimondu apstaigāt abos virzienos). 





