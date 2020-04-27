import warnings
warnings.filterwarnings('ignore')
from manimlib.imports import *
from srcs.utils import run


class Introduction(TeacherStudentsScene):
    CONFIG = {
        "student_colors": [BLUE_D, BLUE_E, PINK],
        "teacher_color": GREY_BROWN,
        "student_scale_factor": 0.7,
        "seconds_to_blink": 2,
        "screen_height": 3,
    }
    def construct(self):

        self.tencher_says_1 = Text("学习平面几何可以使得人变聪明. --爱因斯坦",color=BLUE)
        self.students1 = Text("哇! 这回可以好好学习平面几何了!").set_color(BLUE)
        self.students2 = Text("老师,爱因斯坦好像没说过这话吧!").set_color(BLUE)
        self.students3_1 = Text("这不重要吧....").set_color(BLUE)
        self.students3_2 = Text("老师快开始吧,我已经破不急待了想学习新知识了").set_color(BLUE)
        self.tencher_says_2 = Text("好的,我们开始今天的课程.").set_color(BLUE)


    def Introduction_Animation(self):

        # teacher
        self.play(PiCreatureSays(self.teacher, self.tencher_says_1, self.teacher.change, "speaking", bubble_kwargs={"width": 7, "height": 2, "direction": RIGHT}))
        self.change_all_student_modes("pondering", look_at_arg=self.tencher_says_1)
        self.play(self.teacher.change, "happy") # FadeOut(self.teacher.bubble)
        self.wait()
        self.play(RemovePiCreatureBubble(self.teacher))
        self.wait()

        # student1
        self.play(PiCreatureSays(self.students[0], self.students1, bubble_kwargs={"width": 7, "height": 2, "direction": LEFT}))
        self.change_all_student_modes("pondering", look_at_arg=self.students[0], added_anims=[self.students[0].look_at, self.students1])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[0]))
        self.wait()

        # student2
        self.play(PiCreatureSays(self.students[1], self.students2, bubble_kwargs={"width": 7, "height": 2, "direction": LEFT}))
        self.change_all_student_modes("pondering", look_at_arg=self.students[1], added_anims=[self.students[1].look_at, self.students2])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[1]))
        self.wait()

        # student3
        self.play(PiCreatureSays(self.students[2], self.students3_1, bubble_kwargs={"width": 5, "height": 2, "direction": RIGHT}))
        self.change_all_student_modes("happy", look_at_arg=self.students[2], added_anims=[self.students[2].look_at, self.students[1]])
        self.wait(2)
        self.play(RemovePiCreatureBubble(self.students[2]))
        self.wait()
        self.play(PiCreatureSays(self.students[2], self.students3_2, bubble_kwargs={"width": 7, "height": 3, "direction": LEFT}))
        self.change_all_student_modes("happy", look_at_arg=self.students[2], added_anims=[self.students[2].look_at, self.students3_2])
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[2])) #RemovePiCreatureBubble(self.students[2])
        self.wait()

        # teacher
        self.play(PiCreatureSays(self.teacher, self.tencher_says_2, bubble_kwargs={"width": 7, "height": 2, "direction": RIGHT}))
        self.change_all_student_modes("happy")
        self.wait()

Total_class = [Introduction,]
class LogoDemo(*Total_class):
    def construct(self):
        super(LogoDemo, self).construct()
        for class_instance in Total_class:
            super(class_instance, self).construct()

        self.Introduction_Animation()

if __name__ == "__main__":

    run([LogoDemo], l=True)