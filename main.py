from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
Window.clearcolor = (0.05, 0.1, 0.15, 1)
class ElimuYetuApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical', padding=20, spacing=20)
        main.add_widget(Label(text='ELIMU YETU UNIVERSE v4.0\nMAARIFA YA UISLAMU', font_size='24sp', size_hint_y=0.3))
        btn = Button(text='1. MAARIFA YA UISLAMU - QUR-AN & HADITH', size_hint_y=0.2, background_color=(0, 0.7, 0.3, 1))
        main.add_widget(btn)
        main.add_widget(Label(text='Toleo la Pro - APK Inafanya Kazi', size_hint_y=0.5))
        return main
if __name__ == '__main__': ElimuYetuApp().run()  
