from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


#Window.size = (720, 1200)
Window.size = (360, 600)

from kivy.config import Config
Config.set("kivy", "keyboard_mode", "systemanddock") # включаем виртуальную клавиатуру
from kivymd.theming import ThemeManager

def get_ingridients(m):
    nitro = str(10 * m/1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    dextrose = str(5 * m / 1000)
    salting_time = str(round(m/500*2))

    return {
        "nitro": nitro,
        "salt": salt,
        "starts": starts,
        "dextrose": dextrose,
        "time": salting_time
    }

class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text.partition("\n")[2])

        except:
            mass = 0
        ingridients = get_ingridients(mass)

        self.salt.text = ingridients.get("salt")
        self.nitro.text = ingridients.get("nitro")
        self.starts.text = ingridients.get("starts")
        self.sugar.text = ingridients.get("dextrose")
        self.time.text = ingridients.get("time")
        self.text_input.text = "Введите количество мяса в граммах:\n"





class MyTestApp(App):
    def build(self):
        return Container()

if __name__ == "__main__":
    MyTestApp().run()
