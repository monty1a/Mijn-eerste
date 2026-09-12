# Centralisatie Smarthome & Netwerkinfrastructuur

**Traject:** Meterkast &harr; Huiskamer &harr; Zolder
**Status:** ontwerp — nog niet uitvoeringsgereed (zie §5 en §8)
**Laatst bijgewerkt:** 12 september 2026

> Dit bestand bevat in §1–§4 de projectdocumentatie en materiaallijst zoals
> aangeleverd (§3.3 voegt de verificatie van de vloerconstructie tegen de
> originele bouwstukken toe), en in §5–§8 een kritische review met blokkerende
> punten, ontbrekende posten en een actielijst. **Niet boren voordat §8 is
> afgewerkt** — een verkeerd gat in de vloer is niet terug te draaien.
>
> **Woning:** Kruidenschans 24, Voorhout (type M4, 1986). Bewoond door Pamela;
> de verbouwing volgt over minimaal twee jaar. Zie §6.19 en §6.20 — dat verschil
> tussen bewoner en beheerder is maatgevend voor het ontwerp.

---

## 1. Projectdoel

Het realiseren van een centrale smarthome- en netwerkhub in de meterkast,
gecombineerd met een sub-hub in de huiskamer en een vaste lijn naar zolder. De
infrastructuur wordt fysiek beschermd tegen vocht en ongedierte via een
mantelbuis door de kruipruimte.

---

## 2. Netwerkarchitectuur & protocol-integratie

* **Topologie:** stertopologie vanuit de hoofdswitch in de meterkast.
* **Meterkast hub:**
  * **Server:** HP T630 Mini-PC met Home Assistant OS (vast IP `.21`).
  * **Hoofdswitch:** GigaPlus 10-Port 2.5Gb Switch (8x 2.5G PoE, 2x 10G SFP+)
    op een eigen dedicated B16 aardlekautomaatgroep.
* **Woonkamer sub-hub:**
  * **Switch:** TP-Link TL-SG108PE 8-Port Gigabit PoE Switch.
  * **Zigbee / Thread:** SMLIGHT SLZB-06M PoE Ethernet Coordinator, direct
    aangesloten op de PoE-switch in de woonkamer (verzorgt lokaal bereik voor
    Home Assistant).
* **Bekabeling:**
  * **Huiskamer:** 2x S/FTP Cat6a Outdoor PE netwerkkabel (1x hoofdverbinding,
    1x reserve/extra punt) + 1x Belden H125 PE Outdoor coaxkabel.
  * **Zolder:** 1x S/FTP Cat6a Outdoor PE netwerkkabel (25 m).

> ⚠️ **Openstaand in deze architectuur:** het internet-aansluitpunt (modem/ONT),
> de router, DHCP-autoriteit en gateway zijn niet benoemd, en de voeding van de
> woonkamerswitch is onjuist aangenomen. Zie §5.1 en §5.2.

---

## 3. Bouwkundige specificaties & vloerdoorgang

### 3.1 Begane grond vloerconstructie

* **Vloertype:** Manta systeemvloer (geïsoleerde ribbenvloer, totale dikte
  255 mm, betonkwaliteit B 37,5).
* **Vloeropbouw:** parallel lopende betonribben (600 mm h.o.h.) met daartussen
  pasplaten/vulelementen van piepschuim/bimsbeton en een dekvloer van ca.
  3–5 cm.

> ✅ **Geverifieerd tegen de originele bouwstukken (1986).** Alle opgegeven
> waarden kloppen. Zie §3.3 voor de brongegevens en de constructieve
> randvoorwaarde die daaruit volgt.

### 3.3 Verificatie vloerconstructie tegen de originele stukken

Nageslagen in `huizen/Voorhout-Kruidenschans-24/` (BSF BV / bouwkundig
adviesburo H.C. Bogaards, werk 1341 R2B, 19 woningen plan Oosthout B1 te
Voorhout, Noorlander Bouw, dec. 1985 – feb. 1986):

| Opgegeven in §3.1 | Bron | Uitkomst |
|---|---|---|
| Manta systeemvloer, begane grond | `funderingsplan_vloer.pdf`, titelblok: *"„MANTA" systeemvloer voor de begane grond, woningtype M4"* | ✅ bevestigd, en expliciet voor **type M4** |
| Totale dikte 255 mm | `berekening_belastingen_pasplaat.pdf` blad 1 (*"ht 255 mm"*) en blad 3 (breukmomententabel met kolom ht = 255 mm) | ✅ bevestigd |
| Betonkwaliteit B 37,5 | `funderingsplan_vloer.pdf` titelblok en `…pasplaat.pdf` blad 3: *"Beton: B 37,5, f'b 30 N/mm²"*; wapening FeB 500 | ✅ bevestigd |
| Ribben 600 mm h.o.h. | `…pasplaat.pdf` blad 3: *"Breedte per rib = 600 mm"* | ✅ bevestigd |
| Pasplaten tussen de ribben | `…pasplaat.pdf`: Manta pasplaat-berekening; doorsnede op het funderingsplan | ✅ bevestigd |

**De tegenspraak met het dossier bestaat niet.** De repo-README noemt
"breedplaatvloeren (filigraan)"; dat klopt voor de **verdiepings- en
zoldervloer** (`berekening_vloerplaten_filigraan.pdf`, 53 blz., "FILIGRANPLATEN
… type M4", 16-5-1986). De **begane grondvloer** is een Manta ribbenvloer.
Beide zijn waar; de README was onvolledig, niet onjuist.

**Twee aanvullende gegevens van de tekening die het plan raken:**

1. **"GEEN SPARING IN RIB"** — handgeschreven bij de vloerdoorsnede op het
   funderingsplan. De constructeur heeft in 1986 dus expliciet vastgelegd dat er
   geen doorvoeren in de rib mogen. Ribben vermijden is daarmee geen voorzorg
   maar een constructieve eis. Boren in een rib snijdt de hoofdwapening van het
   dragende element door.
2. **"Betonnokken in isolatie onder rib, max. 150 cm h.o.h., niet t.p.v.
   opleg"** — onder de ribben zitten extra betonnokken. Die zitten *onder de
   rib*, dus wie tussen de ribben blijft, mijdt ze automatisch. Wel relevant bij
   inspectie van onderaf: een nok is geen rib.

**Ribrichting (afgeleid, te controleren bij inspectie).** Op de legtekening
liggen de vloerplaten als banden van ca. 120 cm breed, overspannend ca. 580 cm
tussen de woningscheidende wanden. De ribben lopen dus in de overspanningsrichting
— **haaks op de woningscheidende wanden, parallel aan voor- en achtergevel** — en
de hart-op-hart-afstand van 600 mm ligt in de richting voor-naar-achter.

*Praktisch gevolg voor §3.2 stap 2:* zoek de ribvrije zone door je proefboringen
**in een lijn van voor naar achter** te verschuiven (haaks op de gevel), niet
zijwaarts. Zijwaarts schuiven volgt de rib en levert steeds dezelfde weerstand.

> ⚠️ Let op bij het uitzetten: het blad vermeldt *"2x uitvoeren (getekend), 2x
> uitvoeren (gespiegeld)"*. Of Kruidenschans 24 de getekende of de gespiegelde
> variant is, bepaalt de maatvoering — en #24 is een **hoekwoning**, dus de
> aansluiting aan de vrijstaande kopgevel wijkt af van het middenblok op de
> tekening. Zet de tekening uit tegen de werkelijke woning voordat je aftekent.

### 3.2 Boor- en installatieprocedure (stapsgewijs)

1. **Afwerkvloer / laminaat:** met een 60 mm bi-metaal gatenzaag een ruim gat in
   het laminaat zagen t.b.v. de werking/uitzetting van de houten vloer.
2. **Proefboring (ribben vermijden):** met een lange 6 mm steenboor door de
   dekvloer prikken. Bij zachte weerstand zit je tussen de betonribben (in de
   pasplaat/isolatie). Bij keiharde weerstand stop je en schuif je 7–10 cm haaks
   op.
3. **Betonboorgat:** met een 52 mm diamant boorkroonset (nuttige lengte 200 mm,
   SDS-Plus aansluiting) op de Makita boormachine (**uitsluitend roterend boren,
   klopstand UIT**) door de dekvloer boren tot doorbraak.
4. **Buisborging:** rode dubbelwandige PE-mantelbuis (50 mm) door het gat
   steken. Vlak boven de vloer borgen met een 50 mm RVS slangklem om wegzakken
   in de kruipruimte te voorkomen.
5. **Kabeldoorvoer:** 2x Cat6a Outdoor netwerkkabel + 1x Belden H125 coax via de
   geïntegreerde trekdraad door de mantelbuis trekken.
6. **Afdichting & afwerking:** binnenzijde buis afdichten met Filoform
   afdichtingspasta tegen tocht en bodemgassen; ringspleet tussen buis en beton
   eveneens afdichten. Het gat in het laminaat afdekken met een 50 mm
   afdekrozet.

> ⚠️ **Twee correcties t.o.v. het oorspronkelijke plan, bewust doorgevoerd:**
> stap 3 luidde "in één beweging 20 cm diep boren" (inconsistent met de eigen
> vloeropbouw — zie §5.4) en stap 5 ging uit van vooraf gemonteerde,
> aan elkaar getapete RJ45-stekkers (zie §6.9). Stap 6 dichtte alleen de
> binnenzijde van de buis af (§6.15).

---

## 4. Materiaaloverzicht & bestellinks

| Apparaat / component | Type / specificatie | Prijs | Bestellink |
| :--- | :--- | :--- | :--- |
| **Meterkast groep** | ABB aardlekautomaat B16 (DS201 B16) | € 49,90 | [Amazon](https://amzn.eu/d/036ACNSG) |
| **Hoofdswitch meterkast** | GigaPlus 10-Port 2.5Gb Switch (8x 2.5G PoE, 2x 10G SFP+) | € 69,99 | [Amazon](https://amzn.eu/d/09yBrpMB) |
| **Home Assistant server** | HP T630 Mini-PC (8 GB RAM, 128 GB SSD + HA OS) | € 64,95 | [Marktplaats](https://link.marktplaats.nl/m2438138358) |
| **PoE switch woonkamer** | TP-Link TL-SG108PE 8-Port Gigabit (4x PoE) | € 59,90 | [Amazon](https://amzn.eu/d/03xGOamO) |
| **Zigbee/Thread antenne** | SMLIGHT SLZB-06M (PoE Ethernet Coordinator) | € 39,95 | [SMLIGHT](https://smlight.tech/product/slzb-06m/) |
| **Coaxkabel kruipruimte** | Belden H125 PE zwart (20 m x € 1,99) | € 39,80 | [Onlinekabelshop](https://www.onlinekabelshop.nl/) |
| **Coax connectoren** | Technetix IECMF-A+ haakse schroefset | € 11,99 | [Onlinekabelshop](https://www.onlinekabelshop.nl/) |
| **Netwerkkabels woonkamer** | S/FTP Cat6a Outdoor PE zwart (2x 20 m) | € 50,00 | [Onlinekabelshop](https://www.onlinekabelshop.nl/) |
| **Netwerkkabel zolder** | S/FTP Cat6a Outdoor PE zwart (1x 25 m) | € 25,00 | [Onlinekabelshop](https://www.onlinekabelshop.nl/) |
| **Mantelbuis kruipruimte** | Rode dubbelwandige PE mantelbuis 50 mm (25 m + trekdraad) | € 35,00 | [Irritech](https://share.google/qzXlrR28Nto8fhTGg) |
| **Betonboor vloer** | Diamant boorkroonset 52 mm (200 mm diep + SDS-Plus adapter) | € 49,25 | [Amazon](https://www.amazon.nl/s?k=SDS+Plus+Diamant+Dozenboor+52mm) |
| **Laminaat gatenzaag** | Bi-metaal gatenzaag 60 mm + SDS/Hex adapter | € 10,00 | [Amazon](https://www.amazon.nl/s?k=Bi-metaal+gatenzaag+60mm) |
| **Montagemateriaal** | Filoform afdichtingspasta, RVS slangklem 50 mm, 50 mm afdekrozet | € 15,00 | Bouwmarkt (Toolstation / Gamma) |
| **Subtotaal materiaallijst** | | **€ 520,73** | |

> 📐 **Rekencorrectie:** de aangeleverde lijst vermeldde € 519,73. De posten
> tellen op tot **€ 520,73** (verschil € 1,00). Voor het realistische
> projectbudget inclusief ontbrekende posten: zie §7.

---

## 5. Blokkerende punten

Deze vier moeten opgelost zijn voordat er materiaal wordt besteld of geboord
wordt. Elk punt laat het plan in de huidige vorm falen. Een vijfde punt — het
vloertype — is inmiddels **opgelost**; zie §5.5.

### 5.1 Er zit geen router in de architectuur

De hele §2 beschrijft switches, maar niet waar het internet binnenkomt, welk
apparaat gateway en DHCP-server is, of welk subnet er gebruikt wordt — terwijl
er wel een vast IP `.21` wordt uitgedeeld. Een stertopologie is pas een
topologie als je weet waar de bron staat.

**Doorslaggevend:** staat het modem/de ONT in de woonkamer (in NL heel gewoon —
coax- of glasintrede zit vaak bij de TV-wand), dan is de meterkast niet het
hart van de ster maar een aftakking, en loopt al je verkeer twee keer door de
vloerdoorvoer. Dat is geen ramp, maar het verandert de bekabelingsbehoefte
(je hebt dan minimaal één kabel als uplink *naar* de meterkast nodig, en de
2,5G-switch staat aan de verkeerde kant van de bottleneck).

**Oplossing:** vóór alles vastleggen (a) fysieke locatie van de WAN-intrede,
(b) welk apparaat routert/firewall't, (c) IP-plan (subnet, gateway, DHCP-range,
reserveringen). Als de intrede in de woonkamer zit: overweeg de 2,5G-switch en
de router daar te plaatsen en de meterkast als sub-hub te behandelen, of
verplaats de intrede (bij glas kan de ONT vaak verhuizen, bij coax kun je met
de bestaande coax het modem naar de meterkast halen).

**Let bij (c) specifiek op de DHCP-pool.** Een handmatig ingesteld vast IP dat
binnen het uitgiftebereik van de router valt, levert een IP-conflict op zodra de
router datzelfde adres aan een ander apparaat uitdeelt. Dat gebeurt niet tijdens
de installatie maar weken later, na een herstart of bij een nieuw apparaat — op
precies het apparaat waar je hele smarthome op leunt. Veel consumentenrouters
beginnen hun pool laag (bij AVM/Fritz!Box standaard op `.20`), dus een `.21`
zit daar al in. **Doen:** het adres reserveren op MAC-adres in de router (DHCP
blijft dan de autoriteit), of de pool verkleinen en statische adressen
daarbuiten leggen. Regel dit vóór de HA-installatie, niet erna.

### 5.2 De TL-SG108PE kan niet via PoE gevoed worden

§2 noemt een "PoE-gevoede sub-hub in de huiskamer". De TL-SG108PE is een
PoE-**leverende** switch (4 poorten PoE-out) met een eigen externe
voedingsadapter — er is geen PoE-in. De sub-hub heeft dus **230 V op de
switchlocatie** nodig, en dat staat nergens in het plan of de materiaallijst.

**Oplossing, kies één:**
1. Accepteer netvoeding: leg een wandcontactdoos vast op de switchlocatie
   (kosten laag, betrouwbaarheid het hoogst). Voorkeur.
2. Wil je écht één kabel: gebruik een switch die zelf PoE-powered is en PoE
   doorgeeft (bijv. Ubiquiti USW-Flex — verifieer PoE-in/out en budget vóór
   aanschaf). Reken dan door of het PoE-budget van de hoofdswitch de
   sub-switch **plus** de SLZB-06M draagt (zie §5 en §6.11).
3. Zet de SLZB-06M rechtstreeks op een PoE-poort van de hoofdswitch via de
   reservekabel, en laat de sub-switch vervallen. Simpelste architectuur —
   maar dan verlies je poorten in de woonkamer.

### 5.3 50 mm buis door een 52 mm gat gaat niet passen

Dat is 1 mm speling per zijde, over 200 mm ruw gekerntboord beton, met een
**dubbelwandige geribbelde** buis waarvan de ribbels de maatgevende diameter
zijn. Zodra het gat ook maar één graad scheef staat — en dat staat het, je boort
handmatig door dekvloer in isolatie — klemt de buis halverwege. Dit is de
duurste fout in het plan, omdat het gat onomkeerbaar is en een tweede gat een
tweede ribzoekactie betekent.

**Oplossing, kies één:**
* **Kroon vergroten naar 68 mm** (ruime, foutvergevende maat voor 50 mm buis).
  Let op: bredere kroon = meer koppel en meer kans op wapening raken.
* **Buis verkleinen naar 40 mm** in het 52 mm gat. 3 kabels (2x Cat6a S/FTP
  ~7 mm + coax H125 ~7 mm) passen ruim in 40 mm buis; alleen je toekomstige
  reserveruimte krimpt.
* Behoud 52 mm alleen als je een **gladde** (niet-geribbelde) PE-buis van
  echt max. 47–48 mm OD gebruikt.

### 5.4 De boordiepte is intern inconsistent

De procedure schrijft "in één beweging 20 cm diep boren", maar de eigen
vloeropbouw zegt: dekvloer 30–50 mm + pasplaat van piepschuim/bimsbeton. Tussen
de ribben ben je dus na ca. 60–120 mm door de constructie heen. Blind doorboren
tot 200 mm betekent in het beste geval dat je in het niets boort, in het
slechtste dat je je boorkroon in een naastliggende rib of in de wapening van de
pasplaatondersteuning zet.

**Oplossing:** boor **tot doorbraak**, niet tot een vaste diepte. Markeer de
verwachte doorbraakdiepte met tape op de kroon, en gebruik de proefboring van
stap 2 om de werkelijke pakketdikte te meten vóór je de kroon pakt. Gebruik
altijd de centreerpen bij het aanzetten; een eenmaal aangezet gat opnieuw
starten zonder centrering ruïneert de kroon.

### 5.5 ~~Het vloertype spreekt het bestaande dossier tegen~~ — OPGELOST

**Vervallen als blokkerend punt.** De opgave in §3.1 is volledig bevestigd door
de originele bouwstukken uit 1985–1986: Manta systeemvloer voor de begane grond
van woningtype M4, 255 mm, B 37,5, ribben 600 mm h.o.h., pasplaten ertussen. De
volledige verificatie staat in §3.3. De "tegenspraak" met de repo-README was een
onvolledige README: filigraan geldt voor de verdiepings- en zoldervloer, Manta
voor de begane grond.

De boorprocedure in §3.2 blijft dus geldig — en wordt door de tekening
aangescherpt op twee punten die §3.3 uitwerkt: de rib mag constructief niet
worden doorboord (*"geen sparing in rib"*, 1986), en de proefboringen moeten
**van voor naar achter** verschuiven omdat de ribben parallel aan de gevels
lopen.

**Wat hier nog wél open staat** (geen blokkade, wel uitzoekwerk vóór het
aftekenen): of Kruidenschans 24 de getekende of de gespiegelde variant van het
legplan is, en hoe de hoekwoning-situatie afwijkt van het middenblok op de
tekening. Visuele controle vanuit de kruipruimte blijft de snelste route: van
onderaf is de ribrichting en -afstand direct zichtbaar, en dan hoef je helemaal
niet te prikken.

---

## 6. Serieuze risico's & blinde vlekken

### Uitvoering vloerdoorgang

6.1 **Geen detectie van leidingen in de dekvloer.** De procedure zet direct een
6 mm steenboor in de dekvloer. Zit er vloerverwarming, een elektraleiding of
een waterleiding in, dan is de proefboring zelf al de schade. **Doen:**
leidingzoeker + warmtebeeldcamera (vloerverwarming aanzetten, dan fotograferen)
en de originele tekeningen erbij; bij twijfel de doorvoer vanuit de kruipruimte
omhoog boren op een positie die je van onderaf hebt uitgemeten.

6.2 **Droog diamantboren zonder stofbeheersing.** Een 52 mm droge kroon in
zandcement-dekvloer produceert een enorme hoeveelheid fijnstof door de hele
woonkamer; nat boren kan niet met laminaat eromheen. **Doen:** stofafzuigring +
bouwstofzuiger (M-klasse) begroten, of van onderaf boren.

6.3 **Uitkomstlocatie is niet vastgelegd.** Een 60 mm gat met 50 mm rozet
midden in het laminaat is permanent zichtbaar, en van vloer naar
wand/TV-meubel loopt nog een zichtbaar kabelstuk. **Doen:** exacte positie
bepalen (achter/onder het meubel, of in een hoek) en daar de ribzoekactie op
afstemmen — niet omgekeerd.

6.4 **Kruipruimte-uitvoering ongepland.** Geen check op kruipluikpositie, vrije
hoogte, waterstand of bodemgesteldheid. 25 m mantelbuis leggen in een lage,
natte kruipruimte is een dag werk voor twee personen. **Doen:** kruipruimte
eerst inspecteren; buis vrij van de bodem ophangen/steunen (beugels of op
tegels), niet in het water laten liggen.

6.5 **Zolderroute: nul regels documentatie.** Er staat één kabel van 25 m
begroot, maar geen tracé, geen schacht, geen doorvoeren, geen hulp bij het
optrekken. In de praktijk is dit meestal het moeilijkste deel van het hele
project. **Doen:** tracé uittekenen (bestaande leidingschacht? naast de
ventilatiekanalen? langs de trap?) en de kabellengte pas daarna definitief
vaststellen. Trek meteen een reservekabel of trekkoord mee.

### Meterkast

6.6 **Warmtehuishouding.** T630 (15–25 W continu) plus een 2,5G PoE-switch
(schakelverlies + PoE-dissipatie, al snel tientallen watts) in een dichte
Nederlandse meterkast. Dit is de klassieke oorzaak van uitval op termijn:
niet meteen, maar na de eerste zomer. **Doen:** temperatuurmeting begroten
(een HA-sensor in de kast, meteen), ventilatie voorzien (rooster of stille
fan), en apparatuur niet gestapeld monteren.

6.7 **Toegankelijkheid en ruimte.** De meterkast moet toegankelijk blijven voor
de netbeheerder en is doorgaans 60 cm breed en vol. Controleer of er fysiek
ruimte is voor switch + mini-PC + montagemateriaal, en of de groepenkast een
vrije modulepositie heeft voor de DS201.

6.8 **Geen UPS — en de dedicated groep koopt géén uptime.** € 49,90 aan een
eigen B16 aardlekautomaat beschermt tegen een *andere* groep die uitvalt, maar
niet tegen spanningsuitval, en niet tegen de eigen groep. Zodra de spanning
wegvalt liggen netwerk én Home Assistant plat — inclusief wat daarvan afhangt.
Erger: HA OS dat hard uitvalt corrumpeert op termijn zijn database.
**Doen:** € 60–90 aan een kleine line-interactive UPS levert meer
beschikbaarheid dan die aparte groep, en geeft HA de kans netjes af te sluiten
(USB/NUT-integratie). Overweeg de aparte groep te schrappen of te
verantwoorden op een andere grond dan uptime.

### Netwerk

6.9 **S/FTP zonder afgeschermde afmontage is weggegooid geld.** Er staan geen
keystones, patchpaneel of aardingsplan in de lijst. Een S/FTP-kabel waarvan de
afscherming aan één of beide zijden niet geaard is, presteert niet beter dan
U/UTP en kan zich als antenne gedragen. Daarnaast: vooraf gemonteerde
RJ45-stekkers aan elkaar tapen en door 25 m buis trekken is fragiel (de
trekkracht komt op de contacten te staan, niet op de mantel).
**Doen:** afgeschermde keystones + een geaard patchpaneel in de meterkast
begroten, en de kabels *onafgewerkt* door de buis trekken (trekkous of
trekoog op de mantel), daarna afmonteren. Kabeltester begroten.

6.10 **2x 10G SFP+ zonder plan.** De poorten worden als feature opgevoerd,
terwijl er geen module, geen DAC en geen 10G-capabel apparaat begroot is.
**Doen:** of schrappen als aankoopargument, of € 40–60 voor een DAC/module
begroten met een concreet doel (NAS?).

6.11 **Prijs en PoE-budget van de hoofdswitch zijn niet plausibel/onbekend.**
€ 69,99 voor 8x 2,5G PoE + 2x 10G SFP+ ligt ruim onder de markt voor die
specificatie; verifieer hoeveel poorten écht PoE zijn, wat het **totale
PoE-budget in watt** is, en of het 802.3af of 802.3at is. Zonder dat getal is
de PoE-architectuur (§5.2, optie 2) niet te dimensioneren. Controleer ook of
het een unmanaged model is.

6.12 **Geen segmentatie.** Er is gekozen voor (deels) unmanaged switches,
terwijl een smarthome met IoT-apparatuur, een HA-server en gastapparaten op één
plat L2-domein komt te staan. **Doen:** minimaal een VLAN-plan opstellen
(IoT / vertrouwd / gast) en daar de switchkeuze op baseren — of expliciet
vastleggen dat je dit bewust niet doet en waarom.

6.13 **Zigbee-coördinator op een slechte plek.** In of naast een kast met een
switch en een TV zit hij tussen metaal, 2,4 GHz WiFi en USB3/HDMI-ruis.
**Doen:** SLZB-06M vrij ophangen (niet in een kast, niet tegen metaal), en het
Zigbee-kanaal expliciet kiezen t.o.v. je WiFi-kanalen (Zigbee 15/20/25 naast
WiFi 1/6/11). Controleer ook de prijs: € 39,95 lijkt laag voor de 06M.

6.14 **Maar 2 kabels naar de woonkamer.** De marginale kosten van een derde en
vierde kabel zijn nu ~€ 25 per stuk; later opnieuw moeten boren kost de hele
exercitie opnieuw. De buis heeft de ruimte (mits §5.3 is opgelost).
**Doen:** 4 kabels trekken, of minimaal een extra trekkoord achterlaten.

6.15 **Afdichting alleen aan de binnenzijde van de buis.** De ringspleet tussen
buis en beton blijft dan open als tocht- en bodemgasweg. Beide afdichten.

### Bewoning, eigendom en beheer

6.19 **De woning wordt bewoond door iemand anders dan de beheerder — en dat
blijft ruim twee jaar zo.** De bewoner (Pamela) woont er nu; de ontwerper van
deze installatie komt pas bij de verbouwing inwonen, over minimaal twee jaar.
Het plan is echter geschreven alsof beheerder en bewoner dezelfde persoon zijn.
Dat is de grootste onuitgesproken aanname in het hele document.

**Wat dat concreet betekent:**

* **Alles moet op afstand beheerbaar zijn.** Twee jaar lang is er niemand ter
  plaatse die weet hoe het in elkaar zit. Elke storing die eindigt in "even de
  switch uit en weer aan" wordt een telefoontje, en elke storing die ligt bij
  het apparaat dat je toegang geeft (de router, de hoofdswitch, de HA-server)
  is niet op afstand te verhelpen.
  **Doen:** out-of-band toegang regelen (bijv. een los 4G/LTE-kanaal of een
  remote-reboot-stekker op de hoofdswitch en de server), automatisch herstel na
  spanningsterugkeer inschakelen in het BIOS van de T630 (*restore on AC power
  loss*), en HA zo configureren dat een herstart geen handmatige stappen vraagt.
* **Storingen raken haar dagelijks leven, niet dat van de beheerder.** Als de
  verlichting, de deurbel of het slot via HA loopt en HA valt uit, zit zij in
  het donker. **Doen:** geen enkele basisfunctie (licht, bel, slot, verwarming)
  uitsluitend via HA laten lopen; fysieke schakelaars en de bestaande bedrading
  functioneel houden als terugvaloptie.
* **Toestemming en aansprakelijkheid.** Een gat van 52–68 mm door een dragende
  vloer, een nieuwe groep in de meterkast en een buis door de kruipruimte zijn
  permanente ingrepen aan iemand anders' woning. **Vast te stellen:** is de
  woning eigendom van de bewoner of gehuurd? Bij huur is een doorvoer door de
  constructievloer zonder schriftelijke toestemming van de verhuurder geen
  optie. Ook bij eigendom: leg vast wie opdrachtgever is voor het werk aan de
  elektrische installatie.
* **De zolderlijn hoort bij de verbouwing, niet bij dit project.** Zie 6.20.

6.20 **De zolderlijn is nu weggegooid geld — de verbouwing sloopt precies dat
deel.** Volgens het dossier gaan bij de verbouwing de achtergevel omhoog, komen
er twee dakkapellen, wordt het dak opnieuw geïsoleerd en wordt de zolder een
volwaardige verdieping. Een Cat6a die je nu naar zolder trekt, ligt daar twee
jaar en wordt dan ingebouwd of gesloopt. En wordt die zolder een volwaardige
verdieping met kamers, dan is één kabel hoe dan ook te weinig: reken op drie à
vier aansluitpunten.

**Doen — kies bewust:**

| Optie | Kosten nu | Wanneer verstandig |
|---|---|---|
| Zolderlijn nu volledig uitvoeren | € 25 kabel + arbeid | Alleen als er de komende twee jaar echt een vast aansluitpunt of access point op zolder nodig is; beschouw het als tijdelijk en wegwerpbaar |
| Alleen mantelbuis + trekdraad naar zolder leggen | buis + arbeid | Voorkeur als het tracé nu open ligt: je trekt later de definitieve kabels zonder opnieuw te slopen |
| Zolderlijn uitstellen tot de verbouwing | € 0 | Voorkeur als er nu geen behoefte is — tijdens de dakwerkzaamheden liggen de leidingwegen open en kost het een fractie |

De vloerdoorgang meterkast ↔ woonkamer staat hier los van: die raakt de
verbouwplannen niet en kan vooruit.

### Overig

6.16 **Tweedehands server zonder fallback.** Een Marktplaats-T630 zonder
garantie is een single point of failure voor het hele smarthome.
**Doen:** HA-backupstrategie vastleggen (automatische backups naar een
*andere* machine of offsite, getest door één keer een restore te doen), en
weten wat je doet als de mini-PC sneuvelt.

6.17 **Is de coax nog nodig?** € 51,79 aan coax + connectoren is dood geld als
er geen DVB-C/kabeltelevisie meer wordt afgenomen. Bevestig het gebruiksdoel
voordat je die kabel door de buis trekt — of trek hem mee als reserve, dat is
het verdedigbare argument.

6.18 **Geen volgorde van werkzaamheden.** Boren moet vóór het leggen van (nieuw)
laminaat; de WCD in de woonkamer vóór de switchmontage; de meterkastgroep vóór
de apparatuur. **Doen:** §8 als uitvoeringsvolgorde aanhouden.

---

## 7. Ontbrekende posten & bijgesteld budget

| Ontbrekende post | Indicatie |
| :--- | :--- |
| Afgeschermde keystones + wandcontactdozen/opbouwdozen (woonkamer, zolder, meterkast) | € 40–60 |
| Geaard patchpaneel of keystone-rail meterkast | € 25–40 |
| Patchkabels (afgeschermd) | € 15–25 |
| 230 V wandcontactdoos woonkamer op switchlocatie (§5.2) | € 15–50 |
| Kleine line-interactive UPS (§6.8) | € 60–90 |
| Montagemateriaal meterkast (DIN-rail/plaat, beugels, kabelgoot) | € 20–40 |
| Stofafzuigring / M-klasse stofzuiger (huur) (§6.2) | € 0–40 |
| Kabeltester + labels | € 20–35 |
| Grotere boorkroon 68 mm i.p.v. 52 mm, óf 40 mm buis (§5.3) | € 0–35 |
| Extra 2x Cat6a 20 m (§6.14) | € 50 |
| SFP+ DAC, alleen bij concreet 10G-doel (§6.10) | € 0–60 |
| Ventilatie/temperatuursensor meterkast (§6.6) | € 20–50 |
| **Realistisch projectbudget totaal** | **€ 785 – € 1.095** |

Het oorspronkelijke totaal van ~€ 520 dekt de apparatuur en de kabel, niet de
installatie. Reken op **€ 265 – € 575 extra**. Dat is geen argument tegen het
plan — het is het verschil tussen een boodschappenlijst en een projectbegroting.

---

## 8. Actielijst vóór de eerste boring

0. [ ] **Toestemming en rolverdeling vastleggen** — eigendom of huur, wie is
       opdrachtgever voor het werk aan de elektrische installatie en de
       vloerdoorvoer, en wie is aanspreekbaar bij storing zolang de beheerder er
       niet woont (§6.19).
1. [x] ~~Vloertype vaststellen~~ — **gedaan**: Manta systeemvloer begane grond,
       255 mm, B 37,5, ribben 600 mm h.o.h., geverifieerd tegen de stukken uit
       1986 (§3.3). Resteert: ribpositie van onderaf uitmeten en op de vloer
       aftekenen, en vaststellen of #24 de getekende of gespiegelde variant is.
2. [ ] **WAN-intrede, router en IP-plan vastleggen** — pas daarna is de
       topologie bepaald (§5.1).
3. [ ] **Voeding woonkamerswitch beslissen** — WCD, PoE-powered switch, of
       sub-switch schrappen (§5.2).
4. [ ] **PoE-budget hoofdswitch verifiëren** (watt, aantal poorten, af/at)
       en specificatie/prijs van de GigaPlus controleren (§6.11).
5. [ ] **Boormaat definitief kiezen** — 68 mm kroon + 50 mm buis, óf 52 mm
       kroon + 40 mm buis (§5.3).
6. [ ] **Leidingdetectie in de dekvloer** — leidingzoeker + warmtebeeld (§6.1).
7. [ ] **Uitkomstlocatie woonkamer bepalen** inclusief route vloer → wand (§6.3).
8. [ ] **Kruipruimte inspecteren** — luik, hoogte, water, buisondersteuning (§6.4).
9. [ ] **Zoldertracé uittekenen** en kabellengte definitief maken (§6.5).
10. [ ] **Aantal kabels vaststellen** (advies: 4 naar de woonkamer) en coax
        bevestigen of schrappen (§6.14, §6.17).
10a. [ ] **Beslissen over de zolderlijn** — nu uitvoeren, alleen buis + trekdraad,
        of uitstellen tot de verbouwing (§6.20).
10b. [ ] **Beheer op afstand inrichten** — out-of-band toegang, automatisch
        herstel na spanningsuitval, en geen basisfunctie uitsluitend via HA
        (§6.19).
11. [ ] **Ontbrekende posten bijbestellen** volgens §7, inclusief afmontage
        en UPS.
12. [ ] **Ventilatie/temperatuurbewaking meterkast regelen** (§6.6, §6.7).
13. [ ] **Backupstrategie HA vastleggen en één restore testen** (§6.16).

Uitvoeringsvolgorde daarna: meterkastgroep → WCD woonkamer → boren →
mantelbuis + kabels → afmonteren + testen → apparatuur plaatsen →
HA configureren → laminaat afwerken.

---

## 9. Bronverantwoording

Dit document is gebaseerd op de aangeleverde projecttekst, aangevuld met het
dossier **Kruidenschans 24, Voorhout** in deze repo.

**Gebruikt voor de verificatie in §3.3** (originele stukken, 1985–1986):

| bron | gebruikt voor |
|---|---|
| `bouwtekeningen/funderingsplan_vloer.pdf` | Titelblok "MANTA systeemvloer voor de begane grond, woningtype M4", B 37,5 / FeB 500, oplegging, legplan en ribrichting, notities *"geen sparing in rib"* en *"betonnokken in isolatie onder rib max. 150 cm h.o.h."* |
| `berekeningen/berekening_belastingen_pasplaat.pdf` | ht 255 mm, breedte per rib 600 mm, breukmomententabel Manta, betonkwaliteit B 37,5 |
| `berekeningen/berekening_vloerplaten_filigraan.pdf` | Vaststelling dat filigraan de **verdiepings- en zoldervloer** betreft, niet de begane grond |
| `gespreksverslag.md`, `README.md`, `tekeningen/` | Verbouwplannen (achtergevel, dakkapellen, zolder) → §6.20 |

De scans hebben een OCR-tekstlaag en zijn daarnaast als afbeelding uitgelezen
voor de handschriftnotities en de doorsnedes.

**Niet gebruikt, en waarom:**

| bron | reden |
|---|---|
| Groepenkastoverzicht en IP-/apparatenlijst in Google Drive | Horen bij een **ander adres (Oranjelaan)**, niet bij Kruidenschans. In een eerdere versie van dit document waren ze wel verwerkt; dat is teruggedraaid omdat conclusies over groepsindeling, aardlekzones, overspanningsbeveiliging en subnet dan van het verkeerde gebouw kwamen. |
| Gemini-gesprek (`share.gemini.google`) | Niet op te halen: het netwerkbeleid van de werkomgeving blokkeert dat domein. |
| NotebookLM-notebook | NotebookLM-notebooks zijn geen Drive-bestanden en dus niet via de Drive-koppeling te lezen. |

> ⚠️ **Vaststaande regel voor dit dossier:** gegevens over de bestaande
> installatie (meterkast, groepenindeling, router, subnet, bestaande apparatuur)
> gelden **per adres**. Voor Kruidenschans 24 is daarvan nu niets vastgesteld —
> zie de actielijst in §8. Materiaal van een ander adres is hier geen
> uitgangspunt, ook niet als referentie.
