from passasjer import Passasjer

class Trikk:
    def __init__(self, rutenr, antallRader):
        self._rutenr = rutenr
        self._antallRader = antallRader
        self._radKapasitet = 5
        self._plasser = self._lagRader(antallRader)

    def _lagRader(self, antallRader):
        plasser = []
        for i in range(antallRader):
            rad = []
            for i in range(5):
                rad.append(None)
            plasser.append(rad)
        return plasser

    def gaaPaaTrikk(self, passasjer):
        for rad in range(self._antallRader):
            for kol in range(5):
                if self._plasser[rad][kol] == None:
                        self._plasser[rad][kol] = passasjer
                        passasjer.gaaPaa()
                        return True
        return False

    def gaaAvTrikk(self, stasjon):
        for rad in range(self._antallRader):
            for kol in range(5):
                if self._plasser[rad][kol] != None:
                    passasjer = self._plasser[rad][kol]

                    if passasjer.hentAvstigning() == stasjon:
                        # passasjer skal av
                        print("test")
                        self._plasser[rad][kol] = None
                        passasjer.gaarAvRiktig()
                    
                    elif self.evakuer(rad, kol):
                        print("noob")
                        self._plasser[rad][kol] = None
                        passasjer.gikkAvPgaStank()

                    else:
                        passasjer.ookAntallStasjoner()


                    
    
        return False

    def evakuer(self, r, k):
        naboer = 0
        for rad in range(r - 1, r + 2):
            for kol in range(k-1, k + 2):

                gyldig = True

                # sjekk at koordinatene er innenfor rutenettet
                if rad < 0 or kol < 0: 
                    gyldig = False

                if rad >= self._antallRader or kol >= 5:
                    gyldig = False
                
                if rad == r and kol == k:
                    gyldig = False

                if gyldig and self._plasser[rad][kol] != None:
                    nabo = self._plasser[rad][kol]
                    # print(nabo._antallStasjoner)
                    if nabo.stinker():
                        naboer += 1
        print(naboer)
        return naboer > 4


    def __str__(self):
        r = ""
        for rad in self._plasser:
            r += "|"
            for plass in rad:
                r += str(plass) + "|"  
            r += "\n"
        return r




trikk = Trikk(13, 5)
print(trikk)


p1 = Passasjer("Andreas", 1, 3)
p2 = Passasjer("Thomas", 1, 4)
p3 = Passasjer("Kaia", 1, 5)
p4 = Passasjer("Sigrunn", 1, 6)
p5 = Passasjer("Pernille", 1, 7)
trikk.gaaPaaTrikk(p1)
trikk.gaaPaaTrikk(p2)
trikk.gaaPaaTrikk(p3)
trikk.gaaPaaTrikk(p4)
trikk.gaaPaaTrikk(p5)
trikk.gaaPaaTrikk(p1)
trikk.gaaPaaTrikk(p2)
trikk.gaaPaaTrikk(p3)
trikk.gaaPaaTrikk(p4)
trikk.gaaPaaTrikk(p5)

print(trikk)
trikk.gaaAvTrikk(0)

print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)
print(trikk)
trikk.gaaAvTrikk(0)


print(trikk)