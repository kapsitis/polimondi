Par polimondiem
======================

Trijstūra režģa koordinātes
-------------------------------

Apzīmēsim sešas debesspuses kā sekojošus plaknes vektorus: 

$$A = (1,0),\; B = (1/2, \sqrt{3}/2),\; C = (-1/2, \sqrt{3}/2),$$

$$D = (-1,0),\; E = (-1/2, -\sqrt{3}/2),\; F = (1/2, -\sqrt{3}{2}).$$

Lai nebūtu jāstrādā ar daļskaitļiem un kvadrātsaknēm (un lai koordinātes 
neatšķirtos pēc režģa mērvienībām), ieviešam trijstūra režģa koordinātes 
kā trīs skaitļu komplektu sekojoši: 

$$A = (1,0,-1),\; B = (1,-1,0),\; C = (0,-1,1),\; D = (-1,0,1),\; E = (-1,1,0),\; F = (0,1,-1).$$

Šos vektorus var saskaitīt un pārvietoties pa trijstūra režģa punktiem - 
katram punktam šajā trijstūru režģī atbilst veselu skaitļu trijnieks $(x,y,z)$. 
Tā kā koordinātes joprojām apraksta plaknes punktus, tad šie trijnieki 
apmierina vienu un to pašu lineāro sakarību: $x+y+z = 0$.
(Katru punktu ar trim veselām koordinātēm, kam $x+y+z = 0$ var iezīmēt 
šajā trijstūru režģī).

![Bilde](images/triangle-coordinates.png)


Polimondu konstruēšana kanoniskā secībā
------------------------------------------

Lai būtu vieglāk salīdzināt divu polimondu pārlases algoritmu uzvedību, 
tos pārstaigājam vienmēr vienādā veidā: 

![Bilde2](images/move-iterator.png)

Ir spēkā trīs gadījumi (sk. zīmējumu): 

* Ja iepriekšējais gājiens bijis virzienā A vai D, tad nākamais var būt 
  virzienos C, B, E, F (šādā secībā). 
* Ja iepriekšējais gājiens bijis virzienā C vai F, tad nākamais var būt 
  virzienos virzienos D, B, A, E (šādā secībā). 
* Ja iepriekšējais gājiens bijis virzienā B vai E, tad nākamais var būt 
  virzienos virzienos D, C, A, F (šādā secībā).

Labus polimondus konstruē, vispirms veicot gājienu virzienā A par $N$ garuma vienībām, 
kur $N$ ir iepriekš uzdotais polimonda malu skaits.
Pēc tam veic otro gājienu (obligāti virzienos C vai B -- lai pirmais pagrieziens būtu 
pa kreisi). Ja pirmais pagrieziens būtu pa labi, tad aplūkojam polimonda 
spoguļattēlu (un ja pirmais gājiens nav virzienā A, tad polimondu pagriež tā, lai 
pirmais gājiens vienmēr būtu pa labi). 


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



Nezināmi jautājumi - 2
---------------------------

1. Aplūkojam kādu no $(2n)!$ permutācijām, kurās var izkārtot
   $2n+1$-stūra malu garumus (variantus, kas atšķiras tikai ar ciklisku permutāciju uzskatot par identiskiem). 
   Veidojam perfektus $2n+1$-polimondus, kuros malu garumi atbilst dotajai permutācijai. 
   Kurai no malu garumu permutācijām būs lielākais/mazākais skaits atbilstošo perfekto 
   polimondu? Vai perfektie+maģiskie polimondi, kur permutācija ir 
   tieši $1,2,\ldots,2n+1$, ir biežāk sastopami nekā nemaģiskie (vai viņu ir vairāk)?
2. Vai jebkurai malu garumu permutācijai eksistēs perfekts $(2n+1)$-polimonds, ja
   $2n+1 = 7, 9, 11, 13, \ldots$. 
3. Ar $P_n$ apzīmējam visu maģisko polimondu skaitu. (Piemēram, $P_5 = 1$, 
   $P_7 = 2$, $P_9 = 3$, $P_11 = 21$ utt.) Savukārt ar $L_n$ apzīmējam to
   slēgto lauzto līniju skaitu, kur malu garumi arī atbilst permutācijai 
   $1,2,\ldots,n$, bet līnija drīkst sevi krustot, vilkt pa to pašu līniju 
   vairākas reizes vai sakrist virsotnes (mūs interesē vienīgi, lai malu vektori
   būtu kādā no sešiem virzieniem un to summa būtu nulles vektors). 
   Vai eksistē galīga robeža $\lim_{n \rightarrow \infty} \frac{P_{2n+1}}{L_{2n+1}}$
4. Aplūkojam maģisku $(2n+1)$-polimondu un 
   divus debesspušu burtus ($X,Y \in \{A,B,C,D,E,F \}$), kuri varētu būt kandidāti, lai 
   veidotu "dvīņu polimondus" (pēc divu burtu iespraušanas debesspušu kodējumā no 
   maģiskā $(2n+1)$-polimonda varētu rasties maģisks $(2n+3)$-polimonds.
   Aplūkojam visas iespējamās vietas, kur dotajā maģiskajā $2n+1$-polimondā var iespraust šos $X,Y$ - tādā gadījumā 
   lauztā līnija, iespējams, nenoslēgsies. Atrast to punktu ģeometrisko vietu, kurā šī līnija var beigties? 
   Vai šī ģeometriskā vieta atkarīga no izvēlētā maģiskā $2n+1$ formas, vai arī - tikai no burtiem $X,Y$?
5. Uzdevums - ar vienkāršu lauztu līniju (bez posmu krustošanās), 
   kuras posmu garumi ir doti noteiktā secībā
   (piemēram, $1,2,\ldots,2n+1$) jānokļūst no trijstūru režģa punkta $A$ uz trijstūru režģa punktu $B$,
   pārvietojoties tikai pa režģa līnijām.
   Vai eksistē efektīvs algoritms, kurš nosaka, vai to var izdarīt? Vai arī šāds uzdevums ir NP-pilns (NP-complete)?
   Līdzīgs jautājums arī par kvadrātiņu režģi (varētu būt algoritmiski vieglāks).  
6. Pēc katra no polimondiem izmērāmiem parametriem (laukums, baricentra atrašanās vieta, dažādu iekšējo leņķu skaits)
   atrast "lielākos" un "mazākos" maģiskos polimondus - un noskaidrot, vai no tiem nevar izveidot kādu periodisku konstrukciju - 
   t.i. iegūt no viena optimāla polimonda nākamo ar kaut kādu induktīvo soli (2,4,6,utt.)
7. Vai polimondu skaits $P_{2n+1}$ stingri aug, ja $n$ aug?
8. Vai eksistē sakarība, kas ļauj pēc maģiska polimonda iekšējo leņķu skaita (cik tur ir 60, 120, 240 vai 300 grādu leņķi) 
   noteikt, kādas vērtības var pieņemt polimonda laukums?
9. Kurām $n$ vērtībām eksistē maģiski $(2n+1)$-polimondi, kuros ir tikai $60$ vai $300$ leņķi?
   Maģisks $9$-polimonds ar šo īpašību redzams zīmējumā.    
   ![Bilde](images/polimonds-9.png)
10. Vai eksistē bezgalīga maģisku polimondu virkne, kuru debesspušu kodējumā 
    apraksta ar bezkonteksta gramatiku (*context-free grammar*)?
11. Aplūkojam regulāru sešstūri ar malas garumu $55$ (to var uzskatīt par "riņķi" trijstūru režģa metrikā ar rādiusu $55$). 
    Šis sešstūris satur visus tos punktus, kam pietiktu ar $10$ gājieniem garumā $10,9,8,\ldots,1$, lai atgrieztos sešstūra centrā). 
    No visiem sešstūra iekšpusē un uz perimetra esošajiem punktiem atzīmējam tos, no kuriem tiešām var atgriezties centrā.
    Kādu daļu no visiem punktiem esam atzīmējuši? Kas notiek ar atzīmēto punktu proporciju, ja malu skaitu ($k = 10$) palielina
    līdz $11, 12,\ldots$? 
12. Vai kādai no perfekto/maģisko polimondu pasaulē esošajām skaitļu virknēm varam atrast "ģenerējošo funkciju" (pakāpju rindas summu, kuras koeficienti 
    ir attiecīgās virknes locekļi)? Sk. [Generating functions](https://cse.iitkgp.ac.in/~animeshm/generating_funct.pdf).
    
    
