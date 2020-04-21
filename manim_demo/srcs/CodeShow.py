from manimlib.imports import *

class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
        },
        # 'font': 'DFLianLian SC2 W2',
        'size': 0.36,
        'color': WHITE,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Codeshow(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }

    def construct(self):
        # 坐标系
        plane = NumberPlane(axis_config={"stroke_color": BLACK}, plot_depth=-5) \
            .add_coordinates(y_vals=[1, 2, 3, -1, -2])

        # 字幕
        captions = [
            "使用shift方法可以根据传入的vector移动物体",
            "先将图片添加到画面中",
            "调用shift(LEFT*5)向左移动五个单位",
            "同理可以沿任意方向移动任意单位",
            "shift中可以传入多个vector参数，会先将其全部相加，再进行移动",
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='DFLianLian SC2 W2', size=0.32, color= BLACK).to_edge(UP * 1.2) \
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )

        # 代码块及代码
        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=BLACK, fill_opacity=0.95, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        method = CodeLine("shift(*vector)", size=0.5).next_to(tex_bg.get_top(), DOWN)
        line = Line(LEFT, RIGHT, stroke_width=1, stroke_color=GRAY).set_width(5.4).next_to(method, DOWN)
        codes = [
            "1 self.add(mob)",
            "2 mob.shift(LEFT*5)",
            "3 mob.shift(UP*2+RIGHT*3)",
            "4 mob.shift(DOWN*2, RIGHT*2)"
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(line, DOWN, buff=0.5)

        # 移动向量箭头
        arrow1 = Arrow(ORIGIN, LEFT * 5, color=ORANGE, buff=0, plot_depth=-1)
        arrow2 = Arrow(LEFT * 5, LEFT * 2 + UP * 2, color=ORANGE, buff=0, plot_depth=-1)
        arrow3_0 = Arrow(LEFT * 2 + UP * 2, LEFT * 2, color=GREEN, buff=0, plot_depth=-1)
        arrow3_1 = Arrow(LEFT * 2, ORIGIN, color=GREEN, buff=0, plot_depth=-1)
        arrow3 = Arrow(LEFT * 2 + UP * 2, ORIGIN, color=ORANGE, buff=0, plot_depth=-1)


        # self.add(plane, tex_bg, method, line, codes_mob, arrow1, arrow2, arrow3_0, arrow3_1, arrow3, mob1, mob2)

        self.add(plane)
        self.play(FadeInFromDown(tex_bg))
        self.play(
            Write(captions_mob[0]),
            Write(method)
        )
        self.play(Write(line))
        self.wait(4)
        self.play(
            Transform(captions_mob[0], captions_mob[1])
        )
        self.play(Write(codes_mob[0]))
        self.wait(4)

        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.play(Write(codes_mob[1]))

        self.play(Write(arrow1))


        self.wait(2)
        self.play(FadeOut(arrow1))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.play(Write(codes_mob[2]))

        self.play(Write(arrow2))


        self.wait(2)
        self.play(FadeOut(arrow2))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.play(Write(codes_mob[3]))

        self.play(Write(arrow3_0))
        self.play(Write(arrow3_1))
        self.wait()
        self.play(Write(arrow3), FadeOut(arrow3_0), FadeOut(arrow3_1))

        self.wait(2)
        self.play(FadeOut(arrow3))
        self.wait(2)
        self.play(FadeOut(Group(captions_mob[0], tex_bg, line, method, codes_mob)))
        self.wait(2)


class VideoProgressBar(Scene):
    CONFIG = {
        'methods_dict': {
            '序言': '0025',
            'shift+move_to': '0210',
            'scale': '0402',
            'rotate': '0504',
            'flip': '0712',
            'stretch': '0901',
            'to_corner': '1014',
            'align_to': '1129',
            'next_to': '1227',
            'set_width+set_height': '1500',
            ' ': '1659'},
        'total_time': '1724',
        'text_font': "DFLianLian SC2 W2",
        'color_list': [BLUE, PINK, RED, ORANGE, GREEN],
        'bar_width': 20,
        'text_size': 0.15,
    }

    def construct(self):
        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t) / func_time(self.total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2

        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in self.methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(self.total_time))

        self.colors = color_gradient(self.color_list, len(self.methods_dict) + 1)

        self.lines = VGroup(
            *[Line(p_list[i], p_list[i + 1] - 0.02 * RIGHT, color=self.colors[i], stroke_width=self.bar_width) for i in
              range(len(self.methods_dict) + 1)])
        self.lines.to_edge(DOWN * 0.22, buff=1)
        self.texts = VGroup(
            *[Text(t, color=BLACK, font=self.text_font, size=self.text_size, weight=BOLD) for t in self.methods_dict.keys()],
            plot_depth=1)

        for i in range(len(self.methods_dict)):
            self.texts[i].move_to(self.lines[i + 1])

        self.play(LaggedStartMap(FadeInFromDown,self.lines,run_time=4), LaggedStartMap(ShowCreation,self.texts))
        self.wait()

