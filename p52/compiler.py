import time
import subprocess
import pathlib

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from websockets.sync.client import connect


package_dir = pathlib.Path(__file__).parent.resolve()
fakeModulesPath = package_dir / "fakeModules"
realModulesPath = package_dir / "utils"

SOCKET_URI = "ws://localhost:8765"


def compileSketch(sketch):
    modulesPath = f"{fakeModulesPath}${realModulesPath}"
    outputFolder = sketch.targetFolder / "__target__"
    command = f"transcrypt -b -n -m -xr -k {sketch.path} -xp {modulesPath} -od {outputFolder}"
    subprocess.run(command, shell=True)

    with open(package_dir / "static" / "index.html") as inputFile, open(
        sketch.targetFolder / "index.html", "w"
    ) as outputFile:
        index = inputFile.read()
        index = index.replace("{{sketch}}", sketch.namejs)
        outputFile.write(index)


class RecompileHandler(FileSystemEventHandler):
    def __init__(self, sketch, function):
        self.last_trigger = time.time()
        self.sketch = sketch
        self.function = function

    def on_modified(self, event):
        new_trigger = time.time()
        if new_trigger - self.last_trigger > 2:
            self.function(self.sketch)
            with connect(SOCKET_URI) as websocket:
                websocket.send("RELOAD")
            self.last_trigger = new_trigger


def launch_recompiler_observer(sketch):
    observer = Observer()
    observer.schedule(RecompileHandler(sketch, compileSketch), sketch.folder, recursive=False)
    observer.start()
