# Vaatimusmäärittely

## Tarkoitus

RailwayDesigner auttaa löytämään radanpituuden ja väestökattavuuden kannalta optimaalisen ratalinjauksen kahden kaupungin välille. Optimaalisen linjauksen löydyttyä tästä on mahdollista luoda ja tallentaa raportti. Saatu linjaus voidaan myös tallentaa tietokantaan.

## Käyttäjät

Sovellusta voi tässä vaiheessa käyttää kuka tahansa eikä käyttäjiä mitenkään identifioida tai erotella.

## Käyttöliittymäluonnos

Sovelluksella on tässä vaiheessa vain yksi näkymä. Lisäksi raportti avataan luonnin jälkeen omaan ikkunaansa.
<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/v-1.png" width="750">


## Perusversion tarjoama toiminnallisuus

Perusversio lataa jonkun kovakoodatun kartan paikkakunta, etäisyys ja väestötietoineen todennäköisesti Pythonin dictionaryksi. Kartta näytetää ruudulla ja mahdolliset asemapaikkakunnat alasvetovalikoissa. Määrittämällä radan pituus lasketaan optimaalinen reitti lähdöstä pääteasemalle ja näytetään se kartalla. Hyvän linjauksen löydyttyä se voidaan tallentaa ja ladata uudestaan. Siitä saa myös tehtyä raportin.

## Jatkokehitysideoita

Kartta ei ole kovakoodattu vaan sen voi valita haluamakseen.
Web-versio
Mäkisyys ja muut maston muodot, ratakilometrin hinta missäkin maastossa
