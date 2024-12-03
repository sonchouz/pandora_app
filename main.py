from kivy.config import Config
Config.set("graphics", "resizable", False)
Config.set("graphics", "height", 600)
Config.set("graphics", "width", 300)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
Builder.load_string("""
<StartScreen>:
    GridLayout:
        cols: 1
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'пандора.png'
                size_hint: (0.8, None)
                pos_hint: {'center_x': .5, 'y': .2}

        BoxLayout:
            Label:
                text: 'Пандора'
                font_size: 48
                font_name: 'Lora-Bold'
                pos_hint: {'top': 1.3}
        BoxLayout:
            Label:
                text: 'Танцевальный дом'
                font_size: 24
                font_name: 'Lora'
                pos_hint: {'top': 2.12}
""")

# Declare both screens
class StartScreen(Screen):
    Window.clearcolor = get_color_from_hex("#771088")


class SettingsScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MainApp().run()

