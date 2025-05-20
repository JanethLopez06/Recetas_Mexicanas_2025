import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import  Size


def instructions() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Bienvenido a la página de recetas",
                    text_align="center",
                    font_size=Size.BIG.value,
                    margin_top=Size.DEFAULT.value  # 👈 Esto sí generará espacio arriba
                ),
                rx.text("¡Aquí podrás disfrutar de deliciosas recetas mexicanas!"),
                rx.text("\n¿No sabes por dónde empezar? Aquí te explicamos cómo usar la página:"),
                rx.text("- Navega entre las recetas utilizando los botones 'Menú Principal' o 'Siguiente Receta'."),
                rx.text("- Cada receta incluye ingredientes, instrucciones y una tabla nutricional."),
                rx.text("- Si quieres ver más recetas, solo haz clic en 'Siguiente Receta'."),
                rx.text("- Disfruta de las instrucciones paso a paso para preparar tus platillos favoritos."),
                rx.spacer(size="large"),
                class_name="nes-container with-title",
                spacing="4",
                margin_top=Size.DEFAULT.value,
                align_items="start",
            ),
            font_size=Size.MEDIUM.value,
            style={**styles.MAX_WIDTH_style, "margin": "0 auto"},
            width="100%",
        ),
        padding=Size.SMALL.value,
        width="100%"
    )
