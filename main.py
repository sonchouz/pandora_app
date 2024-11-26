from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
Window.clearcolor = get_color_from_hex("#771088")



class MainApp(App):
    def build(self):
        img = Image(source="пандора.png",
                    size_hint=(.5, .5),
                    pos_hint={'center_x': 0.5, 'center_y':0.65}
                    )
        return img
MainApp().run()