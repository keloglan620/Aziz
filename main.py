from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv = '''
<MyWidget>:
    orientation: 'vertical'
    padding: 20
    spacing: 20

    TextInput:
        id: name_input
        hint_text: "Adınızı girin"
        multiline: False

    Button:
        text: "GÖSTER"
        on_press: root.display_name()

    Label:
        id: name_label
        text: ""
        font_size: '20sp'
'''

Builder.load_string(kv)

class MyWidget(BoxLayout):
    def display_name(self):
        user_name = self.ids.name_input.text.strip()
        if user_name:
            self.ids.name_label.text = f"Merhaba, {user_name.upper()}!"
        else:
            self.ids.name_label.text = "Lütfen bir isim girin!"

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()