# Polinomu problēmas

**Anotācija:** Šajā sadaļā aplūkojam uzdevumus, kas radniecīgi perfekto 
polomondu uzdevumam: Doti vektori garumā $1,2,3,\ldots,n$. 
Saskaitām veidus, kā šos vektorus var pagriezt, lai to summa būtu nulles vektors.
Aplūkojam vairākus veidus, kā šos vektorus var pagriezt:
* Vienā no diviem pretējiem virzieniem ar $180^{\circ}$ leņķi. 
* Vienā no trim pretējiem virzieniem ar $120^{\circ}$ leņķi. 
* Vienā no četriem pretējiem virzieniem ar $90^{\circ}$ leņķi. 
* Vienā no sešiem pretējiem virzieniem ar $60^{\circ}$ leņķi. 

Sāksim ar ["plus-minus" uzdevumu](https://johnlekberg.com/blog/2020-07-09-plus-minus.html). 


**Problēma (Plus-mīnus uzdevums):** 
Izrakstīti visi naturāli skaitļi no $1$ līdz $n$ augošā secībā. 
Cik dažādos veidos var pirms katra no šiem skaitļiem ierakstīt "+" un "-" zīmes tā, 
lai visu skaitļu summa būtu $0$. 

Ierakstot zīmes, var dabūt dažādus skaitļus no $-n(n+1)/2$ līdz $n(n+1)/2$.
Iespēja dabūt $0$ rodas vienīgi tad, ja $n(n+1)/2$ ir pāra skaitlis. 
Tātad, šim "plus-mīnus uzdevumam" eksistē kaut viens atrisinājums  
tikai tad, ja $n$ pieņem vērtības $3, 4, 7, 8, 11, 12, 15, 16, \ldots$. 
T.i. nepieciešams, lai $n$ dotu atlikumu $3 vai 0$, dalot ar $4$. 

Efektīvs saskaitīšanas veids ir, piemēram, dinamiskā programmēšana, kur veidojam 
tabulu $a_{n,k}$ (kur $n$ ir uzdevumā doto skaitļu skaits, bet $k$ pieņem 
visas vērtības starp $-n(n+1)/2$ un $n(n+1)/2$). Katrai nākamajai tabulas 
rindiņai līdzīgi kā Paskāla trijstūrī izmantojam iepriekšējo rindiņu: 
skaitlis $n$ tajā rindiņā un $k$ tajā kolonnā $a_{n,k}$ iegūstams kā 
summa $a_{n-1,k-n} + a_{n-1,k+n}$. Programma šādu tabulu līdz vajadzīgajai 
vietai var izrēķināt $O(n^3)$ laikā. Sk. 
failu ``plus_minus_dynamic.py``. Sk. izvadi no programmas 
``plus_minus_dynamic.py 7``. 

``` text
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 *1* 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 *0* 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 *0* 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 *2* 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 2 0 2 0 *2* 0 2 0 2 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 2 0 2 0 3 0 3 0 3 *0* 3 0 3 0 3 0 2 0 2 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 0 1 0 1 0 2 0 2 0 3 0 4 0 4 0 4 0 5 0 5 *0* 5 0 5 0 4 0 4 0 4 0 3 0 2 0 2 0 1 0 1 0 1 0 0 0 0 0 0 0 
1 0 1 0 1 0 2 0 2 0 3 0 4 0 5 0 5 0 6 0 7 0 7 0 8 0 8 0 *8* 0 8 0 8 0 7 0 7 0 6 0 5 0 5 0 4 0 3 0 2 0 2 0 1 0 1 0 1 
```

Pievērsiet uzmanību vidējai vertikālei, kas parāda, cik veidos var iegūt $0$ 
pie $n = 0,1,2,3,4,5,6,7$. Piemēram, $a_{4,0} = 2$, jo 

$$1 - 2 - 3 + 4 = 0,\; -1 + 2 + 3 - 4 = 0$$. 

## Ģenerējošā funkcija

$$\left( x^{-1} + x^1 \right) \left( x^{-2} + x^{2} \right) \ldots \left( x^{-n} + x^n \right)$$

Veidi, kā katrā no iekavām var izvēlēties kādu no saskaitāmajiem augšminētajā izteiksmē, sakrīt 
ar veidu skaitu, kā var atrisināt "plus-mīnus uzdevumu". 
Ja mums nepatīk negatīvas pakāpes, varam katru no iekavām piereizināt ar 
$x$ pakāpi (pirmo iekavu ar $x^1$, otro iekavu ar $x^2$, utt.). Iegūstam izteiksmi: 

$$\left( 1 + x^2 \right) \left( 1 + x^4 \right) \ldots \left( 1 + x^{2n} \right)$$


## Divide-and-Conquer pieeja

Mēs varam aprēķināt vienīgo nezināmo koeficientu, grupējot 
garo polinomu reizinājumu divās daļās: 

$$P(x) = \left( 1 + x^2 \right) \left( 1 + x^4 \right) \ldots \left( 1 + x^{2m} \right),$$
$$P(x) = \left( 1 + x^{2m+2} \right) \left( 1 + x^{2m+4} \right) \ldots \left( 1 + x^{2n} \right).$$

Pirmās $80$ vērtības šai virknei: 

```
1, 
0, 0, 2, 2, 0, 0, 8, 14, 0, 0, 
70, 124, 0, 0, 722, 1314, 0, 0, 8220, 15272, 
0, 0, 99820, 187692, 0, 0, 1265204, 2399784, 0, 0, 
16547220, 31592878, 0, 0, 221653776, 425363952, 0, 0, 3025553180, 5830034720, 
0, 0, 41931984034, 81072032060, 0, 0, 588491482334, 1140994231458, 0, 0, 
8346638665718, 16221323177468, 0, 0, 119447839104366, 232615054822964, 0, 0, 1722663727780132, 3360682669655028
0, 0, 25011714460877474, 48870013251334676, 0, 0, 365301750223042066, 714733339229024336, 0, 0, 
5363288299585278800, 10506331021814142340, 0, 0, 79110709437891746598, 155141342711178904962, 0, 0, 1171806326862876802144, 2300241216389780443900
```

