# Oppsumering av forrige uke

## Tilbakeblikk på oblig 4

-   Bruk av innebygde metoder
-   while True
-   for elem vs. in range

## Litt repetisjon

Hva returneres her?

```
def max(tall1, tall2):
    if tall1 > tall2:
        return tall1
    return tall2
```

# Tema for uken

-   Fordøye tungt stoff fra forrige uke

## Lesing av filer

For å 'åpne' en fil:

```
file = open("filnavn", "r") # kan gi en FileNotFoundError!
```

Les innhold fra fil:

```
file.read() # leser hele filen
f.read(10) # leser første 10 chars i filen
f.readline() # leser inn en linje
```

Iterer gjennom en fil:

```
for linje in file:
    # do something with linje
```

Skriving til fil:

```
file = open("filnavn", "w") # åpner filen i write-mode
file.write("linje vi vil skrive")
```

Lukking av fil:

```
file.close() # god skikk for å forhindre potensielle feil
```

### Eksempel

## Skop

-   Lokalt vs. globalt skop

### Eksempler

Hva blir printet her?

```
x = 10
def my_func():
    x = 20

my_func()
print(x)
```

Hva med her?

```
x = 10
def my_func():
    x = 20
    return x

my_func()
print(x)
```

Eksempel på argumenter og skop:

```
x = True
def my_func(x):
    print(x)

my_func(False)
```

Hva blir blir variabelen i?

```
i = 0
for i in range(3):
    print("hello")
```
