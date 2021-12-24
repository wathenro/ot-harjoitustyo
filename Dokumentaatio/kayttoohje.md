## Käyttöönotto

Lataa viimeisin release ja pura se sopivaan paikkaan.

Asenna tarvittavat riippuvuudet 
```bash
poetry install
```
Siirry 
```bash
poetry shell
```
Ja nyt voit käynnistää
```bash
poetry run invoke start
```

## Käyttö

Ohjelman käyttöliittymä näyttää tältä:
![](kayttoohjekuva.jpg)

* Vihreä nuoli osoittaa alasvetovalikkoon josta valitaan lähtöasema
* Punainen nuoli osoittaa alasvetovalikkoon josta valitaan pääteasema
* Sinisen nuolen kohtaan kirjoitetaan maksimi radanpituus ja klikataan "Design"

Tämä optimoi radan mahdollisimman suurelle väkimäärälle.

- Saatu tulos näkyy 'Optimized track length'-ruudussa

* Keltaisen nuolen osoittama 'Make report' tekee PDF-raportin ja tallentaa sen data/reports hakemistoon.