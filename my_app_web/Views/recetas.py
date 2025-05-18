import reflex as rx
from my_app_web.Components.recetas_grid import recetas_grid
from my_app_web.Styles.styles import Size, Color, TextColor
from my_app_web.Components.header_text import header_text


def recetas() -> rx.Component:
    return rx.box(
        rx.vstack(
            header_text(
                "heart",
                "¡Recetas!",
                color=TextColor.PRIMARY.value,
            ),
            rx.spacer(size=Size.MEDIUM.value),

            # Aquí empieza el grid dentro del hstack
            rx.hstack(
                rx.grid(
                    *[recetas_grid(i) for i in range(24)],  # Asegúrate de que aquí pases todos los índices de receta
                    columns=rx.breakpoints(
                        initial="2",
                        xs="3",
                        sm="4",
                        md="6",
                        lg="8",
                        xl="8"
                    ),
                    gap=Size.SMALL.value,
                    width="100%",
                    max_width="1200px",
                    padding=Size.MEDIUM.value
                ),
                justify="center",
                width="100%"
            ),
            rx.spacer(size=Size.MEDIUM.value),
            align_items="center"  # Centra horizontalmente todo lo del VStack
        ),
        display="flex",
        flex_direction="column",
        align_items="center",
        bg=Color.ACCENT.value,
        width="100%",
    )
