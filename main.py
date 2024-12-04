from kivy.config import Config
Config.set("graphics", "width", 300)
Config.set("graphics", "height", 600)
Config.set("graphics", "resizable", False)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.lang import Builder
Builder.load_file("my.kv")

# Declare both screens
class StartScreen(Screen):
    Window.clearcolor = get_color_from_hex("#771088")
    def build(self):
        return StartScreen()
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