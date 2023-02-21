# Par polimondiem


## Trijstūra režģa koordinātes

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


## Polimondu konstruēšana kanoniskā secībā

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



## Atklāti jautājumi 

### Polimondu eksistence un skaits


1. Vai katrai $n$ vērtībai eksistē maģisks $2n+1$-polimonds?  
   **Atbilde:** Gandrīz noteikti atbilde ir "Jā". Induktīvās konstrukcijas $4n+1 \rightarrow (4n+1) + 4$ un 
   $4n+3 \rightarrow (4n+1)+4$ ir atrodamas direktorijā "konstrukcijas", bet pagaidām vēl nav vienkāršu pierādījumu,
   ka šīs lauztās līnijas sevi nekrusto.
2. Vai katrai naturālu skaitļu $1,2,\ldots,2n+1$  permutācijai 
   eksistē perfekts polimonds, kurā malu garumu secība atbilst šai permutācijai, bet malu virzieni var būt jebkādi? 
3. Aplūkojam kādu no $(2n)!$ permutācijām, kurās var izkārtot
   $2n+1$-stūra malu garumus (variantus, kas atšķiras tikai ar ciklisku permutāciju uzskatot par identiskiem). 
   Kurai no malu garumu permutācijām būs lielākais/mazākais skaits tai atbilstošo perfekto 
   polimondu? Vai maģiskie polimondi, kuros izmantota *identiskā permutācija*  
   (tieši malu garumu virknīte $1,2,\ldots,2n+1$), ir biežāk sastopami nekā polimondi ar citām malu garumu permutācijām?
4. Ar $M_{2n+1}$ apzīmējam visu maģisko $2n+1$-polimondu skaitu.  
   Piemēram, $M_{5} = 1$, 
   $M_{7} = 2$, $M_{9} = 3$, $M_{11} = 21$ utt.  
   Ar $L_{n}$ apzīmējam to
   slēgto lauzto līniju skaitu, kur malu garumi arī atbilst permutācijai 
   $1,2,\ldots,n$, kura katrā virsotnē maina virzienu,  bet šī līnija drīkst sevi krustot, vilkt pa to pašu līniju 
   vairākas reizes vai sakrist virsotnes.  
   Vai eksistē galīga robeža:
   ${\displaystyle \lim_{n \rightarrow \infty} \frac{M_{2n+1}}{L_{2n+1}}?}$  
   Vai šī robeža atškiras no robežas:
   ${\displaystyle \lim_{n \rightarrow \infty} \frac{M_{2n}}{L_{2n}}?}$  
   (Citiem vārdiem - vai nepāra maģiskie polimondi ir "retāk sastopami" nekā pāra maģiskie polimondi?). 
   **Hipotēze:** Abas robežas, visticamāk, ir $0$ - sevis krustošana ir ļoti biežs iemesls polimonda "izbrāķēšanai" algoritmos arī maziem $n$. 
   No otras puses, atļaujot gan pāra, gan nepāra malu skaitu, virkne $M_5, M_6, M_7, M_8\ldots$ varētu nebūt monotoni augoša, bet virkne 
   $L_5, L_6, L_7, L8\ldots$, visticamāk ir augoša.
5. Vai virkne $M_{2n+1}$ (maģisko $2n+1$-polimondu skaits) stingri aug, ja $n$ aug?
6. Vai kādai no perfekto/maģisko polimondu pasaulē esošajām skaitļu virknēm varam atrast "ģenerējošo funkciju" 
   (pakāpju rindas summu, kuras koeficienti 
   ir attiecīgās virknes locekļi)? Sk. [Generating functions](https://cse.iitkgp.ac.in/~animeshm/generating_funct.pdf).
7. Atrast ģenerējošo funkciju virknei $L_n$ (visām slēgtajām lauztajām līnijām ar posmu garumiem 
   $n,n-1,\ldots,1$ ieskaitot tās, kuras sevi krusto). 


### Polimondu induktīva ģenerēšana

1. Kuriem naturāliem $C$ eksistē bezgalīga maģisku $n$ polimondu virkne, kuru debesspušu kodējumā 
   var uzģenerēt ar bezkonteksta gramatiku (*context-free grammar*), kuras produkcijās katrā solī 
   pievieno ne vairāk kā $C$ jaunus simbolus?  
   **Atbilde:** Induktīvās konstrukcijas parāda, ka var izvēlēties $C=4$ un $C=8$. 
   Par $C=2$ vai $C=6$ attiecīgās konstrukcijas nav zināmas.
2. Vai eksistē konstante $C$ un bezgalīgi daudzi polimondi, kuriem debesspušu kodējums 
   veido periodisku virkni, kura vismaz divreiz atkārtojas (un vēl ne vairāk kā $C$ simboli pirms vai pēc šiem periodiem)? 
3. Vai eksistē bezgalīga maģisku polimondu virkne, kurā malu skaits aug kā ģeometriskā progresijā, 
   bet malu virzienus (A,B,C,D,E,F) 
   var ģenerēt ar [Lindenmaiera sistēmu](https://en.wikipedia.org/wiki/L-system). 
   Piemēram, vai varētu būt šaurleņķu polimondi ar malu skaitu $n = 9, 27, 81, \ldots$, kur katra 
   nākamā polimonda virzienu virknīti var iegūt, pēc kaut kādiem likumiem pārrakstot jeb aizvietojot 
   iepriekšējā polimonda virzienu virknīti?
4. $2n+1$-polimondu $P_1$ un $2n+3$-polimondu $P_2$ saucam par *dvīņu polimondiem*, ja 
   $P_2$ debespušu kodējumu var iegūt, iespraužot $P_1$ debespušu kodējumā divus jaunus virzienu burtus. 
   Vai eksistē bezgalīgi daudzi dvīņu polimondu pāri? Vai eksistē cik patīk garas virknes, kurās 
   katri divi blakusesoši locekļi ir dvīņu polimondi? 



### Polimondu laukumi 

1. Kādas vērtības var (vai noteikti nevar) pieņemt maģiska $2n+1$-polimonda laukums?
2. Kādas vērtības var (vai noteikti nevar) pieņemt perfekta $2n+1$-polimonda laukums?
3. Cik pavisam ir perfektu (maģisku?) polimondu ar doto laukumu? 
4. Kāds ir lielākais un mazākais laukums maģiska $2n+1$ polimonda izliektajai čaulai (mazākajam izliektajam daudzstūrim, kurš 
   satur šo polimondu - tā malas var neiet pa trijstūru režģa līnijām)? 
5. Kāds var būt lielākais un mazākais malas garums regulāram minimālajam sešstūrim, kurš pilnībā satur savā iekšpusē 
   $2n+1$ polimondu?
6. Vai eksistē sakarība, kas ļauj pēc maģiska polimonda iekšējo leņķu skaita (cik tur ir 60, 120, 240 vai 300 grādu leņķi) 
   noteikt, kādas vērtības var pieņemt polimonda laukums?
7. Vai eksistē sakarība, kas ļauj atrast polimonda laukumu, ja zināms režģa punktu skaits 
   uz maģiska polimonda perimetra (parametrs $b$) un  
   trijstūru režģa punktu skaits šī polimonda iekšpusē (parametrs $i$). 
   Sal.  [Pīka formula](https://en.wikipedia.org/wiki/Pick%27s_theorem).
    

### Dažādi ģeometriski raksturlielumi

1. Kādos punktos var atrasties maģiska (pefekta?) $2n+1$-polimonda baricentrs (smaguma centrs)? 
   Kāda ir visu iespējamo baricentru ģeometriskā vieta, ja tos paralēli pārnes tā paša mazā trijstūrīša iekšpusē. 
   (Smaguma centru definē kā visu polimondā ietilpstošo mazo trijstūrīšu centru koordinātu aritmētisko vidējo.)
2. Kādu vislielāko un vismazāko vērtību var pieņemt laba $2n+1$-polimonda gabarīts vienalga kādā no trim virzieniem?
   Kādas vērtības var pieņemt gabarītu trijnieks $(i,j,k)$ maģiskam (perfektam?) $2n+1$-polimondam. 
3. Kāds mazākais šauro leņķu (a60 un a300) skaits var būt maģiskam $2n+1$-polimondam (par šauriem uzskatām arī 300 grādu 
   leņķus, kuros polimonds ir ieliekts).   
   **Hipotēze:** Pietiekami lielām $n$ vērtībām šauro leņķu skaits $2n+1$-polimondā ir skaitlis intervālā $[1;2n-1]$ 
   vai intervālā $[1; 2n+1]$ (šajā gadījumā visi leņķi būs šauri). 
4. Kurām $n$ vērtībām eksistē maģiski $(2n+1)$-polimondi, kuros ir tikai $60$ vai $300$ leņķi?
   Maģisks $9$-polimonds ar šo īpašību redzams zīmējumā.    
   ![Bilde](images/polimonds-9.png)  
   **Atbilde:** Līdz šim atrastās vērtības ir $n=9$, $n=27$, $n=29$. 
5. Bezgalīgā trijstūru režģa trijstūrīšus izkrāso 2 krāsās (paritātes krāsojums). Atrast, cik dažādu 
   krāsu trijstūrīšu var atrasties perfekta (maģiska) polimonda iekšpusē. Kurām $n$ vērtībām atrodas 
   maģiski $n$-polimondi, kurus var sagriezt rombiņos, kurus veido divi mazie trijstūrīši 
   (t.i. melno un balto trijstūrīšu skaits ir līdzsvarā). 


### Citi jautājumi

1. Uzdevums - ar vienkāršu lauztu līniju (bez posmu krustošanās), 
   kuras posmu garumi ir doti noteiktā secībā
   (piemēram, $1,2,\ldots,2n+1$) jānokļūst no trijstūru režģa punkta $A$ uz trijstūru režģa punktu $B$,
   pārvietojoties tikai pa režģa līnijām.  
   Vai eksistē efektīvs algoritms, kurš nosaka, vai to var izdarīt? Vai arī šāds uzdevums ir NP-pilns (NP-complete)?
   Līdzīgs jautājums arī par kvadrātiņu režģi (varētu būt algoritmiski vieglāks).  
2. Aplūkojam regulāru sešstūri ar malas garumu $55$ (to var uzskatīt par "riņķi" trijstūru režģa metrikā ar rādiusu $55$). 
   Šis sešstūris satur visus tos punktus, kam pietiktu ar $10$ gājieniem garumā $10,9,8,\ldots,1$, lai atgrieztos sešstūra centrā). 
   No visiem sešstūra iekšpusē un uz perimetra esošajiem punktiem atzīmējam tos, no kuriem tiešām var atgriezties centrā.
   Kādu daļu no visiem punktiem esam atzīmējuši? Kas notiek ar atzīmēto punktu proporciju, ja malu skaitu ($k = 10$) palielina?











![Bilde](images/ChatGPT-advice.png)
