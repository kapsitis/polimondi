---
layout: default
title: Polimondu raksturlielumi
---

<style>
.boring-table { border-collapse: collapse; width: 100%; margin-bottom: 1rem; }
.boring-table th, .boring-table td { border: 1px solid #ccc; padding: 4px 8px; vertical-align: top; }
.boring-table thead th { background: #f6f8fa; position: sticky; top: 0; z-index: 1; }
.boring-table td:nth-child(1) { text-align: right; width: 3em; }
.mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 0.85em; word-break: break-all; }
details { margin-bottom: 1rem; }
details summary { cursor: pointer; font-weight: bold; padding: 4px 0; }
details summary:hover { text-decoration: underline; }
</style>

# Polimondu raksturlielumi 

## Laukums

Laukumu varētu definēt vai nu kā laukumu 
tradicionālajā Eiklīda plaknē $L_2$ (tas vienmēr ir 
iracionāls skaitlis), vai arī kā polimondā 
ietilpstošo vienības trijstūrīšu skaitu jeb tradicionālo laukumu 
dalītu ar $\sqrt{3}/4$ (tas vienmēr ir vesels skaitlis).

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
area = p.get_area()
print(f'area={area}')

# area = 25617
```


<img
  id="30gon_area"
  alt="Perfekts 30-polimonds"
  src="{{ '/polyiamond_characteristics/30gon_area.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>

## Diametrs

Par *diametru* plaknes figūrai sauc lielāko 
attālums starp figūras punktiem (polimondos un citos daudzstūros  
tās vienmēr ir daudzstūra virsotnes).
"Kompaktām" figūrām ir relatīvi neliels diameters pie 
fiksēta perimetra. (Visu izoperimetrisko plaknes figūru vidū 
mazākais diametrs ir aplim.)

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
diam_sq, i_max, j_max = p.diameter_sq()
print(f'diam_sq={diam_sq}, i_max={i_max}, j_max={j_max}')

# diam_sq=95428, i_max=9, j_max=26
```



<img
  id="30gon_diameter"
  alt="30-polimonda diametrs"
  src="{{ '/polyiamond_characteristics/30gon_diameter.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>



## Platums

Par ierobežotas plaknes figūras *platumu* sauc 
mazāko attālumu starp divām paralēlām *atbalsta taisnēm*, starp kurām 
atrodas figūra. Pietiekami lielam laukumam pie dotā perimetra, 
arī platumam jābūt lielam. 
Platumu var iegūt ar rotējošo skavu (*rotating callipers*) 
algoritmu (vai arī kā minimizācijas uzdevumu virsotņu projekcijām
uz kādu fiksētu taisni). 

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
min_width, seg_min_width, parallel_lines = p.min_width()
print(f'min_width={min_width},')
print(f'seg_min_width={seg_min_width},')
print(f'parallel_lines={parallel_lines}')

# min_width=109.87076689881448,
# seg_min_width=((112.0, 1.7320508075688772), (55.50272034820456, -92.49980585927413)),
# parallel_lines=((37.0, -81.40638795573723), (63.0, -96.99484522385713), (112.0, 1.7320508075688772))
```

<img
  id="30gon_min_width"
  alt="30-polimonda platums"
  src="{{ '/polyiamond_characteristics/30gon_min_width.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Ievilkts riņķis

Par daudzstūri *ievilktu riņķi* sauc lielāko riņķi, 
kurš pilnībā atrodas figūras iekšpusē. Neizliektiem daudzstūriem 
varētu eksistēt vairāki vienāda lieluma ievilktie riņķi, ja, piemēram, 
tā satur vairākus "izaugumus" identisku trijstūru formā. 
Perfektiem polimondiem ar lielu laukumu tā parasti nebūs - tie 
satur savā iekšienē vienu lielu plaknes apgabalu. 
Ja figūra ir gandrīz "apaļa", tad pie dotā perimetra tai būs 
liels ievilktā riņķa rādiuss. 


```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
incircle = p.get_incircle()
print(f'incircle={incircle}')

# incircle=((62.33516483517474, -36.88697214361352), 45.292972491130485)
```

<img
  id="30gon_incircle"
  alt="30-polimonda ievilkts riņķis"
  src="{{ '/polyiamond_characteristics/30gon_incircle.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Apvilkts riņķis

Par daudzstūrim *apvilktu riņķi* sauc mazāko riņķi, 
kurš satur doto figūru.

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
circumcircle = p.get_circumcircle()
print(f'circumcircle={circumcircle}')

# circumcircle=((55.42307692307693, -33.730579188424656), 73.66091885436556)
```

<img
  id="30gon_circumcircle"
  alt="30-polimonda apvilkts riņķis"
  src="{{ '/polyiamond_characteristics/30gon_circumcircle.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Mazākais sešstūris

Mazākais regulārais sešstūris (patvaļīgi pagriezts), kurš 
satur doto polimondu. 

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
hexagon = p.get_smallest_hexagon()
print(f'hexagon={hexagon}')

# hexagon=[(57.19219351042855, 43.601875992409255), (-11.37975989414688, 5.134203513912659), (-12.351755005597049, -73.48468636082082), (55.24820328752825, -113.63590375705769), (123.8201566921037, -75.16823127856108), (124.79215180355388, 3.450658596172353)]
```

<img
  id="30gon_smallest_hexagon"
  alt="30-polimonda mazākais sešstūris"
  src="{{ '/polyiamond_characteristics/30gon_smallest_hexagon.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Mazākais kvadrāts

Mazākais kvadrāts (patvaļīgi pagriezts), kurš 
satur doto polimondu. 

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
square = p.get_smallest_square()
print(f'square={square}')

# square=[(32.23684775994439, -124.65001604883619), (147.2049894160717, -60.7580909233342), (83.31306429056971, 54.210050732793114), (-31.655077365557595, -9.68187439270887)]
```

<img
  id="30gon_smallest_square"
  alt="30-polimonda mazākais kvadrāts"
  src="{{ '/polyiamond_characteristics/30gon_smallest_square.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Mazākais trijstūris

Mazākais regulārais trijstūris (patvaļīgi pagriezts), kurš 
satur doto polimondu. 

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
triangle = p.get_smallest_triangle()
print(f'triangle={triangle}')

# triangle=[(122.63062767637325, -133.0370749227576), (126.61809070888232, 77.82838031485414), (-57.99048182371437, -24.151103021147545)]
```

<img
  id="30gon_smallest_triangle"
  alt="30-polimonda mazākais trijstūris"
  src="{{ '/polyiamond_characteristics/30gon_smallest_triangle.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Tuvākais sešstūris (pēc Hausdorfa)

Regulārs sešstūris $S$ (patvaļīgi pagriezts), līdz kuram dotajam polimondam 
ir mazākais Hausdorfa attālums.
Hausdorfa attālumu definē kā lielāko no attālumiem 
no kādas polimonda virsotnes līdz tās 
tuvākajam punktam uz sešstūra perimetra $P(S)$:

$$
h(P, S) = \max_{v \in P} \left( \min_{q \in P(S)} d(v, q)\right)
$$

No visiem regulāriem sešstūriem $S$ izvēlamies to, kuram $h(P,S)$ ir vismazākais. 


```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
h_hex, dist = p.get_closest_hausdorff_hexagon()
print(f'h_hex={h_hex}')

# h_hex=[(59.57084546535845, 41.75414189844926), (-3.4503763897335062, 6.917133959716978), (-4.79125345049718, -65.07934911369384), (56.88909134383108, -102.23882424837242), (119.91031319892308, -67.40181630964014), (121.25119025968678, 4.5946667637706184)]
```

<img
  id="30gon_hausdorff_hexagon"
  alt="30-polimonda tuvākais sešstūris (Hausdorfa)"
  src="{{ '/polyiamond_characteristics/30gon_hausdorff_hexagon.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Tuvākais trijstūris (pēc Hausdorfa)

Regulārs trijstūris $S$ (patvaļīgi pagriezts), līdz kuram dotajam polimondam 
ir mazākais Hausdorfa attālums.
Hausdorfa attālumu definē kā lielāko no attālumiem 
no kādas polimonda virsotnes līdz tās 
tuvākajam punktam uz trijstūra perimetra $P(S)$:

$$
h(P, S) = \max_{v \in P} \left( \min_{q \in P(S)} d(v, q)\right)
$$

No visiem regulāriem trijstūriem $S$ izvēlamies to, kuram $h(P,S)$ ir vismazākais.


```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
h_tri, dist = p.get_closest_hausdorff_triangle()
print(f'h_tri={h_tri}')

# h_tri=[(-37.603428032177334, -19.544468725195397), (106.3041782745083, -127.50956225373126), (127.85088883884049, 51.10062736993618)]
```

<img
  id="30gon_hausdorff_triangle"
  alt="30-polimonda tuvākais trijstūris (Hausdorfa)"
  src="{{ '/polyiamond_characteristics/30gon_hausdorff_triangle.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Izliektais apvalks

Mazākais izliektais daudzstūris, kurš satur doto polimondu.
Izliektā apvalka laukums izteikts mazo vienības trijstūrīšu vienībās 
(tas vienmēr ir vesels skaitlis).

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
hull = p.convex_hull()
print(f'hull={hull}')
hull_area = p.convex_hull_area()
print(f'hull_area={hull_area}')

# hull=[(-38,52,-14), (-38,64,-26), (-25,78,-53), (-10,94,-84), (7,112,-119), (26,112,-138), (67,92,-159), (89,70,-159), (113,23,-136), (113,-2,-111), (87,-29,-58), (59,-29,-30), (-6,-4,10), (-11,1,10), (-18,14,4), (-27,31,-4)]
# hull_area=29511
```

<img
  id="30gon_convex_hull"
  alt="30-polimonda izliektais apvalks"
  src="{{ '/polyiamond_characteristics/30gon_convex_hull.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Ierobežojošais taisnstūris

Taisnstūris, kura malas paralēlas $x$ un $y$ asīm un kurš satur doto polimondu (mazākais no šādiem taisnstūriem).

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
rect = p.get_bounding_rectangle()
print(f'rect={rect}')

# rect=(-12.0, 124.5, -112.0, 29.0)
```

<img
  id="30gon_bounding_rectangle"
  alt="30-polimonda ierobežojošais taisnstūris"
  src="{{ '/polyiamond_characteristics/30gon_bounding_rectangle.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Ierobežojošais sešstūris

Regulārs sešstūris ar trīsstūru režģim paralēlām malām, kurš satur doto polimondu (mazākais no šādiem sešstūriem).

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
hex_bounds = p.get_bounding_hexagon()
print(f'hex_bounds={hex_bounds}')

# hex_bounds=(-29, 112, -159, 10, -38, 113)
```

<img
  id="30gon_bounding_hexagon"
  alt="30-polimonda ierobežojošais sešstūris"
  src="{{ '/polyiamond_characteristics/30gon_bounding_hexagon.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>


## Izodiametriskais un izoperimetriskais koeficienti

Starp visām figūrām ar doto diametru $D$, vislielākais laukums $A$
ir aplim. Līdzīgi arī starp visām figūrām ar doto perimetru $P$ 
vislielākais laukums ir aplim. Tāpēc katrai figūrai $S$, 
kam laukumu apzīmējam ar $A(S)$, diametru ar $D(S)$, 
perimetru ar $P(S)$, definē šādus koeficientus: 

$$q_{ID}(S) = \frac{4 A(S)}{\pi \cdot D(S)^2}, \quad q_{IP}(S) = \frac{4\pi \cdot A(S)}{P(S)^2}.$$

Angliski tie ir pazīstami kā *isodiametric quotient (ID)* un *isoperimetric quotient (IP)*. 
Šo koeficientu vērtība ir no $0$ neieskaitot (ļoti izstieptām figūrām) 
līdz $1$ ieskaitot (aplim).



## Šauro leņķu skaits

Katram polimondam var būt četru dažādu veidu leņķi, kuru leņķiskie lielumi ir 
$60^\circ$, $120^\circ$, $240^\circ$ un $300^\circ$.
Klasē `Polyiamond` ir definēta funkcija, kas tos visus saskaita. 

Ņemot vērā to, ka lielāki laukumi parasti tiek sasniegti tad, ja 
visi vai gandrīz visi leņķi ir plati ($120^\circ$ vai $240^\circ$), 
tad katram $n$-polimondam var saskaitīt šauro leņķu ($60^\circ$ un $300^\circ$) 
skaitu $k$, un tad platie leņķi būs visi pārējie $n-k$. 

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
(a60, a120, a240, a300) = p.internal_angles()
print(f'(a60, a120, a240, a300) = ({a60}, {a120}, {a240}, {a300})')
(acute, obtuse) = (a60 + a300, a120 + a240)
print(f'(acute, obtuse) = ({acute}, {obtuse})')

```



## Inerces tenzors 

Pieņemam, ka figūra (polimonds) $S$ pārnesta tā, ka 
$O(0,0)$ ir figūras smaguma centrs.
Par inerces tenzoru 2D figūrai $S$ sauc matricu: 

$${\cal I}(S) = \left( \begin{array}{cc} I_{xx} & I_{xy} \\ I_{yx} & I_{yy} \end{array} \right) = 
\left( \begin{array}{cc} \int_S y^2 dA & -\int_S xy dA \\ -\int_S xy dA & \int_S x^2 dA\end{array} \right)$$

Ar $\lambda_1$ un $\lambda_2$ apzīmēsim šīs matricas īpašvērtības.

Šādā gadījumā polārais inerces moments ir:
$$I_z(S) = \int_S r^2 dA  = I_{xx} + I_{yy} = \int_S (x^2+y^2) dx dy = \lambda_1 + \lambda_2.$$

Figūras nesimetriskuma mērs ir frakcionālā anizotropija:
$$A(S) = \frac{|\lambda_2 - \lambda_1|}{\lambda_1 + \lambda_2} = \frac{\lambda_2 - \lambda_1}{I_z(S)}, \quad \lambda_1 \le \lambda_2.$$

```
from polyforms.polyiamond import Polyiamond
p = Polyiamond('ABAFAFEFEDEDCDCDCDCBCBCBCBAFAF')
inertia_tensor = p.get_inertia_tensor()
print(f'inertia_tensor={inertia_tensor}')

# [[22026287.09102281 24281789.1875    ]
#  [24281789.1875     51188299.77810814]]
```






## Bibliotēkas

* C++ bibliotēka CGAL [https://www.cgal.org/](https://www.cgal.org/).
* Python bibliotēka Shapely [https://shapely.readthedocs.io/en/stable/](https://shapely.readthedocs.io/en/stable/).
