import reflex as rx
import my_app_web.constants as constants
from my_app_web.Styles.styles import Size, Color
from my_app_web.Components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/ico.png",
                alt="Imagen pixel art de Cocina con estilo de cocina",
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value
            ),
            rx.heading(""
                    "Sazón Mexicano",
                    font_size=Size.DEFAULT.value,

                    margin_top=Size.BIG.value  # esto crea espacio arriba del texto

                    ),


            rx.spacer(),
            link_icon(

                "github",
                constants.GITHUB_LINK
            ),
            width="100%",  # Coma añadida
        ),  # Cierre de rx.hstack
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",

        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,  # Antes era DEFAULT o BIG
        z_index="999",
        top="0",
        width="100%",
    )
