---
layout: default
title: Polimondi: Perfekti platleņķu polimondi
---

## Perfekti platleņķu polimondi

![Alt text]({{ '/images/polyiamond42.png' | relative_url }}){: width="200" }

<table class="csv-table">
  <thead>
    <tr>
      <th>n</th>
      <th>Malas</th>
      <th>Laukums</th>
    </tr>
  </thead>
  <tbody>
    {% for r in site.data.obtuse %}
    <tr>
      <td>{{ r.n }}</td>
      <td class="mono">{{ r.sequence }}</td>
      <td>{{ r.area }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<style>
.csv-table { border-collapse: collapse; width: 100%; }
.csv-table th, .csv-table td { border: 1px solid #ccc; padding: 4px 8px; vertical-align: top; }
.csv-table thead th { background: #f6f8fa; }
.mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }
</style>
