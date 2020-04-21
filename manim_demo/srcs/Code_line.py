from manimlib.imports import *


class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'manimlib/utils/color.py': GOLD,
            '#': GOLD,
            '_C': BLUE,
            'BLUE_C': BLUE,
            'BLUE': BLUE,
            'GREEN': GREEN,
            'YELLOW': YELLOW,
            'RED': RED,
            'RGB': PURPLE,
            'RGBA': PURPLE,
            'rgb': PURPLE,
            'int_rgb': PURPLE,
            'hex': PURPLE,
            'Color': GREEN,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'Mobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'GREY_BROWN': GREY_BROWN,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            'radius': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,
            "~": "#EBEBEB",
            "vg2": DARK_GRAY,
            'hex_to_rgb': BLUE_D,
            'rgb_to_hex': BLUE_D,
            'color_to_rgb': BLUE_D,
            'rgb_to_color': BLUE_D,
            'color_to_int_rgb': BLUE_D,
            'get_hex_l': BLUE_D,
            'invert_color': BLUE_D,
            'interpolate_color': BLUE_D,
            'average_color': BLUE_D,
            'color_gradient': BLUE_D,
            'random_color': BLUE_D,
            'alpha': GOLD,
            '#6cf': "#66CCFF",
            '#66CCFF': "#66CCFF",
            '#930': "#993300",
            '#9da288': "#9da288",
            'style': PURPLE,
            'stroke': BLUE_D,
            'fill': BLUE_D,
            'background_stroke': BLUE_D,
            'opacity': BLUE_D,
            'set_color': BLUE_D,
            'set_fill': BLUE_D,
            'set_background_stroke': BLUE_D,
            "stroke_color": ORANGE,
            "stroke_opacity": ORANGE,
            "fill_color": ORANGE,
            "fill_opacity": ORANGE,
            "background_stroke_color": ORANGE,
            "background_stroke_opacity": ORANGE,
            "set_color_by_gradient": BLUE_D,
            "set_colors_by_radial_gradient": BLUE_D,
            "outer_color": RED,
            "set_sheen_direction": BLUE_D,
            "set_sheen": BLUE_D,
            "sheen": BLUE_D,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }
    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class DecimalNumberText(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "text_config": {
            "font": "Consolas",
            "size": 0.4,
            "color": GOLD,
        }
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
            Text(char, **kwargs, **self.text_config)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(Text("...", **self.text_config))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = Text(self.unit, color=self.color, **self.text_config)
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
        new_decimal = DecimalNumberText(number, **full_config)
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


class TestDecimalNumberText(Scene):
    def construct(self):
        decimal = DecimalNumberText(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()