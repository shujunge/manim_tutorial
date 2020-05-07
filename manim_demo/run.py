from manimlib.imports import *
from srcs.utils import run
from datetime import *

from srcs.Pythagoras import Pythagoras
from srcs.Dragon import  Dragon
from srcs.serise import *
from srcs.demo import CompareGraph
from srcs.pi_day import HistoryOfOurPeople, AskPuzzle
from srcs.my_textfonts import my_fonts_Demo, Intro, Text_demo, Submojects_demo
from srcs.Code_line import TestDecimalNumberText, RoundedRectangleIllustration,TryLinedCode
from srcs.ThreeD_demo import basic_3d_shape, update_text_timeing
from srcs.TwoD_demo import my_numberplane
from srcs.move_camera import change_camera_size
from srcs.new_VMobject_demo import LevyScene
from srcs.Trident_of_Newton import TridentOfNewton
from srcs.fourier_series import FourierOfTexPaths, ManyFourierOfTexSymbol, ManyFourierOfTextSymbol
from srcs.ZoomScene import ZoomedSceneExample, ZoomDemo


if __name__ == '__main__':
    run(your_module = [ZoomDemo], l=True, gif =False)
