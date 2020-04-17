from manimlib.imports import *
from manimlib.constants import *


class my_text_show(Scene):
    def construct(self):

        position = [ORIGIN, UP, LEFT, RIGHT, DOWN]
        my_colors = [RED, BLUE, GREEN, "#DC28E2",ORANGE]
        title = TextMobject("第一题：")
        title.to_corner(UL)


        base = -3
        ring = Annulus(inner_radius=.4, outer_radius=1, color=BLUE )
        square = Square(color=ORANGE, fill_color=ORANGE, fill_opacity=0.5, side_length= 1 )
        rect = Rectangle(height =2, width=1, color= PINK, fill_color=PINK, fill_opacity=0.5 )
        line01 = Line(np.array([base, 3.6, 0]), np.array([base, 2, 0]), color= BLUE)
        line02 = Line(np.array([-1+base, 2, 0]), np.array([-1+base, 1, 0]), color= BLUE)
        line03 = Line(np.array([1+base, 2, 0]), np.array([1+base, 0.5, 0]), color= BLUE)

        # 设置位置
        base  = 3*LEFT
        ring.shift(UP*2+base)
        square.shift(LEFT+ base + 0.5 *UP)
        square_downarrow = Arrow(square.get_center(), square.get_center() + DOWN * 1.5, color= YELLOW,buff=0)
        square_uparrow = Arrow(square.get_center(), square.get_center() + UP * 1.5 , color= YELLOW, buff=0)
        square_g = TexMobject("G_{\mbox{物} }")
        square_f = TexMobject("F_{\mbox{拉}}")
        square_g.next_to(square_downarrow.get_bottom(), RIGHT)
        square_f.next_to(square_uparrow.get_top(), LEFT)

        rect.shift(RIGHT + DOWN * 0.5 + base)
        rect_downarrow = Arrow(rect.get_center(), rect.get_center() + DOWN * 2.5, color= BLUE, buff=0)
        rect_uparrow = Arrow(rect.get_center(), rect.get_center() + UP * 2.5 , color= BLUE, buff=0)
        rect_g = TexMobject("G_{\mbox{物} }",color=BLUE)
        rect_f = TexMobject("F_{\mbox{拉}}",color=BLUE)
        rect_g.next_to(rect_downarrow.get_bottom(), RIGHT)
        rect_f.next_to(rect_uparrow.get_top(), RIGHT)

        ## 动画显示
        self.play(FadeIn(title))
        self.wait()
        self.add(line01)
        self.play(GrowFromCenter(ring))
        self.wait(0.5)
        self.play(FadeIn(line02), FadeIn(line03))
        self.wait(0.5)
        self.play(FadeInFromDown(square), FadeInFromDown(rect))
        self.play(Rotating(square), Rotating(rect))
        self.wait()


        self.play(FadeInFromDown(square_downarrow))
        self.wait()
        self.play(Transform(square.copy(), square_g))
        self.wait()
        self.play(FadeInFromDown(square_uparrow))
        self.wait()
        self.play(Transform(square.copy(), square_f))
        self.wait()


        self.play(FadeInFromDown(rect_downarrow))
        self.wait()
        self.play(Transform(rect.copy(), rect_g))
        self.wait()
        self.play(FadeInFromDown(rect_uparrow))
        self.wait()
        self.play(Transform(rect.copy(), rect_f))
        self.wait()

        print(rect.get_right())


        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

