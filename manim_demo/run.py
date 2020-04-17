from manimlib.imports import *
from srcs.utils import run

from srcs.Pythagoras import Pythagoras
from srcs.Dragon import  Dragon
from srcs.serise import *
from srcs.demo import CompareGraph
from srcs.pi_day import HistoryOfOurPeople, AskPuzzle
from srcs.my_textfonts import my_fonts_Demo,Intro

from srcs.threed_demo import basic_3d_shape, update_text_timeing

class my_pi(Scene):

    def construct(self):
        title = TextMobject("Learning Algorithm")
        title.scale(2)
        title.bg = SurroundingRectangle(title, color=BLUE, fill_color=BLUE, fill_opacity=.5)

        piCreature = PiCreature(color=BLUE_C, height=1)

        piCreature.next_to(title, DOWN + LEFT)

        self.play(Write(title), FadeInFrom(piCreature, LEFT), ApplyMethod(piCreature.look_at, title))
        self.wait()
        self.play( Blink(piCreature))
        piCreature.change("happy")
        self.wait()


if __name__ == '__main__':

    run(your_module = [update_text_timeing])
    # print(basic_3d_shape.__base__)
