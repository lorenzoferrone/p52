import webview
import sys
import base64
import datetime


class App:
    def __init__(self, sketch):
        self.sketch = sketch

    def save(self, data):
        timestamp = datetime.datetime.now().timestamp()
        fileName = f"{self.sketch.barename}_{timestamp:.0f}.png"

        imgdata = base64.b64decode(data.replace("data:image/png;base64,", ""))
        with open(self.sketch.folder / fileName, "wb") as f:
            f.write(imgdata)


def launch_viewer(sketch):
    def on_closing():
        # minimize traceback output as it is a 'fake' exception
        sys.tracebacklimit = 0
        raise Exception("Quitting!")

    window = webview.create_window(
        sketch.barename, url=str(sketch.targetFolder / "index.html"), js_api=App(sketch), width=1200, height=800
    )
    window.events.closing = window.events.closing + on_closing
    webview.start(debug=True, http_server=True)
