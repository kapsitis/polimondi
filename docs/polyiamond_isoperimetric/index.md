---
layout: default
title: Izoperimetriskie uzdevumi
---
# Izoperimetriskie uzdevumi

Gan maģiskiem, gan perfektiem polimondiem ir viens un tas pats 
perimetrs (skaitļu summa $1+2+\ldots+n = \frac{n(n+1)}{2}$).

Atsevišķi aplūkojam vēl šādas polimondu klases: 

1. Visi polimondi ar doto perimetru $P=\frac{n(n+1)}{2}$ vai arī patvaļīgam perimetram $P$. 
2. Visi polimondi ar tieši $n$ malām un doto perimetru $P=\frac{n(n+1)}{2}$ vai arī patvaļīgam perimetram $P$. 
3. Visi polimondi ar doto perimetru $P=\frac{n(n+1)}{2}$ un dažāda garuma malām 
   (malu skaits var būt jebkurš). Vai arī patvaļīgam perimetram $P$. 
4. Visi maģiskie polimondi ar $n$ malām. 
5. Visi maģiskie polimondi, kam (pie dotās $n$ vērtības) ir maksimāli daudz 
   šauru leņķu. 
6. Visi maģiskie polimondi, kam (dotajai $n$ vērtībai) ir maksimāli daudz 
   platu leņķu.
7. Visi maģiskie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visretāk veic "ieliekumu" (t.i. pagriezienu pretēji polimonda kopīgajai orientācijai). 
8. Visi maģiskie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visbiežāk veic "ieliekumu" (t.i. pagriezienu pretēji polimonda kopīgajai orientācijai). 
9. Visi maģiskie polimondi, kam malu garumu virknes diferencēm 
   $\Delta_i = a_{i+1} - a_{i}$ 
   ir ne vairāk 2 cikliskās zīmju maiņas (*cyclic alternation number* nepārsniedz $2$). 
   Piemēram, identiskajai permutācijai $(1,2,3,4,5)$ un permutācijai 
   $(1,3,5,4,2)$ abām ir tieši divas zīmju maiņas, ja pa apli izrēķina 
   visas starpības - t.i. virkne no augošas kļūst dilstoša un atpakaļ. 
10. Visi maģiskie polimondi, kuriem cikliskās blakusesošo malu garumu
   starpības pēc moduļa ir $1$, izņemot vienā vai divās vietās. 
11. Visi maģiskie polimondi, kuru malu garumi, izrakstot tos apskatot pa apli, 
   veido permutāciju $(p_1,p_2,\ldots,p_n)$ tā, ka 
   $p_i \equiv i$ pēc moduļa $m$, kur $m \in \{ 2,3,4,5,6 \}$
12. Visi perfektie polimondi.
13. Visi perfektie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visretāk veic "ieliekumu".
14. Visi perfektie polimondi, kuru kontūrs (dotajai $n$ vērtībai) 
   visbiežāk veic "ieliekumu".
15. Visi perfektie polimondi, kuriem visi leņķi ir šauri. 
16. Visi perfektie polimondi, kuriem visi leņķi ir plati. 

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
  gan dažādi paātrinātu pilno pārlasi, gan mašīnmācīšanās modeļus.   


## Metriku atbilstības problēma

**Hipotēze 1:**   
Eksistē kāds ģeometrisks raksturlielums, kura maksimums 
vai minimums kādai no polimondu saimēm ir "sinonīms" maksimālajam laukumam. 
Citiem vārdiem: Katrai (vai vismaz pietiekami lielai) $n$ vērtībai
eksistē tāds $n$-polimonds $P_n$ ar maksimālo laukumu starp visiem 
attiecīgās saimes $n$-polimondiem, kurš vienlaikus ir rekordists arī 
attiecībā pret kādu citu ģeometrisku raksturlielumu.

**Hipotēze 2:**  
Ģenerējot bezgalīgas polimondu virknes ar formālām valodām, 
var mēģināt aprobežoties ar tiem polimondiem, kuriem kāds no ģeometriskajiem 
raksturlielumiem pieņem minimālo vai maksimālo vērtību.  


## Piemēri

Konkrētam 30 virsotņu perfektam polimondam (ar visiem platiem leņķiem)
izrēķināti dažādi ģeometriskie raksturlielumi - tā ir ilustrācija augšminētājai
ģeometrisko īpašību pētīšanas pieejai. 

Sk. [Polimondu raksturlielumi]({{ '/polyiamond_characteristics/' | relative_url }}).





