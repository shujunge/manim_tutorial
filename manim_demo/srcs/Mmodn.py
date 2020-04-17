from manimlib.imports import *

class my_MmodN(Scene):

    def construct(self):

        circle, lines = self.get_m_mod_n_objects(x=10, y=120)

        zz = VGroup(circle, lines).to_edge(RIGHT, buff=1)

        self.play(ShowCreation(zz))
        self.wait()
        self.play( LaggedStartMap(ShowCreation, lines, run_time=4) )

        lines_c = lines.copy()
        lines_c.set_color(PINK)
        lines_c.set_stroke(width=3)
        self.play( LaggedStartMap(ShowCreationThenDestruction, lines_c, run_time=6 ))
        self.wait()
        self.play( Uncreate(VGroup(circle, lines)), run_time=3)
        self.wait()

    def get_m_mod_n_objects(self, x, y):

        circle = Circle().set_height(FRAME_HEIGHT)
        circle.scale(0.9)
        my_VGroup = VGroup()
        for index in range(y):
            start_point = circle.point_from_proportion((index % y)/y)
            end_point = circle.point_from_proportion(((index*x)%y)/y)
            line = Line(start_point, end_point).set_stroke(width=1).set_color(RED)
            my_VGroup.add(line)

        return [circle, my_VGroup]
