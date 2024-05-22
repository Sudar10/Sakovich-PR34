from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class RainbowApp(App):
    def build(self):
        self.colors = {
            "Красный": "#ff0000",
            "Оранжевый": "#ff8800",
            "Желтый": "#ffff00",
            "Зеленый": "#00ff00",
            "Голубой": "#00ffff",
            "Синий": "#0000ff",
            "Фиолетовый": "#ff00ff"
        }

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Цвет", font_size='20sp')
        self.text_input = TextInput(hint_text="Код цвета", readonly=True, font_size='20sp', size_hint_y=None, height=50)

        layout.add_widget(self.label)
        layout.add_widget(self.text_input)

        buttons_layout = BoxLayout()

        for color_name, color_code in self.colors.items():
            btn = Button(text=color_name, background_color=self.hex_to_rgb(color_code) + [1])
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)

        return layout

    def on_button_press(self, instance):
        color_name = instance.text
        color_code = self.colors[color_name]
        self.label.text = color_name
        self.text_input.text = color_code

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4)]

if __name__ == "__main__":
    RainbowApp().run()
