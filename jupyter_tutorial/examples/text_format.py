from manimlib.imports import *

class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.play(Write(text))
        self.wait(3)

