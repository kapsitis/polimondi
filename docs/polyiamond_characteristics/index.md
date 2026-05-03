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
