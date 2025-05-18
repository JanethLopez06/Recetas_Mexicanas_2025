import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MED="1.5em"  #Para textos
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"
    HUGE = "4.5em"         #  nueva opción más grande


# STYLESHEETS = [
#     "https://unpkg.com/nes.css@latest/css/nes.min.css",
#     "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
# ]

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap",
    "https://fonts.googleapis.com/css2?family=Inter&display=swap"
]


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,  # Press Start 2P para títulos
        "color": TextColor.ACCENT.value,
        "textAlign": "center"
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none",
            "font_size": Size.VERY_BIG.value,
            "font_family": Font.TEXT.value

        }
    },
    rx.text: {
        "font_family": Font.TEXT.value,  # Inter para textos
        "font_size": Size.MED.value
    },
    rx.el.span: {
        "font_family": Font.TEXT.value,
        "font_size": Size.MED.value
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important"
        }
    }
}

MAX_WIDTH_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",

    max_width=MAX_WIDTH
)
