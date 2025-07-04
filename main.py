from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang import Builder
from zlm import UI


KV = """
#:import Clipboard kivy.core.clipboard.Clipboard
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import dp kivy.metrics.dp
ScreenManager:
    id: scrman
    Screen:
        name: "hello_screen"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "Вітаю в ZLM"
                size_hint: (1., .3)
                font_size: 30
            Widget:
                size_hint: (1., .4)
            BoxLayout:
                size_hint: (1.,.1)
                orientation: "horizontal"
                Widget:
                    size_hint: (0.05, 1)
                Button:
                    background_normal: ""
                    background_color: get_color_from_hex("#00BD16")
                    size_hint: (0.4, 1)
                    text: "Закодувати"
                    on_press: app.root.current = "encode_screen"
                Widget:
                    size_hint: (0.1, 1)
                Button:
                    background_normal: ""
                    background_color: get_color_from_hex("#2F7DE7")
                    size_hint: (0.4, 1)
                    text: "Розкодувати"
                    on_press: app.root.current = "decode_screen"
                Widget:
                    size_hint: (0.05, 1)
            Widget:
                size_hint: (1.,.2)
    Screen:
        name: "encode_screen"
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                size_hint: (1.,.7)
                orientation: "vertical"
                BoxLayout:
                    size_hint: (1.,.1)
                    orientation: "horizontal"
                    Widget:
                        size_hint: (.8,1.)
                        background_color: get_color_from_hex("#007F16")
                    Button:
                        size_hint: (.2, 1)
                        text: "Home"
                        on_press: app.root.current = "hello_screen"
                Label:
                    size_hint: (1.,.1)
                    text: "Введіть головний текст"
                    background_color: get_color_from_hex("#007F16")
                TextInput:
                    id: main
                    size_hint: (1., .15)
                Label:
                    size_hint: (1.,.1)
                    text: "Введіть секретний текст"
                    background_color: get_color_from_hex("#007F16")
                TextInput:
                    id: secret
                    size_hint: (1.,.15)
                Button:
                    size_hint: (1.,.1)
                    text: "Закодувати"
                    on_press: app.root.ids.enc_output.text = app.ui.encode(app.root.ids.main.text, app.root.ids.secret.text)
                Widget:
                    size_hint: (1, .1)
                    background_color: get_color_from_hex("#007F16")
            BoxLayout:
                size_hint: (1., .1)
                orientation: "horizontal"
                Label:
                    size_hint: (.8,1.)
                    id: enc_output
                    text: "Тут буде закодований результат"
                Button:
                    size_hint: (.2,1.)
                    text: "copy"
                    font_size: 30
                    on_press: Clipboard.copy(app.root.ids.enc_output.text)
            Widget:
                size_hint: (1., .2)
    Screen:
        name: "decode_screen"
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                size_hint: (1.,.1)
                orientation: "horizontal"
                Widget:
                    size_hint: (.8,1.)
                Button:
                    size_hint: (.2, 1)
                    text: "Home"
                    on_press: app.root.current = "hello_screen"
            Label:
                size_hint: (1.,.1)
                text: "Введіть закодований текст"
            TextInput:
                size_hint: (1.,.2)
                id: input
            Button:
                size_hint: (1.,.1)
                text: "Розкодувати"
                on_press: app.root.ids.dec_output.text = app.ui.decode(app.root.ids.input.text)
            Label:
                id: dec_output
                size_hint: (1.,.2)
                text: "Тут буде розкодоване повідомлення"
            Widget:
                size_hint: (1.,.4)
"""


class ZeroLenghtMessage(App):
    icon = "assets/icon.png"
    title = "Zero Lenght Message Maker"
    ui = UI()

    def build(self):
        if platform != "android":
            Window.size = (360, 900)
        return Builder.load_string(KV)


app = ZeroLenghtMessage()
app.run()
