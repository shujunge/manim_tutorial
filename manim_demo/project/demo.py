import warnings
warnings.filterwarnings('ignore')
from manimlib.imports import *
from srcs.utils import run


class VideoProgressBar(Scene):
    CONFIG = {
        "camera_config": {
            "background_image": r"background.png",
            # 视频的高宽与帧率
            "pixel_height": DEFAULT_PIXEL_HEIGHT,
            "pixel_width": DEFAULT_PIXEL_WIDTH,
            "frame_rate": DEFAULT_FRAME_RATE,
            # Note: frame height and width will be resized to match
            # the pixel aspect ratio
            # FRAME_HEIGHT = 8.0
            # FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / 						DEFAULT_PIXEL_HEIGHT
            "frame_height": FRAME_HEIGHT,
            "frame_width": FRAME_WIDTH,
        },
        'methods_dict': {
            '序言': '0025',
            '介绍': '0210',
            '第一节': '0402',
            '第二节': '0504',
            'flip': '0712',
            'stretch': '0901',
            'to_corner': '1014',
            'align_to': '1129',
            'next_to': '1227',
            'set_width+set_height': '1500',
            ' ': '1659'},
        'total_time': '1724',
        'color_list': [BLUE, PINK, RED, ORANGE, GREEN],
        'bar_width': 20,
        'text_size': 0.15,
    }

    def construct(self):

        func_time = lambda t: int(t[0:2]) * 60 + int(t[2:])
        func_loc = lambda t: func_time(t) / func_time(self.total_time) * FRAME_WIDTH * RIGHT + FRAME_WIDTH * LEFT / 2

        self.colors = color_gradient(self.color_list, len(self.methods_dict) + 1)
        p_list = [FRAME_WIDTH * LEFT / 2]
        for v in self.methods_dict.values():
            p_list.append(func_loc(v))
        p_list.append(func_loc(self.total_time))

        self.lines = VGroup(
            *[Line(p_list[i], p_list[i + 1] - 0.02 * RIGHT, color=self.colors[i], stroke_width=self.bar_width) for i in
              range(len(self.methods_dict) + 1)])
        self.lines.to_edge(DOWN * 0.22, buff=1)
        self.texts = VGroup(
            *[Text(t, color=BLACK, size=self.text_size, weight=BOLD) for t in self.methods_dict.keys()],
            plot_depth=1)
        for i in range(len(self.methods_dict)):
            self.texts[i].move_to(self.lines[i + 1])

    def demo_begin(self):

        self.play(LaggedStartMap(FadeInFromDown,self.lines), LaggedStartMap(ShowCreation,self.texts))

        self.wait()


class Introduction(TeacherStudentsScene):

    CONFIG = {
        "student_colors": [BLUE_D, BLUE_E, BLUE_C, GOLD_A,
                           TEAL_E, GREEN_E, YELLOW_E, GOLD_E,
                           RED_E, MAROON_E, PURPLE_E,LIGHT_GRAY,
                           TEAL_E, GREEN_E, YELLOW_E, GOLD_E],
        "teacher_color": GREY_BROWN,
        "student_scale_factor": 0.4,
        "teacher_scale_factor": 0.8,
        "seconds_to_blink": 2,
        "screen_height": 10,
    }

    def create_pi_creatures(self):

        self.teacher = Mortimer(color=self.teacher_color)
        self.teacher.scale(self.teacher_scale_factor).to_edge(RIGHT)
        self.teacher.look(DOWN + LEFT)
        self.students = VGroup(*[Randolph(color=c) for c in self.student_colors])
        self.students.arrange_in_grid(n_rows=4, n_cols=4, buff= MED_LARGE_BUFF)
        self.students.scale(self.student_scale_factor)
        self.students.shift(3* LEFT)
        self.teacher.look_at(self.students[len(self.teacher_color)].eyes)
        for student in self.students:
            student.look_at(self.teacher.eyes)
        return [self.teacher] + list(self.students)

    def construct(self):

        self.tencher_says_1 = Text("学习平面几何可以使得人变聪明. --爱因斯坦", color=BLUE)
        self.students1 = Text("哇! 这回可以好好学习平面几何了!").set_color(BLUE)
        self.students2 = Text("老师,爱因斯坦好像没说过这话吧!").set_color(BLUE)
        self.students3_1 = Text("这不重要吧....").set_color(BLUE)
        self.students3_2 = Text("老师快开始吧,我已经破不急待\n想学习新知识了").set_color(BLUE)
        self.tencher_says_2 = Text("好的,我们开始今天的课程.").set_color(BLUE)

    def Introduction_Animation(self):

        # teacher
        self.play(PiCreatureSays(self.teacher, Text("同学们,大家报数!", color=BLUE), self.teacher.change, "speaking", bubble_kwargs={"width": 6, "height": 2, "direction": RIGHT}))
        self.play(self.teacher.change, "happy") # FadeOut(self.teacher.bubble)
        self.wait()
        self.play(RemovePiCreatureBubble(self.teacher))
        self.wait()

        for index in [1,15,7,4,9,12,6]:
            # student
            self.text = Text("%d" % (index), color= self.student_colors[index-1])
            self.play(PiCreatureSays(self.students[index - 1], self.text, bubble_kwargs={"width": 3, "height": 1.2, "direction": LEFT}),run_times=0.2)
            # self.change_all_student_modes("pondering", look_at_arg=self.students[1], added_anims=[self.students[1].look_at, self.students2])
            self.play(RemovePiCreatureBubble(self.students[index - 1]), run_times=0.025)

        self.play(PiCreatureSays(self.teacher, self.tencher_says_2, bubble_kwargs={"width": 6, "height": 2, "direction": RIGHT}))
        self.wait()
        self.play(RemovePiCreatureBubble(self.teacher), run_times=0.025)
        self.wait()

        self.clear_Introduction_Animation_all()
        self.wait()


    def Introduction2_Animation(self):

        # teacher
        self.play(PiCreatureSays(self.teacher, self.tencher_says_1, self.teacher.change, "speaking", bubble_kwargs={"width": 6, "height": 2, "direction": RIGHT}))
        self.play(self.teacher.change, "happy") # FadeOut(self.teacher.bubble)
        self.wait()
        #
        # student1
        self.play(RemovePiCreatureBubble(self.teacher))
        self.wait()
        self.play(PiCreatureSays(self.students[0], self.students1, bubble_kwargs={"width": 7, "height": 2, "direction": LEFT}))
        # self.change_all_student_modes("pondering", look_at_arg=self.students[0], added_anims=[self.students[0].look_at, self.students1])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[0]))
        self.wait()

        # student2
        self.play(PiCreatureSays(self.students[1], self.students2, bubble_kwargs={"width": 5, "height": 2, "direction": RIGHT}))
        # self.change_all_student_modes("pondering", look_at_arg=self.students[1], added_anims=[self.students[1].look_at, self.students2])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[1]))
        self.wait()

        # student3
        self.play(PiCreatureSays(self.students[2], self.students3_1, bubble_kwargs={"width": 5, "height": 2, "direction": RIGHT}))
        # self.change_all_student_modes("happy", look_at_arg=self.students[2], added_anims=[self.students[2].look_at, self.students[1]])
        self.wait(2)
        self.play(RemovePiCreatureBubble(self.students[2]))
        self.wait()
        self.play(PiCreatureSays(self.students[2], self.students3_2, bubble_kwargs={"width": 5, "height": 2, "direction": LEFT}))
        # self.change_all_student_modes("happy", look_at_arg=self.students[2], added_anims=[self.students[2].look_at, self.students3_2])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[2])) #RemovePiCreatureBubble(self.students[2])
        self.wait()

        # teacher
        self.play(PiCreatureSays(self.teacher, self.tencher_says_2, bubble_kwargs={"width": 6, "height": 2, "direction": RIGHT}))
        # self.change_all_student_modes("happy")
        self.wait()

    def clear_Introduction_Animation_all(self):
        clear_list = VGroup()
        for it in [ self.students, self.teacher]:
            clear_list.add(it)
        self.play(LaggedStartMap(Uncreate, clear_list, run_times=3))


class Chapter1(MovingCameraScene):

    def construct(self):
        self.text_1 = Text('摄像机位置缩放效果展示', font=' DFLianLian SC2 W2', color='RED').to_edge(TOP, buff=0.1)
        self.text_2 = Text('让我们来回顾一个经典的问题', font='丁永康硬笔楷书新版', color='YELLOW').scale(0.3)
        self.achilles_svg = SVGMobject('../srcs/figs/Achilles.svg', color='BLUE', stroke_width=0.2).scale(
            1.25).to_corner(
            DOWN * 1.8 + LEFT * 6)
        self.tortoise_svg = SVGMobject('../srcs/figs/tortoise.svg', color='YELLOW').scale(0.64).to_corner(
            DOWN * 1.8 + RIGHT * 6)
        self.circle_1 = Circle(radius=0.5)
        self.obj = VGroup(self.circle_1, self.text_2).arrange_submobjects(DOWN, buff=0.5)

    def Chapter1_Animation(self):
        # 动画展示
        self.wait(1)
        self.play(Write(self.text_1), run_time=1.8)
        self.wait(0.6)
        self.play(LaggedStartMap(FadeInFromDown, self.obj), run_time=2)
        self.wait(0.4)
        self.play(FadeInFromLarge(self.achilles_svg))
        self.play(FadeInFromLarge(self.tortoise_svg))
        self.play(TurnInsideOut(self.achilles_svg), WiggleOutThenIn(self.tortoise_svg))
        self.wait(2)
        self.camera.frame.save_state()
        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_width, self.text_2.get_width() * 1.2,
            # Move the camera to the object
            self.camera.frame.move_to, self.text_2
        )
        self.wait()
        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_height, self.circle_1.get_height() * 1.5,

            # Move the camera to the object
            self.camera.frame.move_to, self.circle_1
        )
        self.wait()
        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_height, self.achilles_svg.get_height() * 1.2,
            # Move the camera to the object
            self.camera.frame.move_to, self.achilles_svg
        )
        self.wait()

        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_width, self.tortoise_svg.get_width() * 1.2,
            # Move the camera to the object
            self.camera.frame.move_to, self.tortoise_svg
        )
        self.wait()
        self.play(Restore(self.camera.frame))

        self.clear_chapter1_all()
        self.wait()

    def clear_chapter1_all(self):
        clear_list = VGroup()
        for it in [self.text_1, self.text_2, self.circle_1, self.achilles_svg, self.tortoise_svg]:
            clear_list.add(it)
        self.play(LaggedStartMap(Uncreate, clear_list, run_times=3))


class Chapter2(PhysicScene):

    def construct(self):
        grd_body = self.space.static_body
        self.grd_seg = pymunk.Segment(grd_body, (-10000, -2000), (10000, -2000), 0)
        self.grd_seg.friction = 0.7
        self.grd_shape = Line(
            LEFT * 10,
            RIGHT * 10
        ).shift(2 * DOWN).set_color(BLACK)

        self.ground = PhysicMobject(grd_body, self.grd_seg, self.grd_shape)


    def Chapter2_Animation(self):

        self.set_gravity(9.8 * DOWN)
        self.add_static_obj(self.ground)
        for i in range(60):

            mass = 10
            size = (500, 500)
            moment = pymunk.moment_for_box(mass, size)
            body = pymunk.Body(mass, moment)
            body.angle = i * 0.1
            body.position = (i * 300 - 5000), 4000
            box = pymunk.Poly.create_box(body, size)
            box.friction = 0.5

            shape = Circle(radius=0.5)
            # shape.stretch_to_fit_height(0.5)
            # shape.stretch_to_fit_width(0.5)
            shape.set_fill(DARK_BLUE, opacity=1)
            mobj = PhysicMobject(body, box, shape)
            mobj.set_add_time(i * 0.5)

            self.add_physic_obj(mobj)

        self.simulate(20)
        self.clear_chapter2_all()
        self.wait()

    def clear_chapter2_all(self):
        clear_list = VGroup()
        for it in [ self.ground,self.grd_shape, *self.physic_objs]:
            clear_list.add(it)
        self.play(LaggedStartMap(Uncreate, clear_list, run_times=3))


Total_class = [ Chapter2, VideoProgressBar, Introduction, Chapter1,]

class LogoDemo(*Total_class):
    def construct(self):
        super(LogoDemo, self).construct()
        for class_instance in Total_class:
            super(class_instance, self).construct()

        self.demo_begin()
        self.Introduction_Animation()
        self.Chapter1_Animation()
        self.Chapter2_Animation()

if __name__ == "__main__":

    run([LogoDemo], l=True, h=False)