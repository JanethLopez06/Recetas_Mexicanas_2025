import reflex as rx
import my_app_web.constants as constants
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import Size, TextColor


def footer() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.vstack(  # Contenido textual a la izquierda
                rx.text(
                    "Sazón Mexicano 2025.",
                    font_size=Size.MED.value,
                    margin_bottom=Size.ZERO.value,
                    text_align="center",
                    margin_top=Size.DEFAULT.value
                ),
                rx.link(
                    rx.hstack(
                        rx.text("Creado  "),
                        rx.el.i(class_name="nes-icon is-small heart"),
                        rx.text(" por Jessica López © 2025"),
                        spacing="2",
                        align_items="center"
                    ),
                    href=constants.JESSICA_URL,
                    is_external=True,
                    font_size=Size.MEDIUM.value,
                    color=TextColor.TERCIARY.value
                ),
                spacing="2",
                align_items="center"
            ),
            rx.image(  # Imagen a la derecha
                src="/logo.png",
                alt="Logo de cocina mexicana",
                class_name="nes-avatar is-large",
                margin_left=Size.MEDIUM.value
            ),
            align_items="center",
            justify_content="center",
            padding_bottom=Size.DEFAULT.value,
            style={**styles.MAX_WIDTH_style, "margin": "0 auto"},
            width="100%",
            padding=Size.SMALL.value
        ),
        width="100%"
    )
