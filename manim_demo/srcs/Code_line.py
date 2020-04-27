from manimlib.imports import *

from manimlib.imports import *

class LinedCode(Text):
    CONFIG = {
        'size'         : 0.5,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
        'ln_color'     : GRAY,
    }

    def __init__(self, *text, **config):
        digest_config(self, config)
        res_text = ''
        i = 1
        for each_text in text:
            res_text += str(i) + '  ' + each_text + '\n'
            self.t2c['{}  '.format(i)] = self.ln_color
            i = i + 1
        super(LinedCode, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)

class Code(Text):
    CONFIG = {
        'font'         : 'Monaco for Powerline',
        'size'         : 0.5,
        'color'        : WHITE,
        'stroke_color' : WHITE,
        'stroke_weight': 0,
    }

    def __init__(self, *text, **config):
        res_text = ''
        for each_text in text:
            res_text += each_text + '\n'
        super(Code, self).__init__(res_text, **config)
        self.set_stroke(self.stroke_color, self.stroke_weight)

class TryLinedCode(Scene):
    def construct(self):
        code = LinedCode(
            "#include <bits/stdc++.h>",
            "using namespace std;",
            "",
            "int main() {",
            "    printf(\"Hello World\\n\");",
            "    return 1;",
            "}",
            t2c={
            '#include <' : BLUE,
            '>' : BLUE,
            'std' : YELLOW,
            'bits/stdc++.h' : GREEN,
            'using' : ORANGE,
            'namespace' : PURPLE,
            ';' : BLUE,
            'for' : BLUE,
            'if' : BLUE,
            'int' : PURPLE,
            '(' : BLUE,
            ')' : BLUE,
            '{' : BLUE,
            '}' : BLUE,
            'return' : BLUE,
            '0' : ORANGE,
            'main' : '#214FB7',
            'printf' : '#214FB7',
            '\"' : BLUE,
            'Hello World' : GREEN,
            '\\n' : BLUE,
        }
        )
        self.play(Write(code))

class TryCode(Scene):
    def construct(self):
        code = Code(
            "#include <bits/stdc++.h>",
            "using namespace std; ",
        )
        self.play(Write(code))


class CodeLine(Text):
    CONFIG = {
        't2c': {
            # 'x': average_color(BLUE, PINK),
            # 'y': average_color(BLUE, PINK),
            # 'z': average_color(BLUE, PINK),
            'True': ORANGE,
            'False': ORANGE,
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
            'sheen': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'play': BLUE_D,
            'round_corners': BLUE_D,
            'corner_radius': BLUE_D,
            'side_length': BLUE_D,
            'stretch': BLUE_D,
            'color': BLUE_D,
            'stroke': BLUE_D,
            'opacity': BLUE_D,
            'stroke_width': BLUE_D,
            'stroke_color': BLUE_D,
            'stroke_opacity': BLUE_D,
            'sheen_factor': BLUE_D,
            'sheen_direction': BLUE_D,
            'PURPLE_C': PURPLE_C,
            'set_stroke': BLUE_D,
            'width': BLUE_D,
            'height': BLUE_D,
            'Rectangle': PURPLE_C,
            'RoundedRectangle':PURPLE_C,
            'Square': PURPLE_C,
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
            '#FF0000': '#FF0000',
            '#66CCFF': '#66CCFF',
            'GREEN_B': GREEN_B,
            'BLUE_B': BLUE_B,
            '~': '#F0F0F0',
        },
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
        'stroke_width': 0,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)
        pass

class RectangleIllustration(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        captions = [
            '这是一个宽度为3，高度为5的长方形',
            '控制形状的有两个参数：width和height（宽度和高度）',
            'width就是宽度，height就是高度',
            'color可以改变矩形颜色',
            'opacity调整其透明度，取值范围[0,1]',
            'stroke相关的参数可以调整笔画粗细、颜色、透明度等',
            'stroke_width:粗细,stroke_color:颜色,stroke_opacity:透明度',
            'sheen的效果是添加渐变',
            '其中的sheen_factor可以调整渐变大小',
            'sheen_direction调整渐变方向',
        ]

        codelines = [
            "rectangle=Rectangle(",# 0
            "~~~~height=5,",# 1
            "~~~~width=3,",# 2
            "~~~~height=4,",# 3
            "~~~~width=3,",# 4
            "~~~~height=4,",# 5
            "~~~~width=5,",# 6
            "~~~~height=2,",# 7
            "~~~~width=3,",# 8
            "~~~~color='#FF0000',",# 9
            "~~~~opacity=1.0,",# 10
            "~~~~color='#66CCFF',",# 11
            "~~~~opacity=0.2,",# 12
            "~~~~opacity=0.5,",# 13
            "~~~~opacity=1.0,",# 14
            "~~~~stroke_color=PURPLE_C,",# 15
            "~~~~stroke_width=20,",# 16
            "~~~~stroke_opacity=1,",# 17
            "~~~~stroke_color=GREEN_B,",# 18
            "~~~~stroke_width=10,",# 19
            "~~~~stroke_opacity=0.5,",# 20
            "~~~~stroke_opacity=0.0,",#21
            "~~~~sheen_factor=0.2,",# 22
            "~~~~sheen_direction=UR,",#23
            "~~~~sheen_factor=0.4,",# 24
            "~~~~sheen_direction=UL,",# 25
            ")",# 26
            "~~~~stroke_color=PURPLE_C,",# 27
        ]

        captions_mob = VGroup(
            *[
                CodeLine(cap, size=0.36,plot_depth=5,color=DARKER_GRAY).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codelines_mob = VGroup(
            *[
                CodeLine(codeline,size=0.36)
                for codeline in codelines
            ]
        )

        code_bg = Rectangle(
            height=7,
            width=6,
            stroke_width=1,
            stroke_color=GRAY,
            fill_color=LIGHT_GREY,
            fill_opacity=0.25,
            plot_depth=-1
        ).to_edge(RIGHT, buff=LARGE_BUFF)

        self.play(FadeIn(code_bg))

        rec = Rectangle(
            stroke_width=1,
            stroke_color=PURPLE_C,
            fill_color="66CCFF",
            fill_opacity=1,
            height=5,
            width=3,
        ).to_edge(LEFT, buff=LARGE_BUFF).shift(RIGHT)

        for each in range(len(codelines_mob)):
            if each == 0:
                codelines_mob[each].next_to(code_bg, direction=RIGHT, aligned_edge=UP).shift(np.array([-code_bg.get_width(),-0.3,0]))
            elif each in [1,3,5,7]:
                codelines_mob[each].next_to(codelines_mob[0], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [2,4,6,8]:
                codelines_mob[each].next_to(codelines_mob[each-1], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [9,11]:
                codelines_mob[each].next_to(codelines_mob[2], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [10,12,13,14]:
                codelines_mob[each].next_to(codelines_mob[9], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [15,18,27]:
                codelines_mob[each].next_to(codelines_mob[14], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [16,19]:
                codelines_mob[each].next_to(codelines_mob[15], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [17,20,21]:
                codelines_mob[each].next_to(codelines_mob[16], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [22,24]:
                codelines_mob[each].next_to(codelines_mob[21], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            elif each in [23,25]:
                codelines_mob[each].next_to(codelines_mob[22], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
            # codelines_mob[each].next_to(code_bg, direction=RIGHT, aligned_edge=UP).shift(np.array([-code_bg.get_width(),-0.3,0]))
            # , DOWN, buff=MED_SMALL_BUFF

        brace_right = Brace(rec, direction=RIGHT,fill_color=LIGHT_GREY, fill_opacity=1)\
            .add_updater(lambda x: x.become(
                Brace(rec, direction=RIGHT,fill_color=LIGHT_GREY, fill_opacity=1)
            ))
        brace_up = Brace(rec, direction=UP,fill_color=LIGHT_GREY, fill_opacity=1)\
            .add_updater(lambda x: x.become(
                Brace(rec, direction=UP,fill_color=LIGHT_GREY, fill_opacity=1)
            ))

        self.play(FadeIn(codelines_mob[0]), run_time=0.8)
        self.play(FadeIn(rec), run_time=0.8)
        self.play(Write(captions_mob[0]))
        self.add(VGroup(brace_up, brace_right))
        up_label = CodeLine('3').next_to(brace_up, UP, buff=SMALL_BUFF)
        right_label = CodeLine('5').next_to(brace_right, RIGHT, buff=SMALL_BUFF)
        self.play(FadeIn(VGroup(up_label, right_label)), run_time=0.8)
        self.play(Write(codelines_mob[1]), run_time=0.5)
        self.play(Write(codelines_mob[2]), run_time=0.5)
        self.play(Write(codelines_mob[26].next_to(codelines_mob[2], DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)), run_time=0.5)
        self.wait(2)
        self.play(Transform(captions_mob[0], captions_mob[1]))
        self.wait(2)
        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.play(
            Transform(codelines_mob[1], codelines_mob[3]),
            Transform(codelines_mob[2], codelines_mob[4]),
        )
        self.play(
            rec.set_height, {'height': 4, 'stretch':True},
            Transform(right_label, CodeLine('4').add_updater(lambda x: x.become(CodeLine('4').next_to(brace_right, RIGHT, buff=SMALL_BUFF)))),
            Transform(up_label, CodeLine('3').add_updater(lambda x: x.become(CodeLine('3').next_to(brace_up, UP, buff=SMALL_BUFF))))
        )
        self.wait(1.8)
        self.play(
            Transform(codelines_mob[1], codelines_mob[5]),
            Transform(codelines_mob[2], codelines_mob[6]),
        )
        self.play(
            rec.set_width, {'width': 5, 'stretch': True},
            Transform(right_label, CodeLine('4').add_updater(lambda x: x.become(CodeLine('4').next_to(brace_right, RIGHT, buff=SMALL_BUFF)))),
            Transform(up_label, CodeLine('5').add_updater(lambda x: x.become(CodeLine('5').next_to(brace_up, UP, buff=SMALL_BUFF))))
)
        self.wait(1.8)
        self.play(
            Transform(codelines_mob[1], codelines_mob[7]),
            Transform(codelines_mob[2], codelines_mob[8]),
        )
        self.play(
            rec.set_height, {'height': 2, 'stretch': True},
            rec.set_width, {'width': 3, 'stretch': True},
            Transform(right_label, CodeLine('2').add_updater(lambda x: x.become(CodeLine('2').next_to(brace_right, RIGHT, buff=SMALL_BUFF)))),
            Transform(up_label, CodeLine('3').add_updater(lambda x: x.become(CodeLine('3').next_to(brace_up, UP, buff=SMALL_BUFF))))
)
        self.wait(1.8)
        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.play(codelines_mob[26].next_to, {'mobject_or_point':codelines_mob[10], 'direction':DOWN, 'buff': MED_SMALL_BUFF, 'aligned_edge': LEFT})
        self.play(Write(codelines_mob[9]), run_time=0.5)
        self.play(Write(codelines_mob[10]), run_time=0.5)
        self.play(rec.set_color, "#FF0000")
        self.wait(1.8)
        self.play(Transform(codelines_mob[9], codelines_mob[11]))
        self.play(rec.set_color, "#66CCFF")
        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.play(Transform(codelines_mob[10], codelines_mob[12]))
        self.play(rec.set_opacity, 0.2)
        self.wait(1.8)
        self.play(Transform(codelines_mob[10], codelines_mob[13]))
        self.play(rec.set_opacity, 0.5)
        self.play(Transform(codelines_mob[10], codelines_mob[14]))
        self.play(codelines_mob[26].next_to, {'mobject_or_point':codelines_mob[17], 'direction':DOWN, 'buff': MED_SMALL_BUFF, 'aligned_edge': LEFT})
        self.play(Write(codelines_mob[15]))
        self.play(Write(codelines_mob[16]))
        self.play(Write(codelines_mob[17]))
        self.play(rec.set_opacity, 1)
        self.play(Transform(captions_mob[0], captions_mob[5]))
        self.play(rec.set_stroke, {'color':PURPLE_C, 'width': 20, 'opacity': 1})
        self.wait(1.8)
        self.play(
            Transform(codelines_mob[15], codelines_mob[18]),
            Transform(codelines_mob[16], codelines_mob[19]),
        )
        self.play(Transform(captions_mob[0], captions_mob[6]))
        self.play(rec.set_stroke, {'color':GREEN_B, 'width': 10, 'opacity': 1})
        self.wait(1.8)
        self.play(
            Transform(codelines_mob[15], codelines_mob[27]),
            Transform(codelines_mob[17], codelines_mob[20]),
        )
        self.play(rec.set_stroke, {'color':PURPLE_C, 'width': 10, 'opacity': 0.5})
        self.wait(1.8)
        self.play(Transform(codelines_mob[17], codelines_mob[21]))
        self.play(rec.set_stroke, {'color':PURPLE_C, 'width': 10, 'opacity': 0})
        self.wait(1.8)
        self.play(codelines_mob[26].next_to, {'mobject_or_point':codelines_mob[25], 'direction':DOWN, 'buff': MED_SMALL_BUFF, 'aligned_edge': LEFT})
        self.play(Write(VGroup(codelines_mob[22], codelines_mob[23])))
        self.play(Transform(captions_mob[0], captions_mob[7]))
        self.play(rec.set_sheen_direction, UR)
        self.play(rec.set_sheen, 0.2)
        self.play(Transform(captions_mob[0], captions_mob[8]))
        self.wait(1.8)
        self.play(Transform(codelines_mob[22], codelines_mob[24]))
        self.play(rec.set_sheen, 0.4)
        self.play(Transform(captions_mob[0], captions_mob[9]))
        self.wait(1.8)
        self.play(Transform(codelines_mob[23], codelines_mob[25]))
        self.play(rec.set_sheen_direction, UL)
        self.wait(1.8)
        fade_out_codelines = VGroup(
            codelines_mob[0],
            code_bg,
            rec,
            up_label,
            right_label,
            captions_mob[0],
            codelines_mob[1],
            codelines_mob[2],
            codelines_mob[9],
            codelines_mob[10],
            codelines_mob[15],
            codelines_mob[16],
            codelines_mob[17],
            codelines_mob[22],
            codelines_mob[23],
            codelines_mob[26]
        )
        self.remove(brace_up, brace_right)
        self.play(FadeOut(fade_out_codelines))
        self.wait()

class SquareIllustration(RectangleIllustration):

    def construct(self):
        captions = [
            'Square的大小参数有side_length',
            '我们添加一个边长为4的正方形',
            '可以通过set_height或者set_width来调节它的大小',
            '由于它继承自Rectangle类，所以加上stretch=True，也可以把它拉回一个长方形',
        ]

        codelines = [
            'square = Square(side_length=4)',
            '# (default)side_length=2.0',
            'square.set_height(3)',
            'square.set_width(5)',
            'square.set_height(3,stretch=True)',
        ]

        captions_mob = VGroup(
            *[
                CodeLine(cap, size=0.32,plot_depth=5,color=DARKER_GRAY).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codelines_mob = VGroup(
            *[
                CodeLine(codeline,size=0.29)
                for codeline in codelines
            ]
        )

        code_bg = Rectangle(
            height=7,
            width=6,
            stroke_width=1,
            stroke_color=GRAY,
            fill_color=LIGHT_GREY,
            fill_opacity=0.25,
            plot_depth=-1
        ).to_edge(RIGHT, buff=LARGE_BUFF)

        self.play(FadeIn(code_bg))

        for each in range(len(codelines_mob)):
            if each == 0:
                codelines_mob[each].next_to(code_bg, direction=UP, aligned_edge=LEFT).shift(DOWN+RIGHT*0.5)
            elif each in range(1,10):
                codelines_mob[each].next_to(codelines_mob[each-1], direction=DOWN, aligned_edge=LEFT)

        sq = Square(
            side_length=4,
            stroke_width=1,
            stroke_color=PURPLE_C,
            fill_color=BLUE,
            fill_opacity=1,
            ).to_edge(LEFT, buff=LARGE_BUFF)
        brace_right = Brace(sq, direction=RIGHT,fill_color=LIGHT_GREY, fill_opacity=1)\
            .add_updater(lambda x: x.become(
                Brace(sq, direction=RIGHT,fill_color=LIGHT_GREY, fill_opacity=1)
            ))
        brace_up = Brace(sq, direction=UP,fill_color=LIGHT_GREY, fill_opacity=1)\
            .add_updater(lambda x: x.become(
                Brace(sq, direction=UP,fill_color=LIGHT_GREY, fill_opacity=1)
            ))
        right_label = CodeLine('4').next_to(brace_right, RIGHT, buff=SMALL_BUFF)
        self.play(FadeIn(captions_mob[0]))
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[1]))
        self.play(FadeIn(codelines_mob[0]))
        self.play(FadeIn(codelines_mob[1]))
        self.play(FadeIn(VGroup(sq, brace_right, right_label),run_time=1.2))
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.play(FadeIn(codelines_mob[2]))
        self.play(
            sq.set_height, 3,
            Transform(right_label, CodeLine('3').add_updater(lambda x: x.become(CodeLine('3').next_to(brace_right, RIGHT, buff=SMALL_BUFF))))
        )
        self.wait()
        self.play(FadeIn(codelines_mob[3]))
        self.play(
            sq.set_width, 5,
            Transform(right_label, CodeLine('5').add_updater(lambda x: x.become(CodeLine('5').next_to(brace_right, RIGHT, buff=SMALL_BUFF))))
        )
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.play(FadeIn(codelines_mob[4]))
        self.play(
            sq.set_height, {'height':3, 'stretch': True},
            Transform(right_label, CodeLine('3').add_updater(lambda x: x.become(CodeLine('3').next_to(brace_right, RIGHT, buff=SMALL_BUFF))))
        )
        self.wait()
        self.play(FadeOut(captions_mob[0]))
        self.wait()
        self.remove(brace_right)
        self.play(FadeOut(VGroup(codelines_mob[0], codelines_mob[1], codelines_mob[2], codelines_mob[3], code_bg, sq, codelines_mob[4], right_label)))


class RoundedRectangleIllustration(RectangleIllustration):

    def emphasize(self, mobject):
        self.play(mobject.scale, 1.2, run_time=0.5)
        self.play(mobject.scale, 10/12, run_time=0.5)

    def construct(self):
        captions = [
            'RoundedRectangle继承自Rectangle类',# 0
            '效果是使长方形的四个角变得圆滑',# 1
            '它的参数是corner_radius',# 2
            '可以通过调整这个参数来设置圆滑度',# 3
            'corner_radius的大小会决定边角的圆滑度',# 4
            '圆角的半径大小就是corner_radius的值',# 5
            '当corner_radius大于矩形最短边的二分之一时，矩形就会发生变形',# 6
            '而当corner_radius的值小于0时，圆边就会向内凹陷',# 7
            '由于RoundedRectangle继承自Rectangle类，你还可以直接调整Rectangle的corner_radius',# 8
            '或者在实例化Rectangle后通过round_corners方法设置其圆滑度',# 9
        ]

        codelines = [
            "roundedrec = RoundedRectangle(",# 0
            '~~~~#~(default)corner_radius=0.5',# 1
            '~~~~corner_radius=0.2',# 2
            '~~~~corner_radius=0.5',# 3
            '~~~~corner_radius=1.0',# 4
            '~~~~corner_radius=3.0',# 5
            '~~~~corner_radius=-1.0',# 6
            '~~~~corner_radius=-2.0',# 7
            '#~(Rectangle)corner_radius=0',# 8
            'rec~=~Rectangle(',# 9
            '~~~~height=3,',# 10
            '~~~~width=4,',# 11
            'rec.round_corners(1.5)',# 12
            ')',# 13
            ')',#14
        ]

        captions_mob = VGroup(
            *[
                CodeLine(cap,size=0.32,plot_depth=5,color=DARKER_GRAY).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )

        codelines_mob = VGroup(
            *[
                CodeLine(codeline,size=0.32)
                for codeline in codelines
            ]
        )

        code_bg = Rectangle(
            height=7,
            width=6,
            stroke_width=1,
            stroke_color=GRAY,
            fill_color=LIGHT_GREY,
            fill_opacity=0.25,
            plot_depth=-1
        ).to_edge(RIGHT, buff=LARGE_BUFF)

        self.play(FadeIn(code_bg))

        for each in range(len(codelines_mob)):
            if each == 0:
                codelines_mob[each].next_to(code_bg, direction=UP, aligned_edge=LEFT).shift(DOWN*0.8+RIGHT*0.2)
            elif each == 1:
                codelines_mob[each].next_to(codelines_mob[0], direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
            elif each in [2,3,4,5,6,7,13]:
                codelines_mob[each].next_to(codelines_mob[1], direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
            elif each == 8:
                codelines_mob[each].next_to(codelines_mob[7], direction=DOWN, aligned_edge=LEFT, buff=SMALL_BUFF).shift(DOWN*0.6)
            elif each in [9,10,11]:
                codelines_mob[each].next_to(codelines_mob[each-1], direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
            elif each == 14:
                codelines_mob[each].next_to(codelines_mob[11], direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
            elif each == 12:
                codelines_mob[each].next_to(codelines_mob[11], direction=DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF).shift(DOWN*0.6)

        roundedrectangle0 = RoundedRectangle(
            corner_radius=0.5,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        arrow_up = Arrow(start=np.array([1-3,1.5,0]), end=np.array([1-3,2,0]),color=YELLOW_A, opacity=1,buff=0,tip_length=0.25, max_tip_length_to_length_ratio=0.3)
        arrow_right = Arrow(start=np.array([1-3,1.5,0]), end=np.array([1.5-3,1.5,0]),color=YELLOW_A, opacity=1,buff=0,tip_length=0.25, max_tip_length_to_length_ratio=0.3)
        roundedrectangle1 = RoundedRectangle(
            corner_radius=0.2,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle2 = RoundedRectangle(
            corner_radius=0.5,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle3 = RoundedRectangle(
            corner_radius=1.0,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle4 = RoundedRectangle(
            corner_radius=3.0,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle5 = RoundedRectangle(
            corner_radius=-1.0,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle6 = RoundedRectangle(
            corner_radius=-2.0,
            fill_color="66CCFF",
            fill_opacity=1,
            height=4,
            width=3,)\
            .shift(LEFT*3)
        roundedrectangle7 = Rectangle(
            fill_color="66CCFF",
            fill_opacity=1,
            height=3,
            width=4,)\
            .shift(LEFT*3)
        self.play(Write(VGroup(codelines_mob[0], codelines_mob[1], codelines_mob[13])))
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[1]))
        self.wait()
        self.play(ShowCreation(roundedrectangle0))
        self.play(FadeIn(VGroup(arrow_up, arrow_right)))
        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.wait()
        self.play(codelines_mob[13].next_to, {'mobject_or_point':codelines_mob[2], 'direction': DOWN, 'aligned_edge': LEFT, 'buff': MED_SMALL_BUFF})
        self.play(Write(codelines_mob[2]))
        self.emphasize(codelines_mob[2])
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.wait()
        self.play(
            Transform(roundedrectangle0, roundedrectangle1),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([1.3-3,1.8,0]), 'end':np.array([1.5-3,1.8,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([1.3-3,1.8,0]), 'end':np.array([1.3-3,2,0])}),
        )
        self.wait()
        self.play(Transform(codelines_mob[2], codelines_mob[3]))
        self.emphasize(codelines_mob[2])
        self.play(
            Transform(roundedrectangle0, roundedrectangle2),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([1.0-3,1.5,0]), 'end':np.array([1.5-3,1.5,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([1.0-3,1.5,0]), 'end':np.array([1.0-3,2,0])}),
        )
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[5]))
        self.wait()
        self.play(Transform(codelines_mob[2], codelines_mob[4]))
        self.emphasize(codelines_mob[2])
        self.play(
            Transform(roundedrectangle0, roundedrectangle3),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([0.5-3,1.0,0]), 'end':np.array([1.5-3,1.0,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([0.5-3,1.0,0]), 'end':np.array([0.5-3,2,0])}),
        )
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[6]))
        self.play(Transform(codelines_mob[2], codelines_mob[5]))
        self.emphasize(codelines_mob[2])
        self.play(
            Transform(roundedrectangle0, roundedrectangle4),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([-1.5-3,-1.0,0]), 'end':np.array([1.5-3,-1.0,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([-1.5-3,-1.0,0]), 'end':np.array([-1.5-3,2,0])}),
        )
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[7]))
        self.play(Transform(codelines_mob[2], codelines_mob[6]))
        self.emphasize(codelines_mob[2])
        self.play(
            Transform(roundedrectangle0, roundedrectangle5),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([0.5-3,1.0,0]), 'end':np.array([1.5-3,1.0,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([0.5-3,1.0,0]), 'end':np.array([0.5-3,2,0])}),
        )
        self.wait()
        self.play(Transform(codelines_mob[2], codelines_mob[7]))
        self.emphasize(codelines_mob[2])
        self.play(
            Transform(roundedrectangle0, roundedrectangle6),
            ApplyMethod(arrow_right.put_start_and_end_on, {'start': np.array([-0.5-3,0.0,0]), 'end':np.array([1.5-3,0.0,0])}),
            ApplyMethod(arrow_up.put_start_and_end_on, {'start': np.array([-0.5-3,0.0,0]), 'end':np.array([-0.5-3,2,0])}),
        )
        self.wait()
        self.play(Transform(captions_mob[0], captions_mob[8]))
        self.wait()
        self.play(Write(codelines_mob[8]))
        self.wait()
        self.play(Write(codelines_mob[9]))
        self.play(Transform(captions_mob[0], captions_mob[9]))
        self.play(
            FadeOut(arrow_right),
            FadeOut(arrow_up),
            FadeIn(roundedrectangle7),
            FadeOut(roundedrectangle0)
        )
        self.wait()
        self.play(Write(codelines_mob[10]),run_time=0.6)
        self.play(Write(codelines_mob[11]),run_time=0.6)
        self.play(Write(codelines_mob[14]),run_time=0.6)
        self.play(Write(codelines_mob[12]))
        self.emphasize(codelines_mob[12])
        self.play(roundedrectangle7.round_corners, 1.5)
        self.wait(2)


class Test(RoundedRectangleIllustration):
    def construct(self):
        r = RoundedRectangle(height=6, width=6, corner_radius=1.5,opacity=1).set_color(BLUE)
        rr = SurroundingRectangle(r).set_color(GRAY)
        rr.set_opacity(1)
        self.play(FadeIn(r))
        # arrow_right = Arrow(color=GREEN, opacity=1,length=1.5, buff=0)
        # arrow_right.set_length(1.5)
        # arrow_right.next_to(r,RIGHT,aligned_edge=UP, buff=0).shift(LEFT*1.5+DOWN*1.3)
        arrow_right = Line(start=np.array([1.5,1.5,0]),end=np.array([1.5,3,0])).set_color(PURPLE_C)
        arrow_up = Line(start=np.array([1.5,1.5,0]),end=np.array([3,1.5,0])).set_color(PURPLE_C)
        arrow_right.add_tip()
        arrow_up.add_tip()
        self.play(FadeIn(arrow_right))
        self.play(FadeIn(arrow_up))
        self.play(ShowCreationThenDestructionAround(rr))


class DecimalNumberText(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "text_config": {
            "font": "Consolas",
            "size": 0.4,
            "color": GOLD,
        }
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            Text(char, **kwargs, **self.text_config)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(Text("...", **self.text_config))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = Text(self.unit, color=self.color, **self.text_config)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        """
        Configuration is based first off instance attributes,
        but overwritten by any kew word argument.  Relevant
        key words:
        - include_sign
        - group_with_commas
        - num_decimal_places
        - field_name (e.g. 0 or 0.real)
        """
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumberText(number, **full_config)
        # Make sure last digit has constant height
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)


class TestDecimalNumberText(Scene):
    def construct(self):
        decimal = DecimalNumberText(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()




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