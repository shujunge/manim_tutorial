from manimlib.imports import *


class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "zoomed_display_center": ORIGIN,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL * 2)

        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.set_height(7)
        frame_text = TextMobject("Frame", color=PURPLE).scale(1.4)
        zoomed_camera_text = TextMobject("Zommed camera", color=RED).scale(1.4)

        self.add(image, dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame, DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        ## 展示缩放区间
        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor = [0.5, 1.5, 0]

        # Resize the frame and zoomed camera
        self.play(
            frame.scale, scale_factor,
            zoomed_display.scale, scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale, 3,
            frame.shift, UP
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display, 2)
        )

        self.wait()

        ## 收回缩放区间
        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1 - t), )

        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()


from srcs.fourier_series import ManyFourierCirclesScene

class ZoomDemo(ManyFourierCirclesScene,ZoomedScene):
    CONFIG = {
        # ManyFourierOfTexSymbol
        "n_vectors": 51,
        "center_point": [ 4.5*LEFT+0.5*UP, 4.5 *LEFT + 0.5*DOWN],
        "slow_factor": 0.1,
        "n_cycles": 1,
        "tex": [index for index in "重庆"],
        "start_drawn": False,
        "max_circle_stroke_width": 1,
        # ZoomedScene
        "zoom_factor": 0.3,
        "zoomed_display_height": 2.5,
        "zoomed_display_width": 1,
        "zoomed_display_center": 2 * RIGHT,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }
    def setup(self):
        ManyFourierCirclesScene.setup(self)
        ZoomedScene.setup(self)


    def construct(self):
        super(ZoomDemo, self).construct()
        super(ManyFourierCirclesScene, self).construct()

        self.add_vectors_circles_path()
        self.wait(1/self.slow_factor)

    def add_vectors_circles_path(self):

        object_list = VGroup()
        scale = [1 for _ in range(len(self.tex))]
        for index, center_point in enumerate(range(len(self.tex))):
            tex_mob = Text(self.tex[index]).scale(scale[index]).shift(self.center_point[index])
            path = tex_mob.family_members_with_points()[0]
            path.set_fill(opacity=0)
            path.set_stroke(WHITE, 1)
            object_list.add(path)


        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.move_to(object_list.get_center())
        frame.set_color(PURPLE)
        frame.set_width(object_list.get_width() * 1.2)
        # frame.set_height(object_list[-1].get_height() * 1.2) # set up the height of zoom camera
        zoomed_display_frame.set_color(BLUE)
        # zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=1,
            buff=MED_SMALL_BUFF,
        )
        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: ReplacementTransform(rect, zoomed_display) #rect.replace(zoomed_display)
        )


        coefs_list  = []
        for index, path in enumerate(object_list):
            coefs_list.append(self.get_coefficients_of_path(center_point=self.center_point[index], path=path))
        vectors_list = VGroup()
        for index, coefs in enumerate(coefs_list):
            vectors_list.add(self.get_rotating_vectors(center_point=self.center_point[index], coefficients=coefs))

        circles_list = VGroup()
        drawn_path = VGroup()
        for vectors in vectors_list:
            circles = self.get_circles(vectors)
            self.set_decreasing_stroke_widths(circles)
            # approx_path = self.get_vector_sum_path(circles)
            drawn_path.add(self.get_drawn_path(vectors))
            if self.start_drawn:
                self.vector_clock.increment_value(1)
            circles_list.add(circles)

        self.play(LaggedStartMap(ShowCreation, object_list))
        self.wait()

        self.play(ShowCreation(frame))
        # Activate zooming
        self.activate_zooming()
        ## 展示缩放区间
        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )
        # Resize the frame and zoomed camera
        self.play(
            frame.scale, 1,
            zoomed_display.scale, 4,
            zoomed_display.set_height, FRAME_HEIGHT * 0.8
        )
        self.wait()

        self.add(*vectors_list)
        self.add(*circles_list)
        self.add(*drawn_path)

    def set_decreasing_stroke_widths(self, circles):
        mcsw = self.max_circle_stroke_width
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                # mcsw / np.sqrt(k),
                mcsw / k,
                mcsw,
            ))
        return circles
