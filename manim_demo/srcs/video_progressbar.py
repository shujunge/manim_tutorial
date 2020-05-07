from manimlib.imports import *

class DownProgressBar(Scene):
    def construct(self):
        methods_dict = {
            '颜色的表示': '0022',
            '颜色表示法的转换': '0125',
            '颜色的运算函数': '0305',
            '给物体设置颜色': '0443',
            '子物体的梯度上色': '0600',
            '光泽和渐变色': '0701',
            ' ': '0810'
        }
        total_time = '0822'
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t)/func_time(total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(total_time))


        colors = color_gradient([BLUE, PINK, RED, ORANGE, GREEN], len(methods_dict)+1)

        lines = VGroup(*[Line(p_list[i], p_list[i+1]-0.02*RIGHT, color=colors[i], stroke_width=20) for i in range(len(methods_dict)+1)])
        lines.to_edge(DOWN * 0.22, buff=1)
        texts = VGroup(*[Text(t, color=WHITE,  size=0.14) for t in methods_dict.keys()], plot_depth=1)
        text = Text('空降', color=WHITE,size=0.14).to_edge(DOWN * 0.132, buff=1).to_edge(LEFT, buff=0.2)
        # text[1].shift(RIGHT*0.03)
        # text[0].shift(LEFT*0.01)

        my_svg = SVGMobject("../srcs/figs/tortoise.svg",color=Color("#00ffff")).scale(0.16).set_color_by_gradient([GREEN,RED])
        line_path = Line(p_list[0], p_list[8]).to_edge(DOWN*0.3, buff=1)

        for i in range(len(methods_dict)):
            texts[i].move_to(lines[i+1])

        self.add(lines, texts, text)
        self.wait()
        self.play(MoveAlongPath(my_svg, line_path), run_time=10)
        self.wait()