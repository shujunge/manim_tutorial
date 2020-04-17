from manimlib.imports import *

class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations": 5,
        "angle": 90*DEGREES,
        "border_proportion": 1.25,
        "colors":[RED_A,RED_C,RED_E,BLUE_A,
                  BLUE_C,BLUE_E,YELLOW_A,YELLOW_C]
    }
    def construct(self):
        self.color = it.cycle(self.colors)
        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, color = next(self.color))
        path.add(first_line)

        self.camera_frame.set_height(first_line.get_height() * self.border_proportion)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))
        self.add_foreground_mobject(path)

        self.target_path = self.get_all_paths(path, self.iterations)
        for i in range(self.iterations):
            self.duplicate_path(path, i)
        self.wait()

    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * self.border_proportion
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians=self.angle,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        self.add_foreground_mobject(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        self.angle, 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1

class my_roate( MovingCameraScene):
    def construct(self):
        text1 = TextMobject("hello 成都!")
        text2 = TexMobject("x_{\mbox{物}}")
        my_models = VGroup()

        zz = VGroup(text1, text2).arrange(RIGHT)
        my_models.add(zz)
        self.camera_frame.set_width(zz.get_width() * 1.25)
        self.camera_frame.move_to(zz)
        self.play(ShowCreation(zz))
        self.add_foreground_mobject(zz)
        self.wait()
        new_path = zz.copy()
        new_path.set_color(RED)
        temp = new_path.copy()
        temp.rotate(90*DEGREES, about_point=text1.get_left())
        my_models.add(temp)
        width = my_models.get_width() * 2
        height = my_models.get_height() * 2

        self.play(Rotating(new_path, radians= 90*DEGREES, about_point=text1.get_left(),
                rate_func=linear),
            self.camera_frame.move_to, my_models,
            self.camera_frame.set_height, height,
            self.camera_frame.set_width, width,
            run_time = 1, rate_func = smooth,
                  )
        self.wait()