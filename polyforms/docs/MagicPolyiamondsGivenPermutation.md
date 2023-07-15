# Maģiskie polimondi dotajai malu garumu permutācijai

Mūsu mērķi: 

* Nelielām $n$ vērtībām uzskaitām  $[1,2,\ldots,n]$ permutācijas. 
  Atmetam simetriskos gadījumus pret rotācijām un inversiju - t.i. pieņemot, ka permutācija sākas ar $1$ un 
  otrais skaitlis ir mazākais no skaitļa $1$ kaimiņiem.
  Katrai no šīm permutācijām uzrakstām, cik maģiskus polimondus ar to var izveidot.
* Izsakām hipotēzi par mazāko $n$, sākot ar kuru katrai permutācijai 
  atbilst vismaz viens maģiskais $n$-stūris, kuram visas malas ir uz trīsstūru režģa. 
* Maziem $n$ izveidojam nederīgo permutāciju sarakstu (kuriem šāds maģiskais $n$-stūris neeksistē). 
* Maziem $n$ atrodam permutācijas-rekordistes, t. i.  tās permutācijas, kurām atbilst visvairāk maģisko $n$-stūru.
* Izsakām hipotēzes par to, kā šīs permutācijas varētu vispārināt. 
* Duālais uzdevums - dota virknīte ar malu virzieniem, atrast permutācijas, kuras var ievietot 
  šajos malu virzienos.


Prasības programmatūras produktam: 

* Atrast visas permutācijas skaitļiem $1, \ldots, n$. 
* Dotajai permutācijai ar "backtracking" atrast/saskaitīt visus maģiskos $n$-stūrus. 
* Dotajam permutācijas prefiksam (pirmajiem locekļiem), atrast visus iespējamos permutācijas turpinājumus 
  (vai permutāciju-rekordistu meklēšanā var izmantot rijīgus algoritmus?)
* Ar dinamisko programmēšanu iegūts "sešstūris".
  