from manimlib.imports import *
from srcs.utils import run
from srcs.fourier_series import ManyFourierCirclesScene

class ZoomDemo(ManyFourierCirclesScene,ZoomedScene):
    CONFIG = {
        # ManyFourierOfTexSymbol
        "n_vectors": 51,
        "center_point": [ 4.5*LEFT+0.5*UP, 4.5 *LEFT + 0.5*DOWN],
        "slow_factor": 0.1,
        "n_cycles": 2,
        "tex": [index for index in "重庆"],
        "start_drawn": False,
        "max_circle_stroke_width": 1,
        # ZoomedScene
        "zoom_factor": 0.15,
        "zoomed_display_height": 2.5,
        "zoomed_display_width": 1,
        "zoomed_display_center": 2 * RIGHT,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
            "background_opacity": 1,
            "buff":MED_SMALL_BUFF,
        },
    }
    def setup(self):
        ManyFourierCirclesScene.setup(self)
        ZoomedScene.setup(self)


    def construct(self):
        super(ZoomDemo, self).construct()
        super(ManyFourierCirclesScene, self).construct()

        self.add_vectors_circles_path()
        self.wait(self.n_cycles/self.slow_factor)

    def get_zoomed_display_pop_out_animation(self, **kwargs):
        display = self.zoomed_display
        display.save_state(use_deepcopy=True)
        display.replace(self.zoomed_camera.frame, stretch=True)
        return ApplyMethod(display.restore)



    def add_vectors_circles_path(self):

        begin_text = Text("千里为重,广大为庆")
        self.play(FadeInFromDown(begin_text))

        object_list = VGroup()
        scale = [1 for _ in range(len(self.tex))]
        for index, center_point in enumerate(range(len(self.tex))):
            tex_mob = Text(self.tex[index]).scale(scale[index]).shift(self.center_point[index])
            path = tex_mob.family_members_with_points()[0]
            path.set_fill(opacity=0.01)
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
            fill_opacity= 1,
            buff = MED_SMALL_BUFF,
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

        # self.play(LaggedStartMap(ShowCreation, object_list))
        self.play(ReplacementTransform(begin_text, object_list))

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
            zoomed_display.scale, 3.2, #放大3.2倍
            zoomed_display.set_height, FRAME_HEIGHT,
            # zoomed_display.set_width, FRAME_WIDTH/2 -4
        )
        self.wait()

        self.add(*vectors_list)
        self.add(*circles_list)
        self.add(*drawn_path)


    def set_decreasing_stroke_widths(self, circles):
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=1)
        return circles


if __name__ == '__main__':
    run(your_module = [ZoomDemo], l=True, h=False, gif =False)
