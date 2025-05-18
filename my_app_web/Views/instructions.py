import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size


def instructions() -> rx.Component:
    return rx.center(  # CENTRA horizontalmente
        rx.box(
            rx.vstack(
                rx.heading("Bienvenido a la página de recetas",
                           size="lg", text_align="center"),
                class_name="title",
                color=TextColor.ACCENT.value,
                font_size=Size.MEDIUM.value,

                margin_top="0px"


            ),

            rx.text("¡Aquí podrás disfrutar de deliciosas recetas mexicanas!"),
            rx.text(
                "\n¿No sabes por dónde empezar? Aquí te explicamos cómo usar la página:"),
            rx.text(
                "- Navega entre las recetas utilizando los botones 'Menú Principal' o 'Siguiente Receta'."),
            rx.text(
                "- Cada receta incluye ingredientes, instrucciones y una tabla nutricional."),
            rx.text(
                "- Si quieres ver más recetas, solo haz clic en 'Siguiente Receta'."),
            rx.text(
                "- Disfruta de las instrucciones paso a paso para preparar tus platillos favoritos."),
            # Espacio entre las instrucciones y la receta
            rx.spacer(size="large"),
            class_name="nes-container with-title",
            spacing=Size.MEDIUM.value,
            align_items="start",  # Mantiene el texto alineado a la izquierda
        ),
        font_size=Size.MEDIUM.value,
        style={**styles.MAX_WIDTH_style,
               "margin": "0 auto"},  # CENTRADO por CSS
        width="100%",
    ),
    padding = Size.SMALL.value,
    width = "100%"
    