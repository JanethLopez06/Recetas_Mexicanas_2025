import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import Size, Color, TextColor,HeadingSize
from my_app_web.Components.header_text import header_text


def partners() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                header_text(
                    icon="nes-icon is-large star",
                    text="Recetas sencillas, pero llenas de sabor y tradición.",
                    color=TextColor.PRIMARY.value,
                    font_size=HeadingSize.BIG,),
                spacing="0",
                padding_y=Size.MEDIUM.value,
                style=styles.MAX_WIDTH_style

            ),
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )
