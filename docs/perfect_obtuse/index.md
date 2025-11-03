---
layout: default
title: Polimondi: Perfekti platleņķu polimondi
---

# Perfekti platleņķu polimondi

Definīcijas sk.  [Kas ir polimondi]({{ '/polyiamond_concepts/' | relative_url }}).

<img
  id="svgImage0"
  alt="My SVG Image"
  src="{{ '/perfect_obtuse/MAX_OBTUSE_12.svg' | relative_url }}"
  width="216"
  height="216"
  style="border:none; background-color:#FFFFE0;"
/>


**Apgalvojums:** 
Lai eksistētu perfekts platleņķu $n$-polimonds, ir nepieciešami, 
lai $n \geq 12$ un $n \equiv 0 \pmod{6}$. 

Pie $n=12$ un $n=18$ eksistē tikai pa vienam perfektam platleņķa polimondam, 
(sk. piemērus lapas apakšā), bet pie $n \geq 24$ šādu polimondu 
skaits strauji pieaug. Tabulā doti lejupielādējami faili 
ar šiem polimondiem - tie pierakstīti kā malu vektoru virzieni,
sākot ar visgarāko polimonda malu līdz visīsākajai.
Polimondi skaitīti, uzskatot figūras, kas atšķiras tikai ar rotāciju 
vai ass simetriju par vienādām. (Platleņķu polimondiem tas nozīmē, ka 
pirmie divi virzienu burti vienmēr ir "AB" - uz austrumiem un tad 
uz ziemeļaustrumiem.)


<table class="csv-table">
  <thead>
    <tr>
      <th>n</th>
      <th>Fails</th>
      <th>Skaits</th>
    </tr>
  </thead>
  <tbody>
    {% for r in site.data.obtuse_count %}
    <tr>
      <td>{{ r.n }}</td>
      <td><a href="http://www.dudajevagatve.lv/static/polimondi/obtuse_{{ r.n }}.txt">obtuse_{{ r.n }}.txt</a></td>
      <td>{{ r.count }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>


**Nepierādīts apgalvojums:** Katram naturālam skaitlim $n \geq 12$, 
kuram $n \equiv 0 \pmod{6}$, eksistē perfekts platleņķu $n$-polimonds.
(T.i. dalāmība ar $6$ polimonda eksistencei ir ne tikai 
nepieciešamais, bet arī pietiekamais nosacījums.)


# Platleņķu polimondu laukumi

**Apgalvojums:** 
Ja $n \equiv 0 \pmod{12}$, tad katra perfekta platleņķu polimonda laukums $A$ ir 
pāra skaitlis, bet ja $n \equiv 6 \pmod{12}$, tad katra perfekta 
platleņķu $n$-polimonda laukums ir nepāra skaitlis.

*Piezīme:* Polimondu laukumus šeit un turpmāk izteiksim "trijstūrīšu vienībās" -- 
uzskatām, ka vienādmalu trijstūrim ar malu $1$ laukums ir $1$ vienība. 
Parastajā Eiklīda telpā $L_2$ laukumu $S$ (vienības kvadrātiņu vienībās)
var iegūt no $A$, pareizinot ar trijstūrīša 
Eiklīda laukumu: $S = A \cdot \frac{\sqrt{3}}{4}$.

**Hipotēze (par platleņķu polimondu maksimālo laukumu):** 
Ar $A_n$ ($n=12,18,24,30,\ldots$) apzīmēsim lielāko iespējamo perfekta 
platleņķu polimonda laukumu (mazajam trijstūrītim laukums ir $1$). 
Ir spēkā šāds apgalvojums:

$$\limsup_{n\to\infty} \frac{A_n}{(n^2(n+1)^2)/32} = 1.$$

T.i. bezgalīgi bieži vislielākais perfektais platleņķa $n$-polimonds 
ir ar laukumu, kas asimptotiski tuvojas regulāra "izrobota sešstūra laukumam", 
kurš novietots vertikāli: 

![Perfekts 42-polimonds]({{ '/images/polyiamond42.png' | relative_url }}){: width="200" }

*Piezīme:* Lai uzkonstruētu augošu naturālu skaitļu 
apakšvirkni $n_1,n_2,\ldots$, kuras locekļi asimptotiski tuvojas sešstūrim, 
būs vajadzīga nepieciešama induktīva (vai kāda cita) konstrukcija, kura 
izveido aptuveni vienāda garuma zigzagveida lauztas līnijas, kuras 
sastāda sešstūri. (Lai figūra būtu noslēgta, var gadīties 
pievienot vēl arī nedaudzas īsas savienotājmalas pašās beigās.)
Ja šāda konstrukcija ir iespējama visiem $n$, kas dalās ar $6$, tad 
augšējās robežas vietā varēs pamatot parastu robežu.

Kāpēc vajadzētu ticēt šai hipotēzei? 
Līdz šim iegūtie maksimālie perfekto platleņķa polimondu laukumi 
(pie $n = 12, \ldots, 48$) tuvojas asimptotiskajam novērtējumam. 
Šie piemēri ir ar maksimālo laukumu un atrasti, izmantojot pilno 
pārlasi. 


<select id="selectSvg" data-base="{{ '/perfect_obtuse/' | relative_url }}">
<option value="MAX_OBTUSE_12.svg;240">MAX_OBTUSE_12</option>
<option value="MAX_OBTUSE_18.svg;360">MAX_OBTUSE_18</option>
<option value="MAX_OBTUSE_24.svg;420">MAX_OBTUSE_24</option>
<option value="MAX_OBTUSE_30.svg;480">MAX_OBTUSE_30</option>
<option value="MAX_OBTUSE_36.svg;540">MAX_OBTUSE_36</option>
<option value="MAX_OBTUSE_42.svg;600">MAX_OBTUSE_42</option>
<option value="MAX_OBTUSE_48.svg;600">MAX_OBTUSE_48</option>
</select>

<img
  id="svgImage"
  alt="My SVG Image"
  src="{{ '/perfect_obtuse/MAX_OBTUSE_12.svg' | relative_url }}"
  width="240"
  style="border:none; background-color:#FFFFE0;"
/>


<table class="csv-table">
  <thead>
    <tr>
      <th>n</th>
      <th>Malas</th>
      <th>Laukums</th>
      <th>Asimptotika</th>
      <th>Attiecība</th>
    </tr>
  </thead>
  <tbody>
    {% for r in site.data.obtuse_max_areas %}
    <tr>
      <td>{{ r.n }}</td>
      <td class="mono">{{ r.sequence }}</td>
      <td>{{ r.area }}</td>
      <td>{{ r.asymptotics }}</td>
      <td>{{ r.ratio }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

Tabulas kolonnu paskaidrojumi: 

* $n$ pieņem visas vērtības, kurām ir atrasti 
  un izpētīti visi perfektie platleņķa polimondi. 
* "Malas" apzīmē to virzienu virknīti, kas ļauj iegūt 
  polimondu ar maksimālo laukumu. 
* "Laukums" ir šī maksimālā polimonda laukums (vienības trijstūrīšos). 
* "Asimptotika" ir laukums "robainajam sešstūrim" $(n^2(n+1)^2)/32$, kurš ir regulārs,  
  un kura perimetru veido zigzagveida lauzta līnija ar posmiem 
  $30^{\circ}$ leņķī pret lielā sešstūra malām.
* "Attiecība" ir maksimālā polimonda un asimptotikas attiecība
  noapaļota līdz 6 cipariem aiz komata.





