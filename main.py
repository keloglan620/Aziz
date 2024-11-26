from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)

# Complete code in one Python file with KV design inside
kv = '''
<MyLayout>:
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            id: calc_input
            text: "0"
            halign: "right"
            font_size: 65
            size_hint: (1, .15)

        GridLayout:
            cols: 4
            rows: 5

            # Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "%"
                on_press: root.math_sign("%")

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "C"
                on_press: root.clear()

            Button:
                id: clear
                size_hint: (.2, .2)
                font_size: 32
                text: u"\u00AB"
                on_press: root.remove()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "/"
                on_press: root.math_sign("/")

            # Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "7"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(7)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "8"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(8)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "9"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(9)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "x"
                on_press: root.math_sign("*")

            # Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "4"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(4)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "5"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(5)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "6"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(6)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "-"
                on_press: root.math_sign("-")

            # Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "1"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(1)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "2"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(2)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "3"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(3)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+"
                on_press: root.math_sign("+")

            # Row
            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+/-"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.pos_neg()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "0"
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.button_press(0)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "."
                background_color: (157/255, 157/255, 157/255, 1)
                on_press: root.dot()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "="
                on_press: root.equals()
'''

class MyLayout(Widget):
    calc_input = ObjectProperty(None)

    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, num):
        current_text = self.ids.calc_input.text
        if current_text == "0":
            self.ids.calc_input.text = str(num)
        else:
            self.ids.calc_input.text += str(num)

    def math_sign(self, sign):
        current_text = self.ids.calc_input.text
        if current_text[-1] not in "+-*/":
            self.ids.calc_input.text += sign

    def pos_neg(self):
        current_text = self.ids.calc_input.text
        if current_text.startswith("-"):
            self.ids.calc_input.text = current_text[1:]
        else:
            self.ids.calc_input.text = "-" + current_text

    def dot(self):
        current_text = self.ids.calc_input.text
        if "." not in current_text:
            self.ids.calc_input.text += "."

    def remove(self):
        current_text = self.ids.calc_input.text
        self.ids.calc_input.text = current_text[:-1] if len(current_text) > 1 else "0"

    def equals(self):
        try:
            current_text = self.ids.calc_input.text
            result = str(eval(current_text.replace('x', '*').replace('%', '/100')))
            self.ids.calc_input.text = result
        except:
            self.ids.calc_input.text = "Error"

class CalculatorApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    CalculatorApp().run()
