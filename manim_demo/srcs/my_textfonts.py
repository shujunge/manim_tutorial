from manimlib.imports import *
"""
安装不同的字体
>>> sudo mkfontscale && sudo mkfontdir && fc-cache -fv
"""
class my_fonts_Demo(Scene):
    def construct(self):
        my_fonts_list = []
        with open("fonts.txt",'r') as f:
            alllines = f.readlines()
            for   lines in alllines:
                my_fonts_list.append(lines.split(": ")[1].split(",")[0].split("\n")[0].split(":")[0])

        my_fonts_list =list(set(my_fonts_list))
        print(my_fonts_list)
        print(len(my_fonts_list))

        all_fonts = VGroup()
        for index in range(len(my_fonts_list)):
            title = Text('%s:hello 重庆' %my_fonts_list[index], font=my_fonts_list[index]).scale(0.3)
            title[:4].set_color(BLUE)
            all_fonts.add(title)
        all_fonts.arrange(DOWN).arrange_in_grid(14, 2)
        self.play(LaggedStartMap(WiggleOutThenIn, all_fonts))
        self.wait()
        self.clear()

class Intro(my_fonts_Demo):

    def construct(self):
        super(Intro, self).construct()
        text_1 = Text('如何证明更一般的情况呢？', font='STKaiti', color=BLUE).scale(0.9).shift(UP * 1.8)
        # text_1 = TextMobject(r"\normalfont 如何 \bfseries 证明  \scshape 更一般的情况呢 23456").scale(0.9).shift(UP * 1.8)
        text_2 = Text('让我们来回顾一个经典的问题', font='STKaiti', color=YELLOW).scale(0.7).shift(UP * 0.25)

        achilles_svg = SVGMobject('./srcs/figs/Achilles.svg', color=BLUE, stroke_width=0.2).scale(1.25).to_corner(DOWN * 1.8 + LEFT * 6)
        tortoise_svg = SVGMobject('./srcs/figs/tortoise.svg', color=YELLOW).scale(0.64).to_corner(DOWN * 1.8 + RIGHT * 6)

        self.wait(0.4)
        self.play(Write(text_1), run_time=1.8)
        self.wait(0.6)
        self.play(Write(text_2), run_time=2)
        self.wait(0.4)
        self.play(FadeInFromLarge(achilles_svg))
        self.play(FadeInFromLarge(tortoise_svg))
        self.play(TurnInsideOut(achilles_svg), WiggleOutThenIn(tortoise_svg))

        self.wait(2)


class DecimalNumber(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            SingleStringTexMobject(char, **kwargs)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(SingleStringTexMobject("\\dots"))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = SingleStringTexMobject(self.unit, color=self.color)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        """
        Configuration is based first off instance attributes,
        but overwritten by any kew word argument.  Relevant
        key words:
        - include_sign
        - group_with_commas
        - num_decimal_places
        - field_name (e.g. 0 or 0.real)
        """
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumber(number, **full_config)
        # Make sure last digit has constant height
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)


class Integer(DecimalNumber):
    CONFIG = {
        "num_decimal_places": 0,
    }

    def get_value(self):
        return int(np.round(super().get_value()))
