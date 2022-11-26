from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
class Container(GridLayout):
    def biomass_minus(self):
        if int(self.ids.biomass.text) == 0:
            pass
        else:
            num = int(self.ids.biomass.text) - 1
            self.ids.biomass.text = str(num)
    def biomass_plus(self):
        num = int(self.ids.biomass.text) + 1
        self.ids.biomass.text = str(num)
    #ОСБ
    def osb_minus(self):
        if int(self.ids.osb.text) == 0:
            pass
        else:
            num = int(self.ids.osb.text) - 1
            self.ids.osb.text = str(num)
    def osb_plus(self):
        num = int(self.ids.osb.text) + 1
        self.ids.osb.text = str(num)
    # Чиппер
    def сhipper_minus(self):
        if int(self.ids.сhipper.text) == 0:
                pass
        else:
            num = int(self.ids.сhipper.text) - 1
            self.ids.сhipper.text = str(num)
    def сhipper_plus(self):
        num = int(self.ids.сhipper.text) + 1
        self.ids.сhipper.text = str(num)
    # Дисковая
    def disk_minus(self):
        if int(self.ids.disk.text) == 0:
                pass
        else:
            num = int(self.ids.disk.text) - 1
            self.ids.disk.text = str(num)
    def disk_plus(self):
        num = int(self.ids.disk.text) + 1
        self.ids.disk.text = str(num)
    # Роликовая
    def roller_minus(self):
        if int(self.ids.roller.text) == 0:
                pass
        else:
            num = int(self.ids.roller.text) - 1
            self.ids.roller.text = str(num)
    def roller_plus(self):
        num = int(self.ids.roller.text) + 1
        self.ids.roller.text = str(num)
    # Рециклы
    def recycling_minus(self):
        if int(self.ids.recycling.text) == 0:
                pass
        else:
            num = int(self.ids.recycling.text) - 1
            self.ids.recycling.text = str(num)
    def recycling_plus(self):
        num = int(self.ids.recycling.text) + 1
        self.ids.recycling.text = str(num)
    # Сброс
    def reset(self):
        self.ids.biomass.text = '0'
        self.ids.osb.text = '0'
        self.ids.сhipper.text = '0'
        self.ids.disk.text = '0'
        self.ids.roller.text = '0'
        self.ids.recycling.text = '0'

class MyApp(App):
    def build(self):
        return Container()
if __name__ == '__main__':
    MyApp().run()