from manimlib.imports import *

class Chapter1_Animation(MovingCameraScene):

    def construct(self):
        self.text_1 = Text('摄像机位置缩放效果展示', font=' DFLianLian SC2 W2', color='RED').to_edge(TOP, buff=0.1)
        self.text_2 = Text('让我们来回顾一个经典的问题', font='丁永康硬笔楷书新版', color='YELLOW').scale(0.3)
        self.achilles_svg = SVGMobject('./srcs/figs/Achilles.svg', color='BLUE', stroke_width=0.2).scale(
            1.25).to_corner(
            DOWN * 1.8 + LEFT * 6)
        self.tortoise_svg = SVGMobject('./srcs/figs/tortoise.svg', color='YELLOW').scale(0.64).to_corner(
            DOWN * 1.8 + RIGHT * 6)
        self.circle_1 = Circle(radius=0.5)
        self.obj = VGroup(self.circle_1, self.text_2).arrange_submobjects(DOWN, buff=0.5)
    
    def Chapter1_Animation(self):
        # 动画展示
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

        self.wait()

class Chapter2_Animation(Chapter1_Animation):

    def construct(self):
        super(Chapter2_Animation, self).construct()

        self.Chapter2_text_1 = Text('文字变换展示', font=' DFLianLian SC2 W2', color='GREEN').scale(2)
        
    def Chapter2_Animation(self):
        # 动画展示
        self.clear()
        self.play(WiggleOutThenIn(self.Chapter2_text_1), run_time=1.8)
        self.wait(0.6)

class change_camera_size(Chapter2_Animation):

    def construct(self):
        super(change_camera_size, self).construct()
        self.Chapter1_Animation()
        self.Chapter2_Animation()
