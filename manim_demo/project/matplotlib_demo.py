from manimlib.imports import *
from srcs.utils import run

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from sklearn import svm # sklearn = scikit-learn
from sklearn.datasets import make_moons


def mplfig_to_npimage(fig):

    """ Converts a matplotlib figure to a RGB frame after updating the canvas"""
    #  only the Agg backend now supports the tostring_rgb function

    canvas = FigureCanvasAgg(fig)
    canvas.draw() # update/draw the elements

    # get the width and the height to resize the matrix
    l,b,w,h = canvas.figure.bbox.bounds
    w, h = int(w), int(h)
    #  exports the canvas to a string buffer and then to a numpy nd.array
    buf = canvas.tostring_rgb()
    image= np.frombuffer(buf, dtype=np.uint8)
    plt.close()
    return image.reshape(h, w, 3)


def make_frame_mpl(t):
    fig_mpl, ax = plt.subplots(1, figsize=(5, 3), facecolor='white')
    xx = np.linspace(-2, 2, 200)  # x向量
    zz = lambda d: np.sinc(xx ** 2) + np.sin(xx + d)  # （变化的）Z向量
    ax.set_title("Elevation in y=0")
    ax.set_ylim(-1.5, 2.5)
    line, = ax.plot(xx, zz(0), lw=3)
    line.set_ydata( zz(np.pi*t))  # 更新曲面
    return mplfig_to_npimage(fig_mpl) # 图形的RGB图像


def make_frame(t):

    X, Y = make_moons(50, noise=0.1, random_state=2)  # 半随机数据

    fig, ax = plt.subplots(1, figsize=(4, 4), facecolor=(1, 1, 1))
    fig.subplots_adjust(left=0, right=1, bottom=0)
    xx, yy = np.meshgrid(np.linspace(-2, 3, 500), np.linspace(-1, 2, 500))
    ax.clear()
    ax.axis('off')
    ax.set_title("SVC classification", fontsize=16)

    classifier = svm.SVC(gamma=2, C=1)
    # 不断变化的权重让数据点一个接一个的出现
    weights = np.minimum(1, np.maximum(0, t**2+10-np.arange(50)))
    classifier.fit(X, Y, sample_weight=weights)
    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=plt.cm.bone, alpha=0.8,
                vmin=-2.5, vmax=2.5, levels=np.linspace(-2,2,20))
    ax.scatter(X[:,0], X[:,1], c=Y, s=50*weights, cmap=plt.cm.bone)

    return mplfig_to_npimage(fig)


class manim_with_animation(Scene):

    def construct(self):

        during_times = ValueTracker(0)
        self.img = ImageMobject(make_frame_mpl(0))
        self.left_img = ImageMobject(make_frame(0))


        self.img.add_updater(lambda d: d.set_array(make_frame_mpl(during_times.get_value())))
        self.img.shift(2*RIGHT)

        self.left_img.add_updater(lambda d: d.set_array(make_frame(during_times.get_value())))
        self.left_img.shift(2*LEFT)

        self.play(ShowCreation(self.img), ShowCreation(self.left_img), run_times=2)
        for i in range(6):
            self.play(during_times.increment_value, 0.5*i, rate_func=linear,run_times=0.5*i)
        #
        # for i in range(6)[::-1]:
        #     self.play(during_times.increment_value, 0.1*i, rate_func=linear,run_times=0.1*i)
        self.wait()



if __name__=="__main__":

    run([manim_with_animation])