# Vaatimusmäärittely

## Tarkoitus

RailwayDesigner auttaa löytämään radanpituuden ja väestökattavuuden kannalta optimaalisen ratalinjauksen kahden kaupungin välille. Optimaalisen linjauksen löydyttyä tästä on mahdollista tallentaa PDF-raportti. 

## Käyttäjät

Sovellusta voi tässä vaiheessa käyttää kuka tahansa eikä käyttäjiä mitenkään identifioida tai erotella.

## Käyttöliittymäluonnos

Sovelluksella on yksi näkymä.
<img src="https://github.com/wathenro/ot-harjoitustyo/blob/master/RailwayDesigner/Dokumentaatio/kayttoliittyma.jpg" width="750">


## Perusversion tarjoama toiminnallisuus

Ohjelma lukee wikipediasta Suomen kunnat sijainteineen, sekä tiedostosta näiden kuntien asukasluvut. Alasvetovalikoista voidaan valita lähtö- ja pääteasemat. Maksimi radanpituus syötetään tekstikenttään. Näistä määritellään mahdollisimman lähellä annettua radan pituutta olevat reitti, jonka asukasmäärä on mahdollisimman suuri. Reittilinjauksesta piirretään kartta, josta saa käsityksen sen kulusta. Hyvän linjauksen löydyttyä siitä voidaan tehdä PDF-raportti.

## Jatkokehitysideoita

Optimointi perustuu suureen määrään satunnaisia hakuja. Tämä voidaan optimoida tekemällä siitä syvyyshaku. Sama asukasmäärä voidaan saavuttaa myös eri pituisilla ratalinjauksilla, nykyinen algoritmi ei valitse näistä lyhyintä vaan sen joka on lähimpänä annettua maksimipituutta.

Ohjelma voi tehdä visuaalisesti huomattavasti selkeämmän, jos se piirtäisi ratalinjaukset tyhjän taustan sijaan olemassa olevalle kartalle. Tämä on täysin toteutettavissa.

Tehdyt radat tulisi voida tallettaa tietokantaan josta niitä voisi tarpeen tullen hakea. Toinen vaihtoehto on oma tiedosto. Esimerkiksi raporttirakenteen hyvin määrittelemällä ohjelma voisi lukea ne suoraan tehdyistä raporteistakin.
