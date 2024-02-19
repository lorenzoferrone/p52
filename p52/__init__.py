import inspect
import pathlib

from .compiler import compileSketch, launch_recompiler_observer
from .viewer import launch_viewer
from .sketchClass import SketchInfo
from .reloader import launch_reload_server


importFile = inspect.stack()[-1]
sketchPath = pathlib.Path(importFile.filename).resolve()


sketch = SketchInfo(sketchPath)
compileSketch(sketch)

launch_reload_server()
launch_recompiler_observer(sketch)
launch_viewer(sketch)


# import definition file just to have autocomplete in the sketch file
from .static.allDefinition import *


# TODO:
# come far funzionare "pop", "map" e simili (al momento sono metodi di python, non di p5js)?
#    sono riuscito a fare qualcosa dentro utils.p52.
#    al momento ho reimplementato map, ma in questo modo sovrascrivo pymap
#    continuare a testare per capire  se si rompe qualcos'altro

# come integrare eventuali altre librerie javascript??
#    da testare, ma dovrebbe bastare importare il file (import file.js)
#    facendo solo import non funzionerà mai con file js fatti per essere messi in un tag <script>, ma
#    solo con file che fanno export dei loro attributi....

# come modificare comportamenti di p5js direttamente a runtime (ad esempio cambiare le coordinate)?
#    BOH, penso impossibile, bisognerebbe accedere al runtime di p5js... che però mentre sto compilando
#    ancora non esiste...
