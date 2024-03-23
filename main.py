from kivy.lang import Builder
from app import ElearningApp

Builder.load_file("main_screen.kv")
Builder.load_file("alphabet.kv")
Builder.load_file("numbers.kv")
Builder.load_file("character.kv")
Builder.load_file("words.kv")
Builder.load_file("phrases.kv")
Builder.load_file("paragraph.kv")

if __name__ == '__main__':
    ElearningApp().run()