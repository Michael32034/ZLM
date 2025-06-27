from kivy.app import App
from kivy.core.window import Window
from kivy.utils import _get_platform
from kivy.lang import Builder


KV = """
#:import UI zlm.UI
#:import Clipboard kivy.core.clipboard.Clipboard
ScreenManager:
    id: scrman
    Screen:
        name: "hello_screen"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "Вітаю в Шифраторі нульової довжини"
                size_hint: (1., .3)
            Widget:
                size_hint: (1., .4)
            BoxLayout:
                size_hint: (1.,.1)
                orientation: "horizontal"
                Button:
                    text: "Закодувати"
                    on_press: app.root.current = "encode_screen"
                Button:
                    text: "Розкодувати"
                    on_press: app.root.current = "decode_screen"
            Widget:
                size_hint: (1.,.2)
    Screen:
        name: "encode_screen"
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                size_hint: (1.,.8)
                orientation: "vertical"
                Widget:
                    size_hint: (1.,.1)
                Label:
                    size_hint: (1.,.1)
                    text: "Введіть головний текст"
                TextInput:
                    id: main
                    size_hint: (1., .15)
                Label:
                    size_hint: (1.,.1)
                    text: "Введіть секретний текст"
                TextInput:
                    id: secret
                    size_hint: (1.,.15)
                Button:
                    size_hint: (1.,.1)
                    text: "Закодувати"
                    on_press: app.root.ids.output.text = UI.encode(app.root.ids.main.text, app.root.ids.secret.text)
            BoxLayout:
                size_hint: (1., .2)
                orientation: "horizontal"
                Label:
                    size_hint: (.8,1.)
                    id: output
                    text: "Тут буде закодований результат"
                Button:
                    size_hint: (.2,1.)
                    text: "copy"
                    on_press: Clipboard.copy(app.root.ids.output.text)
    Screen:
        name: "decode_screen"
        BoxLayout:
            orientation: "vertical"
            Label:
                size_hint: (1.,.2)
                text: "Введіть закодований текст"
            TextInput:
                size_hint: (1.,.2)
                id: input
            Button:
                size_hint: (1.,.1)
                text: "Розкодувати"
                on_press: app.root.ids.output.text = UI.decode(app.root.ids.input.text)
            Label:
                id: output
                size_hint: (1.,.2)
                text: "Тут буде розкодоване повідомлення"
            Widget:
                size_hint: (1.,.3)
"""


class ZeroLenghtMessage(App):
    icon = "assets/icon.png"
    title = "Zero Lenght Message Maker"

    def build(self):
        if _get_platform() != "android":
            Window.size = (360, 900)
        return Builder.load_string(KV)


app = ZeroLenghtMessage()
app.run()
