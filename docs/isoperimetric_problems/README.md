# Izoperimetriskie uzdevumi

Fiksētai $n$ vērtībai trijstūru režģī kā parasti definējam 
*maģisku* $n$-polimondu (kura malu garumi ir visi skaitļi no $[1;n]$
patvaļīgā secībā) un *perfektu* $n$-polimondu (kura malu garumi 
ir visi skaitļi $[1;n]$, kuri pēc kārtas seko viens otram).
Gan maģiskiem, gan perfektiem polimondiem ir viens un tas pats 
perimetrs (skaitļu summa $1+2+\ldots+n = \frac{n(n+1)}{2}$).

Atsevišķi aplūkojam vēl šādas polimondu klases: 

A. Visi polimondi ar doto perimetru $P=\frac{n(n+1)}{2}$ vai arī patvaļīgam 
   perimetram $P$. 
B. Visi polimondi ar tieši $n$ malām un doto perimetru $P=\frac{n(n+1)}{2}$
   vai arī patvaļīgam perimetram $P$. 
C. Visi polimondi ar doto perimetru $P=\frac{n(n+1)}{2}$ un dažāda garuma malām 
   (malu skaits var būt jebkurš). Vai arī patvaļīgam perimetram $P$. 
D. Visi maģiskie polimondi ar $n$ malām. 
E. Visi maģiskie polimondi, kam (pie dotās $n$ vērtības) ir maksimāli daudz 
   šauru leņķu. 
F. Visi maģiskie polimondi, kam (dotajai $n$ vērtībai) ir maksimāli daudz 
   platu leņķu.
G. Visi maģiskie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visretāk veic "ieliekumu" (t.i. pagriezienu pretēji polimonda kopīgajai orientācijai). 
H. Visi maģiskie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visbiežāk veic "ieliekumu" (t.i. pagriezienu pretēji polimonda kopīgajai orientācijai). 
I. Visi maģiskie polimondi, kam malu garumu virknes diferencēm 
   $\Delta_i = a_{i+1} - a_{i}$ 
   ir ne vairāk 2 cikliskās zīmju maiņas (*cyclic alternation number* nepārsniedz $2$). 
   Piemēram, identiskajai permutācijai $(1,2,3,4,5)$ un permutācijai 
   $(1,3,5,4,2)$ abām ir tieši divas zīmju maiņas, ja pa apli izrēķina 
   visas starpības - t.i. virkne no augošas kļūst dilstoša un atpakaļ. 
J. Visi maģiskie polimondi, kuriem cikliskās blakusesošo malu garumu
   starpības pēc moduļa ir $1$, izņemot vienā vai divās vietās. 
K. Visi maģiskie polimondi, kuru malu garumi, izrakstot tos apskatot pa apli, 
   veido permutāciju $(p_1,p_2,\ldots,p_n)$ tā, ka 
   $p_i \equiv i$ pēc moduļa $m$, kur $m \in \{ 2,3,4,5,6 \}$
L. Visi perfektie polimondi.
M. Visi perfektie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visretāk veic "ieliekumu".
N. Visi perfektie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visbiežāk veic "ieliekumu".
O. Visi perfektie polimondi, kuriem visi leņķi ir šauri. 
P. Visi perfektie polimondi, kuriem visi leņķi ir plati. 

Šādām polimondu klasēm var aplūkot dažādas 
ģeometriskās īpašības (laukums, ievilktā/apvilktā riņķa
rādiuss, ierobežojošais taisnstūris vai sešstūris utt.).
"Tradicionālām" ģeometrisku figūru saimēm
(plaknes figūrām ar gludu robežu, patvaļīgiem $n$-stūriem,
patvaļīgiem polimondiem) šīs un līdzīgas
īpašības ir jau optimizētas -- ir zināmas figūras, kurām 
tās pieņem lielākās vai mazākās vērtības.

Savukārt, augšminētajām polimondu klasēm ir spēkā vairāki 
ierobežojumi, tāpēc tām optimizācijas uzdevumu atbildes 
kļūst sarežģītākas. Atbildot uz šiem jautājumiem, iegūstam 
jaukus daudzstūru piemērus un arī dziļāku izpratni par to, 
kādi vispār mēdz būt attiecīgās saimes daudzstūri un 
cik "blīvi" tie izvietoti (t.i. cik tuvu faktiski atrastie 
optimālie daudzstūri no attiecīgās saimes ir tam, kas 
būtu optimāli kādā virskopā). 




## Ģeometriskie raksturlielumi 

Katrs no zemāk minētajiem ģeometriskajiem raksturlielumiem 
(laukums, platums, utt.) ļauj uzdot vairākus 
*izoperimetriskos jautājumus*:

* Atrast raksturlieluma lielāko un mazāko iespējamo vērtību 
  $n$-polimondam no dotās saimes katram fiksētam naturālam skaitlim $n$.  
* Atrast kādas vispār ir iespējamās raksturlieluma vērtības 
  $n$-polimondam no dotās saimes; kuras no vērtībām dažādu 
  invariantu dēļ ir neiespējamas.
* Atrast, vai optimālo vērtību sasniedz viens vai varbūt 
  vairāki polimondi no dotās saimes. Ja ir spēkā unikalitātes
  rezultāti, tad censties tos pamatot.
* Tām $n$ vērtībām, kurām optimumu atrast neizdodas, atrast 
  pietiekami labus novērtējumus gan lielākajai, gan mazākajai 
  vērtībai. 
* Saprast, kā konstruējami $n$-polimondu piemēri, kuri ir vai 
  nu optimāli dotajam $n$, vai sasniedz pietiekami labu novērtējumu.
  Tai skaitā var konstruēt arī induktīvas polimondu virknes, 
  atrodot optimālus polimondus *bezgalīgi bieži* (jeb 
  bezgalīgi augošām polimondu virknēm). 
* Pamatot asimptotiskus novērtējumus un rezultātus, kuri 
  ir spēkā "pietiekami lielām" $n$ vērtībām. 
* Aplūkot efektīvus algoritmus polimondu piemēru atrašanai. 
  Gan pilno pārlasi jeb *backtracking*, 
  gan dažādi paātrinātu pilno pārlasi, gan mašīnmācīšanās modeļus (PyTorch)
  un/vai ģenētiskos algoritmus, gan paralēlus algoritmus.   


## Metriku atbilstības problēma

**Hipotēze:** Eksistē kāds ģeometrisks raksturlielums, kura maksimums 
vai minimums kādai no polimondu saimēm ir "sinonīms" maksimālajam laukumam. 
Citiem vārdiem: Katrai (vai vismaz pietiekami lielai) $n$ vērtībai
eksistē tāds $n$-polimonds $P_n$ ar maksimālo laukumu starp visiem 
attiecīgās saimes $n$-polimondiem, kurš vienlaikus ir rekordists arī 
attiecībā pret kādu citu ģeometrisku raksturlielumu.






### 1. Laukums (*Area*)

**Definīcija:** 
  Vai nu tradicionālā figūras laukuma definīcija 
  Eiklīda plaknē $L_2$ vai arī polimondā ietilpstošo vienības 
  trijstūrīšu skaits (t.i. figūras laukums dalīts ar $\sqrt{3}/4$). 

**Intuīcija:**
  Laukums ir svarīgs figūras invariants un to var rēķināt dažādos veidos

**Algoritms:**
  Laukumu var atrast ar paralelizējamu "kurpju šņoru algoritmu".



### 2. Diametrs (*Diameter*)

**Definīcija:** 
  Lielākais attālums starp figūras punktiem (daudzstūra virsotnēm).

**Intuīcija:**
  "Kompakti" novietotām figūrām ir mazs diameters, piemēram, visu fiksēta 
  perimetra figūru vidū aplis ir optimāls.

**Algoritms:** 
  Paralelizētā algoritmā var meklēt maksimālo vērtību virsotņu attālumu matricā. 



### 3. **Platums** (*Width*)

**Definition:** 
  Minimālais attālums starp divām paralēlām atbalsta taisnēm, starp kurām 
  atrodas figūra (t.i. taišņu atstarpe "tievākajā" virzienā). 

**Intuīcija:**
  Parasti gribam maksimizēt platumu. 
  Figūra, kurai ir liels laukums, nevar būt ļoti mazs platums - 
  tā ir tuvāka aplim nevis tievam un izstieptam daudzstūrim. 

**Algoritms:** 
  Platumu var iegūt ar rotējošo skavu (*rotating callipers*) 
  algoritmu. To var reducēt arī uz minimizācijas uzdevumu virsotņu projekcijām
  uz taisni. 


### 4. **Radius of Inscribed Circle** (*Inradius*)

**Definīcija:** 
  Lielākais riņķis, kurš pilnībā atrodas figūras iekšpusē.

**Intuīcija:** 
  Kāds ir vislielākais ievilktā riņķa rādius starp visiem polimondiem 
  no dotās saimes. Cieši saistīts ar to, cik figūra ir "apaļa".

**Algoritms:** 
  TBD.


### 5. **Radius of Circumscribed Circle** (Circumradius)

**Definīcija:**
  Mazākais riņķis, kurš satur doto figūru.

**Intuīcija:** 
  

- **Isoperimetric question:** *What is the minimal circumradius?*

---

### 6. **Compactness / Roundness**

- **Definition:** Quantities like \(\frac{\text{Area}}{\text{Diameter}^2}\), which measure how circular or compact a shape is for its perimeter.

**Intuīcija:** 
  Maksimāls kompaktums piemīt figūrām, kuras ir tuvas apļa formai. 

**Algoritms:** 
  Pietiek ievietot formulā. 


### 7. Inerces moments (*Moment of Inertia*)
- **Definition:** \(\int (r^2) dA\), where \(r\) is distance to centroid.
- **Isoperimetric question:** *What shape minimizes/maximizes moment of inertia for given area/perimeter?*
- **Popular in:** Physics, shape optimization. Easily converted into matrix operations from coordinates.

---

### 8. **Bounding Rectangle Area**
- **Definition:** Minimal area rectangle containing the shape.
- **Isoperimetric question:** *Which polyiamond minimizes this for a fixed perimeter?*
- **Matrix-friendly:** Yes; quick for GPU with known vertices.

---

### 9. **Symmetry Measures**
- **Definition:** Quantify (perhaps via representations or principal axes) how symmetric a shape is.
- **Isoperimetric question:** *Among polygons with given side lengths, which is most/least symmetric?*
- **Matrix-friendly:** Eigenvalue decomposition of inertia tensor.

---

### 10. **Convex Hull Area**
- **Definition:** Area of the convex hull.
- **Relevance:** Useful if studying "how concave" a given shape is (difference between hull area and polygon area).

---

### 11. **Number of Vertices with Acute/Obtuse Angles**
- **Definition:** Count of angles of given type.
- **Documentation:** Can optimize for extremal angles, which connects to classical questions in combinatorics and geometric design.

---

### 12. **Cheeger Constant (Isoperimetric Quotient)**
- **Definition:** Ratio of perimeter to area (or area to perimeter squared).
- **Isoperimetric question:** *Which shape optimizes this within the prescribed family?*
- **Relevance:** Used in analysis, spectral geometry, fluid dynamics.

---

### 13. Hausdorfa attālums līdz dotai figūrai (*Hausdorff Distance to a Reference Shape*)

**Definīcija:** 
  Cik tālu figūra ir no ideāla apļa vai sešstūra.

**Intuīcija:** 
  Kura no figūrām dotajā klasē ir vistuvāk regulāram sešstūrim. 

**Algoritms:** 
  Attāluma matricas(?) starp punktu mākoņiem abās figūrās.




## Paralizējami aprēķini ar virsotņu vai malu vektoriem

* Laukums (*Area*): Polimondu laukuma formula (kurpju šņoru algoritms).
* Diametrs (*Diameter*): Rēķina attālumus virsotņu pāriem un maksimumus.
* Ievilktā/apvilktā riņķa rādiuss (*Inradius/circumradius*): 
  Lineāras programmas, kas izmanto malas un leņķus. 
* Inerces moments (*Moment of inertia*): Summē pa virsotnēm 
  vai mazajiem trijstūrīšiem; matricu darbības.
* Izliektā čaula (*Convex hull*): Kaut kādi specializēti izliekto čaulu 
  algoritmi Fast parallel algorithms for 2D hulls.
* Ierobežojošais taisnstūris/sešstūris (*Bounding rectangle/hexagon*): 
  Rotējošo skavu algoritms; var vektorizēt.
* Simetrija (*Symmetry*) Inerces tenzora īpašvērtību dekompozīcija.
* Šauro/plato leņku skaits (*Acute/obtuse angle counts*):
  Vektoru skalārie reizinājumi. 
* Ieliekumu skaits (*Concave bends*): Vektoru skalārie reizinājumi. 

Vairums no šiem lielumiem ir efektīvi izrēķināmi; vektoru/matricu operācijām 
var izmantot GPU optimizācijas, ja daudzstūru ievades dati (virsotņu 
koordinātes) ir jau sagatavotas.


## **Summary Table**:

| Property                     | Natural Isoperimetric Q?        | Matrix/Algebra Friendly? | Optimized for...  |
|------------------------------|----------------------------------|-------------------------|-------------------|
| Area                         | Max (classic)                    | Yes                     | Enclosed region   |
| Diameter                     | Min/Max                          | Yes                     | Spread            |
| Width                        | Min/Max                          | Yes                     | Thinness          |
| Inradius                     | Max                              | Yes                     | Inscribed circle  |
| Circumradius                 | Min                              | Yes                     | Circumscribed c.  |
| Compactness                  | Max                              | Yes                     | "Roundness"       |
| Inertia                      | Min/Max                          | Yes                     | Mass distribution |
| Bounding Rec. area           | Min/Max                          | Yes                     | Boxiness          |
| Convex Hull area             | Min/Max                          | Yes                     | Convexity measure |
| Acute/obtuse angle count     | Min/Max                          | Yes                     | Angular structure |
| Hausdorff dist. to prototype | Min                              | Yes                     | Shape similarity  |

---


**Bibliotēkas**

* C++ bibliotēka CGAL [https://www.cgal.org/](https://www.cgal.org/).
* Python bibliotēka Shapely [https://shapely.readthedocs.io/en/stable/](https://shapely.readthedocs.io/en/stable/).