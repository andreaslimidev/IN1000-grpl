# IN1000 labinar | uke 7

## Tilbakeblikk på uke 6
* Oblig 5
* Andre ting?

## Grunnleggende objektorientering

### Hvorfor?
* Modellering av virkeligheten

## Begreper
* Innkapsling
* Instansiering / instans
* Objekt
* Klassedefenisjon
* Grensesnitt
* Instansvariabel
* Metode


### Defenisjon
En klasse defineres slik:
```python
class Person:
    # defenisjon
```
En klasse kan også ha andre metoder:
```python
class Person: 
    .
    .
    .
    def siHallo(self):
        print("Hallo!")
```

Vi er nødt til å sende med `self` i alle metoder for å få tilgang til objektets variabler/metoder.

**Oppgave**: implementer et gitt grensesnitt:
```python
class Person:

    """ settNavn(self, navn):
            setter navnet på personen
        
        skrivNavn(self):
            skriver ut navnet på personen

        settAlder(self, alder):
            setter alder på personen
        
        settVekt(self, vekt):
            setter vekt på personen

        settHoyde(self, hoyde):
            setter hoyde på personen

        skrivUtInfo(self):
            skriver ut info om personen

        skrivUtHilsen(self):
            printer "hei, jeg heter <navn> og er <alder> aar gammel"

        hoyereEnn(self, annen):
            om 'self' personen er høyere en den gitte 'annen' 
            return True, else False
    """
```

En klasse burde ha en konstruktør. Denne forteller hva som skal skje når et objekt instansieres. Denne defineres slik:
```python
class Person:
    def __init__(self, args...):
        # do something
```
Et eksempel kan være:

```python
def __init__(self, navn, alder):
    self._alder = alder
    self._navn = navn
```

**Oppgave**: gjør om klassen til å ta i bruk en konstruktør, slik at variabler som navn, høyde, etc, kan settes når objektet instansieres.

**Oppgave**: instansier tre personer og legg disse i en liste. Lag deretter en funksjon som looper denne listen og printer ut navnet til hver person.

Hva er alderen til p2 her?
```
class Person:
    .
    .
    .

p1 = Person("Thomas", 21)
p2 = Person("Sigrunn", 20)

p1 = p2
p1.settAlder(19)

```







