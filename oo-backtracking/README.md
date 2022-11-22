Par polimondiem
======================

**Definīcija:** Par $n$-*polimondu* sauc vienkāršu slēgtu lauztu līniju (jeb daudzstūri) no $n$ posmiem, 
kam visas virsotnes atrodas trijstūru režģa virsotnēs, bet malas iet pa trijstūru režģa līnijām. 

**Definīcija:** $n$-polimondu sauc par *labu*, ja tā malu garumi, sākot skaitīt no kādas virsotnes, 
ir skaitļi $n,n-1,n-2,\ldots,3,2,1$ tieši šādā secībā.

**Definīcija:** $n$-polimonda *kodējums ar debesspusēm* ir virknīte garumā $n$, kura 
sastāv no 6 burtiem (`A`,`B`,`C`,`D`,`E`,`F`), kas norāda uz malu virzieniem, kuros tiek vilktas secīgas
polimonda malas. (Labiem polimondiem malu garumi ir secībā  $n,n-1,n-2,\ldots,3,2,1$, 
bet citiem polimondiem kopā ar debespusi kodējumā norāda arī attiecīgās malas garumu.)

**Definīcija:** Polimondu virkni garumā $k$, kas satur polimondus ar 
$n, n+2, \ldots, n+2(k-1)$ malām sauc par *labu polimondu virkni
ar indukcijas soli 2*, ja 
katriem diviem blakusesošiem polimondiem (ar $n+2i$ un $n+2i+2$ malām, $i = 0,\ldots,k-2$) 
to debesspušu kodējumi sakrīt, izņemot to, ka polimonda ar $n+2i+2$ malām 
kodējumā ir iesprausti divi jauni debesspušu burti (jebkurās divās vietās).  
Līdzīgi definē arī labu polimondu virknes ar indukcijas soli $4, 6, 8$ utml. 

(Vai polimondu virknē malu iespraušanai jānotiek pēc kādas regulāras shēmas, piemēram, 
debesspušu kodējumiem jābūt ģenerējamiem ar *bezkonteksta gramatiku* vai ar 
vienkāršāku metodi - periodisku apakšvirkņu ievietošanu divās kodējuma vietās, vēl neesam izlēmuši.)

**Definīcija:** Par polimonda laukumu sauc veselu skaitli - tajā ietilpstošo mazo trijstūrīšu skaitu. 

**Definīcija:** Par polimonda gabarītizmēriem sauc naturālu skaitļu trijnieku $(i,j,k)$, kur 
* $i$ izsaka mazāko attālumu starp divām horizontālām taisnēm trijstūra režģī tādām, 
  ka visas polimonda virsotnes atrodas starp šīm taisnēm (vai uz tām). 
* $j$ izsaka mazāko attālumu starp divām paralēlām slīpām taisnēm (kas vilktas no ziemeļaustrumiem uz dienvidrietumiem) tādām, 
  ka visas polimonda virsotnes atrodas starp šīm taisnēm (vai uz tām). 
* $k$ izsaka mazāko attālumu starp divām paralēlām slīpām taisnēm (kas vilktas no ziemeļrietumiem uz dienvidaustrumiem) tādām, 
  ka visas polimonda virsotnes atrodas starp šīm taisnēm (vai uz tām). 


**Definīcija:** Par $2n+1$ polimonda *relatīvo kodējumu* sauc $2n$-burtu virknīti, kas
sastāv no 4 burtiem (`a`,`b`,`c`,`d`). Pirmo malu novelk jebkurā izvēlētā virzienā (parasti - taisni pa labi), 
šai malai kodējumā neviens burts neatbilst. Turpmākos burtus iegūst sekojoši:

* burtu "a" raksta kodējumā tad, ja nākamā mala pret iepriekšējo veic asu/šaurleņķa pagriezienu pa kreisi ($60^{\circ}$ leņķis); 
* burtu "b" raksta kodējumā tad, ja nākamā mala pret iepriekšējo veic platleņķa pagriezienu pa kreisi ($120^{\circ}$ leņķis); 
* burtu "c" raksta kodējumā tad, ja nākamā mala pret iepriekšējo veic platleņķa pagriezienu pa labi ($120^{\circ}$ leņķis); 
* burtu "d" raksta kodējumā tad, ja nākamā mala pret iepriekšējo veic asu/šaurleņķa pagriezienu pa labi ($60^{\circ}$ grādu leņķis). 

Labiem polimondiem pieņemam, ka malu garumi ir secībā  $n,n-1,n-2,\ldots,3,2,1$, 
bet citiem polimondiem kopā ar relatīvo virzienu (a,b,c,d) norāda arī attiecīgās malas garumu.


**Definīcija:** Polimonds ir *divdaļīgs*, ja eksistē kāda diagonāle, kura pilnībā atrodas šī polimonda iekšpusē un 
visi augstumi, kurus novelk no polimonda virsotnēm uz šo diagonāli arī pilnībā atrodas polimonda iekšpusē. 
(Vienkāršoti sakot, polimondam ir koka lapas forma ar centrālo dzīslu, no kuras var novilkt perpendikulus uz jebkuru vietu uz 
lapas perimetra.)



Nezināmi jautājumi
---------------------------

1. Vai katrai $n$ vērtībai eksistē labs $2n+1$-polimonds? 
2. Vai katrai naturālu skaitļu $1,2,\ldots,2n+1$  permutācijai (virknei, kura satur katru no šiem 
   skaitļiem tieši vienu reizi) eksistē polimonds, kurā malu garumu secība atbilst šai permutācijai? 
3. Kādas vērtības var pieņemt laba $2n+1$-polimonda laukums?
4. Kādas vērtības var pieņemt $2n+1$-polimonda laukums, ja starp tā malām katrs garums $1,2,\ldots,2n+1$ sastopams 
   tieši vienu reizi (bet ne obligāti dilstošā secībā)?
5. Kādos punktos var atrasties laba $2n+1$-polimonda baricentrs (smaguma centrs)?
   Smaguma centru var definēt vai nu kā polimonda virsotņu koordinātu aritmētisko vidējo, vai polimonda perimetra punktu 
   (ar veselām trijstūra režģa koordinātēm) aritmētisko vidējo, vai arī visu tajā ietilpstošo mazo trijstūrīšu centru aritmētisko vidējo. 
6. Kādu vislielāko un vismazāko vērtību var pieņemt laba $2n+1$-polimonda gabarīts vienalga kādā no trim virzieniem?
7. Kādas vērtības var pieņemt gabarītu trijnieks $(i,j,k)$ labam $2n+1$-polimondam. 
8. Kāds mazākais aso jeb šaurleņķa pagriezienu skaits var būt labam $2n+1$-polimondam (t.i. mazākais skaits ar burtiem "a", "d" 
   šī polimonda relatīvajā kodējumā). 
9. Kāds ir lielākais un mazākais laukums laba $2n+1$ polimonda izliektajai čaulai (mazākajam izliektajam daudzstūrim, kurš 
   satur šo polimondu)? 
10. Kāds var būt lielākais un mazākais malas garums regulāram minimālajam sešstūrim, kurš pilnībā satur savā iekšpusē 
   $2n+1$ polimondu? 



Backtracking un DFS uzdevumi
--------------------------------

Te var apkopot dažus derīgus jautājumus, kas risināmi ar kādu mēģinājumu/kļūdu metodi, piemēram, pielāgojot 
esošo universālo "backtracking" algoritmu. 

1. Pieņemsim, ka plaknes punktā ar trijstūra režģu koordinātēm $(x,y,z)$ no kādas debesspuses (A,B,C,D,E, vai F) 
   nonākusi lauzta līnija. Pieņemsim, ka to turpina kā vienkāršu lauztu līniju, izmantojot malu garumus $k,k-1,\ldots,1$. 
   Kurās vietās var nonākt šī lauztā līnija pēc visu $k$ posmu uzzīmēšanas? (Atbildes norādīt kā relatīvos pārvietojumus trijstūra 
   režģu koordinātēs.)   
   (Šo uzdevumu var izmantot, lai paātrināti atrastu labos polimondus ar pietiekami lielu malu garumu -- 
   ja izrādās, ka ar pēdējiem $k$ posmiem nevarēs veikt vajadzīgo pārvietojumu (pat neņemot vērā iespējamos konfliktus
   ar agrāk novilktajām malām), tad attiecīgo apakškoku neaplūko.)
2. Dots labs $(2n+1)$-polimonds ar debesspušu kodējumu. Atrast visus veidus, kuros to var turpināt, ievietojot debespušu kodējumā 
   $2$ vai $4$ jaunas malas/debesspuses?
3. Skaitīt tikai tos labos polimondus, kuri apmierina kādu ierobežojumu. Piemēram, ar noteiktu laukumu, ar fiksētu/nelielu skaitu 
   pagriezienu pa šauru/asu leņķi vai citu īpašību, kas ļautu vieglāk tos pēc tam analizēt - piemēram, pamatot, ka induktīvais 
   solis (divu jaunu malu pievienošana) allaž noved pie derīga polimonda, kam nav malu krustošanās.

