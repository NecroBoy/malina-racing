# Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.image import Image, AsyncImage
from kivy_deps import sdl2, glew
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.graphics.context_instructions import PopMatrix, PushMatrix
from kivy.graphics import Rotate

Config.set('graphics', 'width', '256')
Config.set('graphics', 'height', '256')
Config.set('graphics', 'resizable', '0')
Config.write()

import pygame
import time

Builder.load_string("""
<MyScreenManager>:

    FirstScreen:
        id: first_screen 
<FirstScreen>:
    canvas:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    RelativeLayout
        Image:
            id: image
            source: 'wheel.png'
            size_hint: None,None
            size: 256,256
            canvas.before:
                PushMatrix
                Rotate:
                    angle: root.angle
                    origin: self.center

""")

class JSManager():

    def __init__(self):
        pygame.init()
        #pygame.joystick.init()
        try:
            self.js = pygame.joystick.Joystick(0)
        except:
            print('could not find joystick')
            exit()
        self.js.init()
        self.axes = self.js.get_numaxes()
        self.buttons = self.js.get_numbuttons()

    def update_axes(self):
        '''get joystick values'''
        #pygame.event.get is needed to update axis values
        pygame.event.get()
        axes_values = []
        #self.js.init()
        for a in range(self.axes):
            axis = self.js.get_axis(a)
            axes_values.append(axis)
        return axes_values

    def update_buttons(self):
        '''get button presses'''
        pygame.event.get()
        button_presses = []
        for b in range(self.buttons):
            button = self.js.get_button(b)
            button_presses.append(button)
        return button_presses



class FirstScreen(Screen):
    
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        event = Clock.schedule_interval(self.main, 0)
 

    



    def main(self, *args):
        global old





        js = JSManager()



        vals = js.update_axes()
        buts = js.update_buttons()


        print(vals[0] * 450 - 1)

        self.angle = vals[0] * 450 * -1



class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
  

class SwitchingScreenApp(App):
    

    def build(self):
        self.title = 'Malina Racing'
        return MyScreenManager()

if __name__ == "__main__":
    SwitchingScreenApp().run()

















