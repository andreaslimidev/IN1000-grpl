# Oppsummering av forrige uke

-   Tilbakeblikk på oblig 3

    > Gjennomgå oppgave 4.

-   Utbredte uvaner
    > Unødvendig typekonvertering.

# Tema for uken

## Loops

Brukes dersom man ønsker å gjenta en kodeblokk.

## While-loops

Brukes som regel der det er ukjent hvor mange iterasjoner en ønsker. Utrykket må være modifiserbart (ellers infinite-loop).

```
while condition:
    # do something
```

### Eksempler

Loop fra 0 til 5:

```
i = 0
while i < 5:
    # do something

    i += 1
```

Legg til elementer i en liste:

```
lst = []
while len(lst) < 3:
    lst.append(1)
```

Indekser en liste:

```
tekst = ["hadet", "på", "badet", "din", "gamle", "sjokolade"]
i = 0

while i < len(tekst):
    print(tekst[indeks])
    indeks += 2
```

Loop til brukeren ikke gir input:

```
inp = input("Skriv noe")
while inp != '':
    print(inp)
    inp = input("Skriv noe mer")
```

## For-loops

Fint når vi 'vet' hvor mange ganger som skal loopes.

```
for i in <noe>:
    # do something
```

### Eksempler

Loop x antall ganger:

```
for i in range(3):
    # do something
```

Loop fra x til y:

```
for i in range(2, 5):
    # do something
```

Loop fra x til y m/steg:

```
for i in range(0, 10, 2):
    # do something
```

Loop igjennom en liste:

```
lst = [1, 2, 3]
for num in lst:
    print(num)
```

## Funksjoner

-   Prosedyrer vs. funksjoner.

### Argumenter

-   Parameter vs. argument

Definer en prosedyre med argumenter:

```
def add(x, y):
    # do something with x and y!
```

Bruk argument i prosedyrekropp:

```
def add(x, y):
    print(x + y)
```

### Funksjoner (returverdier)

Funksjoner har alltid en returverdi.

Definer en funksjon:

```
def func(var1, var2):
    # do something
    # return something
```

Definer funksjonen add som plusser to tall:

```
def add(x, y):
    return x + y
```

Return brukes til å både avslutte funksjonen, samt returnere en verdi.

### Eksempler

Skriv en prosedyre “storst_av_to” som tar imot to tall som parametre og skriver ut verdien til det største tallet:

```

```

Definer funksjonen find(lst, elem). Denne funksjonen tar inn en liste og returnerer True dersom elementet finnes i listen:

```
def find(lst, elem):
    # what to do??
```
