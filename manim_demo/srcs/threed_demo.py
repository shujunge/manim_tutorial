from manimlib.imports import *

class update_text_timeing(GraphScene):

    CONFIG = {
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": MAROON_A,
        "x_min": -3,
        "x_max": 3, "y_min": -10,
        "y_max": 10,
        "x_axis_width": 14,
        "y_axis_height": 8,

    }
    def construct(self):
        my_dot = Dot()
        txt= Text("A", font='STKaiti').set_color(RED)
        txt.next_to(my_dot,LEFT)
        zz = VGroup(txt, my_dot)
        self.add( zz)
        self.play(Rotating(zz, axis= OUT, radians=2*PI, about_point= 2*RIGHT, run_times = 3))
        self.wait()

        def update_txt(mobj):
            mobj.next_to(my_dot, LEFT, buff = SMALL_BUFF)

        txt.add_updater(update_txt)  # 把这个函数添加给text
        self.play(Rotating(my_dot, axis= OUT, radians=2*PI,
                           about_point= 2*RIGHT, run_times =3))

        # self.play(Rotating(my_dot, axis= OUT, radians=2*PI,
        #                    about_point= 2*RIGHT, run_times =3), UpdateFromFunc(txt, update_txt))
        self.wait()
        self.clear()
        def x2(x):
            return x ** 4+ x**2

        my_plane = NumberPlane(background_line_style={"stroke_color": GREEN, "stroke_opacity": 0.4})
        C = Circle(color=BLUE, radius=3)

        self.add(my_plane)
        self.setup_axes()
        A = self.get_graph(x2, color=YELLOW, x_min=-3, x_max=3)
        S1 = Dot(color=RED).scale(3)
        self.add(A)
        self.play(FadeInFromLarge(C), run_time=4)
        self.play(MoveAlongPath(S1, A), run_time=5, rate_fun=there_and_back_with_pause)
        self.wait()

class basic_3d_shape(ThreeDScene):

    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.wait()

        bb= Sphere(r=1, color=BLUE)#,checkerboard_colors=[RED,TIFF])
        bb.shift(1*IN)
        cc= Cube(side_length= 1, fill_color= RED)
        cc.next_to(bb,OUT)
        pp = Prism(dimensions=[1, 1, 1])
        pp.next_to(cc,OUT)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60*DEGREES,distance=8, gamma=None)
        self.wait()
        self.play(ShowCreation(bb), FadeIn(cc), Write(pp), run_times= 3)
        self.wait()
        self.play(Uncreate(bb), Uncreate(cc), Uncreate(pp),run_times=2)

        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 + 1.2 * np.cos(u),
                1.2 * np.sin(u),
                2.4 * np.sqrt(0.5 - 0.5 * np.cos(u))
            ]), color=RED, t_min=0, t_max=2 * np.pi)
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Uncreate(curve1))

        sphere = ParametricSurface(
            lambda u, v: np.array([u, v, (u ** 2 - v ** 2) / 2
                                   ]), v_min=-2, v_max=2, u_min=-2, u_max=2, checkerboard_colors=[RED_D, RED_E],
            resolution=(30, 30)).scale(2)
        self.play(ShowCreation(sphere))
        self.wait()

        self.begin_ambient_camera_rotation(rate=0.02)
        self.move_camera(theta= 60 * DEGREES, run_time=3)
        self.move_camera(phi=0 * DEGREES, run_time=3)
        self.move_camera(distance=5, run_time=3)
        self.wait()
