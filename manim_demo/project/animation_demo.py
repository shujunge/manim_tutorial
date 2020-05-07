from manimlib.imports import *
from srcs.utils import run

class WiggleOutThenIn(Animation):
    CONFIG = {
        "scale_value": 1.1,
        "rotation_angle":  TAU/4,
        "n_wiggles": 2,
        "run_time": 2,
        "scale_about_point": None,
        "rotate_about_point": None,
    }

    def get_scale_about_point(self):
        if self.scale_about_point is None:
            return self.mobject.get_center()

    def get_rotate_about_point(self):
        if self.rotate_about_point is None:
            return self.mobject.get_center()

    def interpolate_submobject(self, submobject, starting_sumobject, alpha):
        submobject.points[:, :] = starting_sumobject.points
        submobject.rotate_in_place( wiggle(alpha, self.n_wiggles) * self.rotation_angle)

        # submobject.scale(
        #     interpolate(1, self.scale_value, there_and_back(alpha)),
        #     about_point=self.get_scale_about_point()
        # )
        # submobject.rotate(
        #     wiggle(alpha, self.n_wiggles) * self.rotation_angle,
        #     about_point=self.get_rotate_about_point()
        # )


class Transform(Animation):
    CONFIG = {
        "path_arc": -np.pi,
        "path_arc_axis": OUT,
        "path_func": None,
        "replace_mobject_with_target_in_scene": True,
    }

    def __init__(self, mobject, target_mobject=None, **kwargs):
        super().__init__(mobject, **kwargs)
        self.target_mobject = target_mobject
        self.init_path_func()

    def init_path_func(self):
        if self.path_func is not None:
            return
        elif self.path_arc == 0:
            self.path_func = straight_path
        else:
            self.path_func = path_along_arc(
                self.path_arc,
                self.path_arc_axis,
            )

    def begin(self):
        # Use a copy of target_mobject for the align_data
        # call so that the actual target_mobject stays
        # preserved.
        self.target_mobject = self.create_target()
        self.check_target_mobject_validity()
        self.target_copy = self.target_mobject.copy()
        # Note, this potentially changes the structure
        # of both mobject and target_mobject
        self.mobject.align_data(self.target_copy)
        super().begin()

    def create_target(self):
        # Has no meaningful effect here, but may be useful
        # in subclasses
        return self.target_mobject

    def check_target_mobject_validity(self):
        if self.target_mobject is None:
            message = "{}.create_target not properly implemented"
            raise Exception(
                message.format(self.__class__.__name__)
            )

    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        if self.replace_mobject_with_target_in_scene:
            scene.remove(self.mobject)
            scene.add(self.target_mobject)

    def update_config(self, **kwargs):
        Animation.update_config(self, **kwargs)
        if "path_arc" in kwargs:
            self.path_func = path_along_arc(
                kwargs["path_arc"],
                kwargs.get("path_arc_axis", OUT)
            )

    def get_all_mobjects(self):
        return [
            self.mobject,
            self.starting_mobject,
            self.target_mobject,
            self.target_copy,
        ]

    def get_all_families_zipped(self):
        return zip(*[
            mob.family_members_with_points()
            for mob in [
                self.mobject,
                self.starting_mobject,
                self.target_copy,
            ]
        ])

    def interpolate_submobject(self, submob, start, target_copy, alpha):
        submob.interpolate(
            start, target_copy,
            alpha, self.path_func
        )
        return self

class Ball(Circle):
    CONFIG = {
        "radius": 0.4,
        "fill_color": BLUE,
        "fill_opacity": 1,
        "color": BLUE
    }

    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.velocity = np.array((2, 0, 0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius


class demo(Scene):
    def construct(self):
        self.text = Text("hdd",font='dsfont')
        self.ball = Ball().shift(UR)
        self.play(Write(self.text))
        self.wait()
        self.play(WiggleOutThenIn(self.text))
        self.wait()
        self.play(Transform(self.text, self.ball,run_times=4))
        self.wait()






class test(Scene):
    def construct(self):
        phi = ValueTracker(0)
        line = Line(ORIGIN,(2,0,0))
        sample_text = TextMobject("Text")
        sample_text.shift(LEFT*2)
        line.add_updater(lambda d: d.set_angle(phi.get_value()))
        self.add(line)
        self.play(
            GrowFromCenter(sample_text,rate_func = linear),
            phi.increment_value,PI
        )


class ClockOrganization(VGroup):
  CONFIG = {
    "numbers" : 4,
    "radius" : 3.1,
    "color" : WHITE
  }

  def __init__(self, **kwargs):
    digest_config(self, kwargs, locals())
    self.generate_nodes()
    VGroup.__init__(self, *self.node_list,**kwargs)

  def generate_nodes(self):
    self.node_list = []
    for i in range(self.numbers):
      mobject = VMobject()
      number = TexMobject(str(i+1))
      circle = Circle(radius=0.4,color=self.color)
      mobject.add(number)
      mobject.add(circle)
      mobject.move_to(
        self.radius * np.cos((-TAU / self.numbers) * i + 17*TAU / 84) * RIGHT
        + self.radius * np.sin((-TAU / self.numbers) * i + 17*TAU / 84) * UP
      )
      self.node_list.append(mobject)

  def select_node(self, node):
    selected_node = self.node_list[node]
    selected_node.scale(1.2)
    selected_node.set_color(RED)

  def deselect_node(self, selected_node):
    node = self.node_list[selected_node]
    node.scale(0.8)
    node.set_color(self.color)

class Testing4(Scene):
  def construct(self):
    test = ClockOrganization(numbers=21)
    self.play(Write(test), run_time=1.5)
    animation_steps=[]
    #animation_steps.append(test)
    num_circ=15
    for i in range(num_circ):
      thing = test.deepcopy()
      thing.select_node((19+i)%test.numbers-1)
      animation_steps.append(thing)
    test_normal=test.copy()
    test.save_state()
    self.play(Transform(test, animation_steps[0]))
    self.wait(2)
    self.play(Restore(test))
    anims=[]
    for i in range(1,num_circ):
        test.node_list[(19+i)%test.numbers-1].generate_target()
        test.node_list[(19+i)%test.numbers-1].target.scale(1.2)
        test.node_list[(19+i)%test.numbers-1].target.set_color(RED)
        anims.append(MoveToTarget(test.node_list[(19+i)%test.numbers-1],rate_func=there_and_back))
    self.play(
        AnimationGroup(*anims,lag_ratio=0.1)
        )
    self.wait()


if __name__=="__main__":
    run([DownProgressBar])