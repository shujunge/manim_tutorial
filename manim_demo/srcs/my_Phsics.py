from manimlib.imports import *


class PhysicExample(PhysicScene):
    def construct(self):

        self.set_gravity(9.8 * DOWN)
        grd_body = self.space.static_body
        grd_seg = pymunk.Segment(grd_body, (-10000, -2000), (10000, -2000), 0)
        grd_seg.friction = 0.7
        grd_shape = Line(
            LEFT * 10,
            RIGHT * 10
        ).shift(2 * DOWN)

        ground = PhysicMobject(grd_body, grd_seg, grd_shape)
        self.add_static_obj(ground)

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
