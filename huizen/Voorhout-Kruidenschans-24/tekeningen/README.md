# Kruidenschans 24, Voorhout — schetsen & verbouwstudie

Herget. schetsen van huis, tuin en verdiepingen, plus een eerste studie naar het
**optrekken van de achtergevel (nokverhoging)** met 2 dakkapellen en nieuwe
dakisolatie. Alle tekeningen zijn herleid uit de originele bestektekeningen en
constructieberekeningen (Bouwkundig adviesburo H.C. Bogaards / Noorlander Bouw,
1986) en de aangeleverde foto's en kadasterkaart.

> ⚠️ De maten zijn **indicatief** (afgelezen van gescande tekeningen) en bedoeld
> als basis voor het gesprek. Exacte maten moeten tegen de originele
> gemaatvoerde tekeningen worden gelegd; de constructie moet door een
> constructeur worden nagerekend vóór aanvraag.

## De woning
- **Adres / perceel:** Kruidenschans 24, Voorhout — kadastraal VHT00-B-5008, ± 215 m².
- **Type:** woning **type M4**, plan Oosthout B1 (rij van 19 woningen), bouwjaar 1986.
- **Opbouw:** begane grond + verdieping + zolder onder een **steil zadeldak**.
- **Fundering:** prefab **heipalen** (≈ 290 mm vierkant) — puntdragend op zand.
- **Vloeren:** **breedplaatvloeren** (filigraan), verdiepingsvloer ontworpen op
  ± 4,8 kN/m² permanent + woonbelasting.
- **Dak:** pannendak (grijze romaanse pannen), zeer steile helling.

### Kerngeometrie (afgelezen uit de doorsnede)
| niveau | hoogte t.o.v. peil |
|---|---|
| begane grond vloer (peil) | ± 0,00 |
| verdiepingsvloer | + 2,70 |
| goot (dakvoet) | + 3,70 |
| zoldervloer | + 5,40 |
| nok (dakfirst) | + 9,20 |

- Breedte (tussen bouwmuren): **± 5,40 m**
- Diepte onder hoofddak (voor↔achter): **± 8,0 m**, nok ongeveer in het midden
- Dakhelling: **± 50–54°** (steil)

## De tekeningen (map `tekeningen/`)
| blad | bestand |
|---|---|
| 1. Situatie & tuin | `1_situatie_tuin.png` |
| 2. Begane grond | `2_begane_grond.png` |
| 3. Verdieping (1e) | `3_verdieping.png` |
| 4. Zolder | `4_zolder.png` |
| 5. Doorsnede – voorstel achtergevel optrekken | `5_doorsnede_voorstel.png` |

Alle bladen zijn ook als bewerkbare `.svg` aanwezig; herfabriceren met
`python3 generate_plans.py`.

## Voorstel: achtergevel optrekken + 2 dakkapellen + dakisolatie

### Idee (zoals op de aangeleverde "Ontwerpvoorstel"-foto)
De achterste (tuinzijde) dakhelling wordt vervangen door de **achtergevel
recht op te trekken tot nokhoogte**, met een nieuw, flauwer dakvlak van de
bestaande nok naar de nieuwe achtergevel. Daardoor verandert de lage, schuine
zolderruimte aan de tuinzijde in **volwaardige, recht-wandige vloeroppervlakte**.

### Oppervlaktewinst (raming)
Op zolderniveau (vloer +5,40) is nu pas vrije hoogte:
- ≥ 1,5 m vanaf ± 2,3 m uit de gevel → **≈ 17 m²** telt mee als gebruiksoppervlak;
- ≥ 2,3 m (volwaardig verblijf) vanaf ± 2,9 m uit de gevel → **≈ 11 m²**.

Na het optrekken van de achtergevel wordt de **achterste helft (± 4,0 × 5,1 m)**
volledige sta-hoogte:

| | bestaand | na optrekken | winst |
|---|---|---|---|
| volwaardige vloer (≥ 2,3 m) op zolder | ≈ 11 m² | ≈ 25 m² | **≈ +14 m²** |
| gebruiksoppervlak (≥ 1,5 m) op zolder | ≈ 17 m² | ≈ 30 m² | ≈ +13 m² |

**Conclusie: ordegrootte +15 à +22 m² volwaardige bruikbare ruimte**,
afhankelijk van de gekozen nieuwe nokhoogte en dakhelling. De zolder wordt
daarmee feitelijk een (bijna) volwaardige tweede verdieping. Daarnaast krijgt
de verdieping aan de tuinzijde een rechte gevel in plaats van een schuin dak →
flinke comfort-/bruikbaarheidswinst.

### 2 dakkapellen
- Op het **resterende (voorste/straat-) dakvlak** geven 2 dakkapellen extra
  sta-hoogte en daglicht op verdieping/zolder; elke dakkapel van ± 3–4 m breed
  voegt grofweg **3–5 m²** volwaardige hoogte toe in het schuine deel.
- Let op vergunning: dakkapel aan de **voorzijde** is **niet** vergunningvrij
  (welstand!); aan achter/zijkant vaak wél, mits binnen de regels.

### Dak opnieuw isoleren
- Bij vernieuwen/optrekken het hele dak isoleren naar **Rc ≥ 6,3 m²·K/W**
  (huidige verbouweis voor daken). Combineer met goede luchtdichting en
  ventilatie.
- Mogelijk **ISDE-subsidie** voor dakisolatie (voorwaarden checken).

### Technische haalbaarheid (eerste inschatting)
- **Fundering:** heipalen met ruime puntdraagkracht; een nokverhoging voegt
  relatief weinig gewicht toe (lichte hout-/staalconstructie + isolatie +
  dakbedekking). Doorgaans haalbaar, **maar** paaldraagkracht en de bestaande
  belasting moeten worden nagerekend.
- **Belastingafdracht:** de opgetrokken achtergevel en het nieuwe dak rusten op
  de bestaande achtergevel en breedplaat-verdiepingsvloer → mogelijk een
  **nieuwe ligger / versterking** nodig.
- **Vergunning:** nokverhoging + gevelwijziging = **omgevingsvergunning**
  (bouw + welstand). Op de originele tekening staat een
  welstandsstempel (Vereniging Dorp Stad en Land) → welstand is hier relevant.

## Aandachtspunten / nog te bevestigen
1. Exacte maatvoering (breedte, diepte, nok-/goothoogte) tegen de originele
   gemaatvoerde tekening leggen.
2. Is dit een **tussen-** of **hoek-/eindwoning**? (kadasterkaart suggereert een
   ruim/hoekperceel) — bepaalt of er een vrije kopgevel is en wat er mag.
3. Gewenste **nieuwe nokhoogte / dakhelling** van het achterdakvlak — bepaalt de
   exacte m²-winst.
4. Plaats en breedte van de **2 dakkapellen** (voor/achter/zij).
5. Constructeursberekening + check geldende **bestemmingsplan/welstand**.
