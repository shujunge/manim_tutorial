from manimlib.imports import *

class change_camera_size(MovingCameraScene):

    def construct(self):

        ## 物体构建
        text_1 = Text('摄像机位置缩放效果展示', font=' DFLianLian SC2 W2', color=BLUE).to_edge(TOP, buff=0.1)
        text_2 = Text('让我们来回顾一个经典的问题', font='丁永康硬笔楷书新版', color=YELLOW).scale(0.3)
        zz = Circle(radius=0.5)
        obj = VGroup(zz, text_2).arrange_submobjects(DOWN, buff=0.5)

        achilles_svg = SVGMobject('./srcs/figs/Achilles.svg', color=BLUE, stroke_width=0.2).scale(1.25).to_corner(
            DOWN * 1.8 + LEFT * 6)
        tortoise_svg = SVGMobject('./srcs/figs/tortoise.svg', color=YELLOW).scale(0.64).to_corner(
            DOWN * 1.8 + RIGHT * 6)

        # 动画展示
        self.play(Write(text_1), run_time=1.8)
        self.wait(0.6)
        self.play(LaggedStartMap(FadeInFromDown, obj), run_time=2)
        self.wait(0.4)
        self.play(FadeInFromLarge(achilles_svg))
        self.play(FadeInFromLarge(tortoise_svg))
        self.play(TurnInsideOut(achilles_svg), WiggleOutThenIn(tortoise_svg))
        self.wait(2)
        self.camera.frame.save_state()
        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_width, text_2.get_width()*1.2,
            # Move the camera to the object
            self.camera.frame.move_to, text_2
        )
        self.wait()
        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_height, zz.get_height() * 1.5,

            # Move the camera to the object
            self.camera.frame.move_to, zz
        )
        self.wait()
        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_height, achilles_svg.get_height() * 1.2,
            # Move the camera to the object
            self.camera.frame.move_to, achilles_svg
        )
        self.wait()

        # Restore the state saved
        self.play(Restore(self.camera.frame))

        self.play(
            # Set the size with the width of a object
            self.camera.frame.set_width, tortoise_svg.get_width() * 1.2,
            # Move the camera to the object
            self.camera.frame.move_to, tortoise_svg
        )
        self.wait()
        self.play(Restore(self.camera.frame))



        self.wait()