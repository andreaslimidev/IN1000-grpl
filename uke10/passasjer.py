class Passasjer:

    def __init__(self, navn, paastigning, avstigning):
        self._navn = navn
        self._paastigning = paastigning
        self._avstigning = avstigning
        self._antallStasjoner = 0
        self._komFram = False
        self._komPaa = False


    def hentPaastigning(self):
        return self._paastigning

    def hentAvstigning(self):
        return self._avstigning

    def ookAntallStasjoner(self):
        self._antallStasjoner += 1

    def gaarAvRiktig(self):
        self._komFram = True

    def komFram(self):
        return self._komFram

    def komPaa(self):
        return self._komPaa

    def gaaPaa(self):
        self._komPaa = True

    def hentAntallStasjoner(self):
        return self._antallStasjoner

    #hvis personer har sittet på 6 stopp eller mer stinker den
    def stinker(self):
        if self._antallStasjoner >= 6:
            return True
        return False

    def gikkAvPgaStank(self):
        if self._komPaa and not self._komFram:
            return True
        return False

    def __str__(self):
        return self._navn
