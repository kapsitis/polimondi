---
layout: default
title: Platleņķu regex meklēšana
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
