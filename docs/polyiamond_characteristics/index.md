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

diam_sq=95428, i_max=9, j_max=26
```



<img
  id="30gon_diameter"
  alt="30-polimonda diametrs"
  src="{{ '/polyiamond_characteristics/30gon_diameter.svg' | relative_url }}"
  style="width: 100%; max-width: 600px; border:none; background-color:#FFFFE0;"
/>



## Platums


