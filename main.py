from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import platform
from kivy.lang import Builder
from zlm import UI

LabelBase.register(
    name="CorrectionBrush", fn_regular="assets/CorrectionBrush-ywW7Y.ttf"
)


class ZeroLenghtMessage(App):
    icon = "assets/icon.png"
    title = "Zero Lenght Message Maker"
    ui = UI()

    def build(self):
        if platform != "android":
            Window.size = (360, 900)
        return Builder.load_file("main.kv")


app = ZeroLenghtMessage()
app.run()
