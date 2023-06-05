# Laukumu novērtējumi

Katrai no $n$ vērtībām intervālā $[5;12]$ dots maksimālais maģiska polimonda laukums ar $n$ malām 
(izteikts vienības trijstūrīšu laukumos). Līdzās tam - polimonda perimetrs un arī 
cik liels būtu riņķa laukums ar attiecīgo perimetru (un arī pa trijstūra režģa līnijām tuvināta 
riņķa laukums ar šo perimetru). 

Izmantotas šādas formulas: 

* ${\displaystyle S_{\mbox{unit}} = \frac{\sqrt{3}}{4}}$ - mazā trijstūrīša laukums. 
* ${\displaystyle P = 1+2+3+\ldots +n = \frac{n(n+1)}{2}}$ - maģiska $n$-polimonda perimetrs. 
* ${\displaystyle s_{\mbox{circle}} = \frac{P^2}{4 \pi \cdot S_{\mbox{unit}}}}$ - laukums riņķim ar perimetru $P$ (nesasniedzams maksimums)
* ${\displaystyle s_{\mbox{grid-circle}} = \frac{P^2 \cdot \pi}{48 \cdot S_{\mbox{unit}}}}$ - laukums "riņķim" ar perimetru $P$, ja tuvina īstu riņķi ar trijstūru režģa līnijām.
* ${\displaystyle s_{\mbox{hexagon}} = \frac{P^2 \cdot \sqrt{3}}{24 \cdot S_{\mbox{unit}}}}$ - laukums regulāram sešstūrim ar perimetru $P$

Šeit ar lielo burtu $S$ apzīmēts laukums vienības kvadrātos, bet ar 
mazo burtu $s$ apzīmēti laukumi vienības trijstūrīšos.



| $n$      | Laukums | Perimetrs  | Riņķa laukums | "Režģa riņķa" laukums | Sešstūra laukums  |
| -------- | ------- | ---------- | ------------- | --------------------- | ----------------- |
| 5        | 31      | 15         | 41.3          | 34.0                  | 37.5              |
| 6        | 67      | 21         | 81.0          | 66.7                  | 73.5              |
| 7        | 116     | 28         | 144.1         | 118.5                 | 130.7             |
| 8        | 208     | 36         | 238.2         | 195.9                 | 216.0             |
| 9        | 315     | 45         | 372.1         | 306.1                 | 337.5             |
| 10       | 483     | 55         | 555.9         | 457.2                 | 504.2             |
| 11       | 670     | 66         | 800.5         | 658.4                 | 726.0             |
| 12       | 958     | 78         | 1118.1        | 919.6                 | 1014.0            |


[(5, 37.5), (6, 73.5), (7, 130.7), (8, 216.0), (9, 337.5), (10, 504.2), (11, 726.0), (12, 1014.0)]
