<img src="https://github.com/wathenro/ot-harjoitustyo/blob/master/Dokumentaatio/pak_ka.jpg" width="750">

#Sekvenssikaavio
<img src="https://github.com/wathenro/ot-harjoitustyo/blob/master/Dokumentaatio/sekvenssikaavio.jpg" width="750">

UI käyttöliittymä hakee LocationLoaderin kautta netistä Suomen kunnat sijaintitietoineen ja tiedostosta kuntien asukasmäärät.

Käyttäjä valitsee lähtö- ja pääteasemat sekä max radan pituuden. Nämä välitetään MapMakerille joka tekee kartan numpy matriisiin ja palauttaa myös listan kartalle jäävistä kunnista tietoineen.

UI ohjaa nämä tiedot sekä käyttäjän antaman maksimi radanpituuden Optimizerille, joka antaa annetulle radanpituudelle mahdollisimman väestokattavan ratalinjauksen ja palauttaa nämä tiedot. UI lopuksi renderöi kartan ruudulle.
