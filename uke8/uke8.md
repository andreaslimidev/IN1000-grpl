# Uke 8 IN1000

## Repetisjon og beskjeder.

* Oblig 6
* **Oblig 7!!**

```python
class Motorsykkel: 

    def __init__(self, merke, regnr, kmstand):
        self._merke = merke
        self._regnr = regnr
        self._kmstand = kmstand

    def kjor(self, km): 
        self._kmstand += km

    def hentKilometerstand(self):
        return self._kmstand
```
Hva skjer her?
```python
m1 = Motorsykkel("Honda", 1, 10)
m2 = Motorsykkel("Suzuki", 2, 10)
m3 = Motorsykkel("Kawasaki", 3, 15)

m2 = m1
m2.kjor(10)

# hva blir m1 sin kilometerstand her?
```

Hva med her? 
```python
m1 = Motorsykkel("Honda", 1, 10)
m4 = Motorsykkel("Honda", 1, 10)

if m1 == m4: 
    # do something

if m1 == m1: 
    # do something

m1 = m4 
if m1 == m4:
    print("hello")
```

## Gjennomgang av uke 8

### Returnere None
En funksjon kan returnere 'ingenting'.

```python
def finn_stud(self, navn):
    for student in stud_liste:
        if student.navn == navn:
            return student


def finn_stud(self, navn):
    stud = None
    for student in stud_liste:
        if student.navn == navn:
            stud = student
    return stud

```
### __str__

For å gjøre printingen av et objekt enklere, kan dere implementere `__str__`.
```
def __str__(self):
    # returner en string
```

### Oppgaver

### 1
Skriv en klasse sirkel. En sirkel har en radius, lag en konstruktør som setter radius. Konstruktøren skal ta inn radius som argument. I tillegg skal dere sette instansvariabelen diameter (radius*2).

Lag 2 metoder til: en som returnerer omkretsen til sirkelen og en som returnerer arealet til sirkelen.

Hint: omkrets av en sirkel er diameter * pi, arealet av en sirkel er radius² * pi. Eksponenter skrives som <base>**<eksponent>, f.eks. 2^8 skrives 2 ** 8. 

Lag deretter 2 sirkler med ulik radius. 
Skriv ut den ene sirkelens omkrets og areal, og den andre sirkelens diameter.

### 2
Lag en klasse Blomst. En blomst har en art, en høyde, en instansvariabel som sier om blomsten har det bra eller ikke (denne verdien er en boolean), og en verdi som forteller hvor lenge siden blomsten ble vannet sist. Konstruktøren setter alle disse verdiene, når en blomst blir opprettet vil blomsten alltid ha det bra og det vil være 0 dager siden den ble vannet sist. 

En blomst har en metode hentStatus som returnerer verdien som forteller om blomsten har det bra eller ikke.

I tillegg har den metoden __str__, som returnerer en info streng om blomsten

Videre har en blomst en metode nesteDag, som øker antall dager siden den ble vannet med en. Hvis det er mer enn tre dager siden blomsten ble vannet sist vil statusen til blomsten være at den har det dårlig. Hvis statusen til blomsten er  at den har det bra vokser blomsten 1 cm.  

Den siste metoden en blomst har er metoden vann. Hvis det er mindre enn 3 dager siden blomsten ble vannet vil statusen til blomsten bli dårlig (over vanning), ellers vil statusen være bra. 

Skriv denne klassen + lag et lite testprogram for å teste klassen din.




