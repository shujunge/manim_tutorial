from manimlib.imports import *

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -2,
        "y_max" : 2,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10, 12, 2),
        "y_labeled_nums": range(-2, 3, 1),
    }

    def construct(self):

        self.setup_axes(animate=True)
        func_graph= self.get_graph(self.func_to_graph, COLOR=self.function_color)
        func_graph2= self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2= self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.wait()
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))
        self.wait()

        self.clear()
        my_line = NumberLine(animate=True).set_color(RED)
        self.play(FadeInFromDown(my_line))
        self.wait()

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)

class my_numberplane(Scene):

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

        self.play(ShowCreation(plane))
        self.wait()

        numberline = NumberLine(axis_config={"stroke_color": BLACK}, plot_depth=-5) \
            .add_coordinates(y_vals=[1, 2, 3, -1, -2])