import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import Size


def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Sazón Mexicano",
                text_align="center",
                font_size=Size.BIG.value,
                padding_bottom=Size.DEFAULT.value,

                margin_top=Size.BIG.value  # esto crea espacio arriba del texto

            ),
            rx.flex(
                rx.image(
                    src="/acerca.png",
                    alt="Imagen pixel de cocina.",
                    width="16em",
                    height="16em",
                    margin_right=Size.BIG.value
                ),
                rx.vstack(
                    rx.box(
                        rx.heading("Acerca:"),
                        font_size=Size.MEDIUM.value,
                        class_name="nes-balloon from-left",
                        text_align="center"
                    ),
                    rx.text(
                        "Este proyecto es una muestra de mi pasión por la cocina mexicana y el desarrollo web. " \
                        "Cada receta ha sido cuidadosamente seleccionada y presentada con un diseño retro, combinando" \
                        " tradición culinaria con creatividad digital. El objetivo es compartir sabores auténticos mientras " \
                        "demuestro mis habilidades en programación y diseño.",
                        as_="span",
                        text_align="center"
                    ),
                    # rx.link(
                    #     "CocinaMexicana2025",
                    #     href=constants.RECETAS_COCINA_URL,
                    #     is_external=True,
                    #     color=TextColor.TERCIARY.value,
                    #     padding_top=Size.BIG.value,
                    #     font_size=Size.MEDIUM.value,
                    #     text_align="center"
                    # ),
                    align_items="start"
                ),
                flex_direction=styles.FLEX_DIRECTION,  # Para que la página sea responsive
                align_items="center",
                justify="center",
                spacing=Size.DEFAULT.value,
                width="auto"
            ),
            spacing=Size.BIG.value,
            align_items="center",
            style={**styles.MAX_WIDTH_style, "margin": "0 auto"}
        ),
        width="100%"
    )
