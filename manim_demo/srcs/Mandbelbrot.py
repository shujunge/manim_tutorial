from manimlib.imports import *
from datetime import *

class Mandbelbrot(Scene):
    def construct(self):
        st_t = datetime.now()
        scale = 2
        iter_func = lambda z, c: z ** 2 + c
        iter_num = 128
        colors = color_gradient(['#182AFF', WHITE, BLACK], iter_num + 1)

        def get_color(c):
            z = complex(0, 0)
            num = 0
            while abs(z) < 2 and num < iter_num:
                z = iter_func(z, c)
                num += 1
            return colors[num]

        x_pn, y_pn = 140, 140
        sp = Square(stroke_width=0, fill_color=RED, fill_opacity=1).scale(4 * scale / y_pn / 2 * 1.12)
        for i in range(int(y_pn / 2) + 1):
            for j in range(x_pn):
                lij = (-x_pn / 2 + j) / x_pn * 4 * scale * RIGHT + \
                      (-y_pn / 2 + i) / y_pn * 4 * scale * UP
                c = complex(*(lij[:2] / scale)) / 1.6 - 0.6
                self.add(sp.copy().set_fill(color=get_color(c)).move_to(lij))
                self.add(sp.copy().set_fill(color=get_color(c)).move_to(lij * np.array([1, -1, 0])))
                if j == 1:
                    print('i = %d, j = %d\t' % (i, j), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        ed_t = datetime.now()
        tot_t = (ed_t - st_t).total_seconds()
        print('Total time : %d s' % tot_t)

        self.wait()



class Sandpile(Scene):
    CONFIG = {
        "d": 10,
        "size": 5120 * 1.5,
        "num": 500000,
        "maxh": 1,
        "field_size": 600,
        "fromtxt": None,
    }

    def construct(self):
        self.camera.set_frame_height(self.size)
        self.camera.set_frame_width(self.size)
        points = PMobject(stroke_width=self.d)

        if self.fromtxt is not None:
            field = np.loadtxt(self.fromtxt, dtype=int, delimiter=",")
            print("load field from file {}".format(self.fromtxt))
            center = self.field_size / 2
        else:
            field = np.zeros((self.field_size + 10, self.field_size + 10))
            center = int(self.field_size / 2)

            field[center, center] += self.num

            iters = 0
            t0 = time.time()
            dt0 = time.time()

            while np.max(field) >= self.maxh:
                toohigh = field >= self.maxh
                field[toohigh] -= self.maxh

                field[1:, :][toohigh[:-1, :]] += self.maxh / 4
                field[:-1, :][toohigh[1:, :]] += self.maxh / 4
                field[:, 1:][toohigh[:, :-1]] += self.maxh / 4
                field[:, :-1][toohigh[:, 1:]] += self.maxh / 4

                field[0:1, :] = 0
                field[:, 0:1] = 0

                iters += 1
                if iters % 1000 == 0:
                    dt1 = time.time()
                    print("finish {} iterations - {:.2f}s/1000it".format(iters, dt1 - dt0))
                    dt0 = time.time()

            t1 = time.time()
            print("{} iterations in {:.2f} seconds".format(iters, t1 - t0))
            np.savetxt("sand-{}.txt".format(self.num), field, fmt="%d", delimiter=",")

        t2 = time.time()
        colors = color_gradient([BLACK, GREEN, YELLOW], 4)
        for i in range(center * 2 + 3):
            dt0 = time.time()
            for j in range(center * 2 + 3):
                if field[i][j] != 0:
                    points.add_points(
                        [np.array([(-center + i) * self.d, (center - j) * self.d, 0])],
                        color=colors[int(field[i][j])]
                    )
            dt1 = time.time()
            print("finish {} in {:.2f} seconds".format(i, dt1 - dt0))
        t3 = time.time()
        if self.fromtxt is None:
            print("{} iterations in {:.2f} seconds".format(iters, t1 - t0))
        print("render in {:.2f} seconds".format(t3 - t2))

        self.add(points)
