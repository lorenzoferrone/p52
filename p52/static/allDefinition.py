# type: ignore

# questi tre "import" funzionano solo perché l'autocomplete non esegue il codice e non passa
# tramite transcrypt, ma vede che dallo sketch "importo" questo file e quindi vede cosa ci sta dentro
# (e anche ricorsivamente)

# sys.exit serve perché questo codice non va davvero eseguito, altrimenti lo sketch (inteso
# come script python) dopo aver terminato il viewer entra dentro questo file e si trova in un import circolare del modulo
# p52

import sys

sys.exit(0)

from .p5definition import *  # original p5 definition
from ..utils.p52 import *  # custom stuff I added

# 'fake' empty object so that can we use it w/o warning inside the sketch
self = {}


def injectJs(name):
    pass
