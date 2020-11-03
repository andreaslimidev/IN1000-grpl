# Uke 11 IN1000

- Fysiske gruppetimer fortsetter!
- Status på oblig 8
- 4 timers hjemmeksamen (3. desember)
- Eksamensoppgaver ligger ute for 2019.


## Feilsøking


## Noen nøtter

Hva heter person etter denne koden er kjørt?
```python

class Person:
    def __init__(self, navn):
        self._navn = navn
    
    def endre_navn(self, navn):
        self._navn = navn


class Folkeregister:
    
    def bytt_navn(self, person, navn):
        person.endre_navn(navn)


pers = Person("Andreas")
register = Folkeregister()

register.bytt_navn(pers, "Thomas")

```

Hva blir verdiene i denne listen?
```python

def squared(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]**2

    return [7, 8, 9]

lst = [1, 2, 3]
squared(lst)

print(lst)

```

## Oppgave for uken 

**Studenter og Fag**
Denne uken skal dere begynne å jobbe på et større program. Dere vil denne uken lage klassene “Fag” og “Student” som begge skal ha referanser til hverandre. Neste uke vil dere jobbe med å knytte dem sammen til et større system. 

**Oppgave 1**
1.1 Lag en klasse “Fag”, som skal ha et navn og en liste som holder på alle studentene som tar det aktuelle faget. Ved opprettelsen av et fag vil denne studentlisten være tom. 

1.2 Lag en metode i Fag-klassen som heter “leggTilStudent(student)” som tar imot en Student som parameter og legger den til i listen. Hvor i listen du legger den til spiller ingen rolle, så du må gjerne bruke .append(). 

1.3 Lag en metode i Fag-klassen som returnerer antallet studenter som tar faget, kall denne “hentAntallStudenter()”.

1.4 Lag en metode som returnerer fagets navn, hentFagNavn(). 

1.5 Lag en metode “skrivStudenterVedFag()” som skriver ut fagnavnet, og deretter alle studentene som tar faget. 
Merk: Anta at metoden hentStudentNavn() er implementert Student-objektet. 


**Oppgave 2**
2.1 Lag en klasse “Student”. Studenten skal ha et navn og en liste som holder på fagene studentene tar. Ved opprettelsen av en student vil denne faglisten være tom. 

2.2 Legg til en metode i Student-klassen som heter “leggTilFag(fag)” som tar imot et fag som parameter og legger det til i studentens liste over fag. 

2.3 Lag en metode i Student-klassen som returnerer antallet fag studenten tar, kall denne “hentAntallFag()”.  

2.4 Lag en metode i Student-klassen som returnerer studentens navn, hentStudentNavn(). 

2.5 Lag en metode “skrivFagPaaStudent()” som skriver ut studentens navn, og deretter alle fagene som studenten tar. 
Her må du bruke hentFagNavn() fra Fag-objektet. 


**Oppgave 3**
Lag et lite testprogram hvor du lager noen studenter og noen fag. Legg til fagene i studentenes liste og studentene inn i fagene. Skriv ut hvor mange fag studentene dine tar, og hvor mange studenter hver av fagene dine tar. 

