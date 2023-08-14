from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


class Gece(MDApp):
    def build(self):
        self.title="FitImage"
        global sc
        sc=ScreenManager()
        sc.add_widget(Builder.load_file("main.kv"))
        
        return sc




if __name__=='__main__':
    Gece().run()
