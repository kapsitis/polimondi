---
layout: default
title: Polimondi: Perfekti platleņķu polimondi
---

# Perfekti platleņķu polimondi

Definīcijas sk.  [Kas ir polimondi]({{ '/perfect_acute/' | relative_url }}).

<select id="selectSvg" data-base="{{ '/polyiamond_concepts/' | relative_url }}">
<option value="MAX_OBTUSE_12.svg;216;216">MAX_OBTUSE_12</option>
<option value="MAX_OBTUSE_18.svg;432;432">MAX_OBTUSE_18</option>
<option value="MAX_OBTUSE_24.svg;720;792">MAX_OBTUSE_24</option>
<option value="MAX_OBTUSE_30.svg;1224;1152">MAX_OBTUSE_30</option>
<option value="MAX_OBTUSE_36.svg;1440;1800">MAX_OBTUSE_36</option>
<option value="MAX_OBTUSE_42.svg;1944;2520">MAX_OBTUSE_42</option>
<option value="MAX_OBTUSE_48.svg;2736;3456">MAX_OBTUSE_48</option>
</select>

<img
  id="svgImage"
  alt="My SVG Image"
  src="{{ '/perfect_obtuse/MAX_OBTUSE_12.svg' | relative_url }}"
  width="216"
  height="216"
  style="border:none; background-color:#FFFFE0;"
/>


**Apgalvojums:** 
Lai eksistētu perfekts platleņķu $n$-polimonds, ir nepieciešami, 
lai $n \geq 12$ un $n \equiv 0 \pmod{6}$. 

**Pierādījums:**
TBD

<table class="csv-table">
  <thead>
    <tr>
      <th>n</th>
      <th>Skaits</th>
    </tr>
  </thead>
  <tbody>
    {% for r in site.data.obtuse_count %}
    <tr>
      <td>{{ r.n }}</td>
      <td>{{ r.count }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

*Piezīme:* Esam pārliecināti, ka nosacījums ($n \geq 12$ un $n \equiv 0 \pmod{6}$)
ir arī pietiekams, lai eksistētu perfekts platleņķu $n$-polimonds.
Bet tas būtu jāpamato ar induktīvu konstrukciju vai kādu citu eksistences teorēmu.


# Platleņķu polimondu laukumi

**Apgalvojums:** 
Ja $n \equiv 0 \pmod{12}$, tad katra perfekta platleņķu polimonda laukums $A$ ir 
pāra skaitlis, bet ja $n \equiv 6 \pmod{12}$, tad katra perfekta 
platleņķu $n$-polimonda laukums ir nepāra skaitlis. 
(Vienības trijstūrīša laukums ir $1$. Tad parastais Eiklīda telpas laukums
ir izsakāms kā $A \cdot \frac{\sqrt{3}}{4}$.)

<table class="csv-table">
  <thead>
    <tr>
      <th>n</th>
      <th>Malas</th>
      <th>Laukums</th>
    </tr>
  </thead>
  <tbody>
    {% for r in site.data.obtuse_max_areas %}
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






**Hipotēze (par platleņķu polimondu maksimālo laukumu):** 
Ar $A_n$ ($n=12,18,24,30,\ldots$) apzīmēsim lielāko iespējamo perfekta 
platleņķu polimonda laukumu (mazajam trijstūrītim laukums ir $1$). 
Ir spēkā 

$$\limsup_{n\to\infty} \frac{A_n}{(n^2(n+1)^2)/32} = 1.$$

T.i. bezgalīgi bieži vislielākais perfektais platleņķa $n$-polimonds 
ir ar laukumu, kas asimptotiski tuvojas regulāra sešstūra laukumam, 
kura malas ir izrobotas tā, ka visi nogriežņi, kas atrodas uz robiņiem 
veido ar sešstūra malu $30^{\circ}$ leņķi. 

*Piezīme:* Lai uzkonstruētu augošu naturālu skaitļu 
apakšvirkni $n_1,n_2,\ldots$, kuras locekļi asimptotiski tuvojas sešstūrim, 
ir nepieciešama induktīva (vai kāda cita) konstrukcija, kura 
izveido aptuveni vienāda garuma zigzagveida lauztas līnijas, kuras 
sastāda sešstūri. (Lai figūra būtu noslēgta, var gadīties 
pievienot vēl arī nedaudzas īsas savienotājmalas pašās beigās.)
Ja šāda konstrukcija ir iespējama visiem $n$, kas dalās ar $6$, tad 
augšējās robežas vietā var pierādīt parastu robežu.

![Perfekts 42-polimonds]({{ '/images/polyiamond42.png' | relative_url }}){: width="200" }
