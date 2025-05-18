import reflex as rx
import my_app_web.constants as constants
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import Size, Color, TextColor
# Importar la función header_text
from my_app_web.Components.header_text import header_text
from my_app_web.Components.button import button  # Si es necesario


def author() -> rx.Component:
    return rx.center(
        rx.vstack(
            header_text(
                icon="like", 
                text="Hola, mi nombre es Jessica López",
                color=TextColor.ACCENT.value,
                font_size=Size.DEFAULT.value
                
                
            ),
            rx.flex(
                rx.image(
                    
                    src="/Jessica.png",

                    width="220px",
                    height="220px",
                    bg=Color.PRIMARY.value,
                    padding="2px",
                    border=f"4px solid {Color.SECONDARY.value}",
                    border_radius="20%",
                    margin_right=Size.SMALL.value,
                    margin_bottom=Size.SMALL.value
                ),
                rx.vstack(
                    rx.text("• Soy ingeniera de formación y cocinera de corazón. Desde pequeña me ha encantado experimentar en la cocina, especialmente con recetas tradicionales mexicanas que me conectan con mis raíces."),
                    rx.text("• Esta página nació como un espacio para compartir sabores, historias y trucos que he aprendido con el tiempo. Me encanta crear platillos sencillos pero llenos de sabor, perfectos para quienes quieren cocinar sin complicaciones y con ingredientes accesibles."),
                    rx.text("• Aquí encontrarás recetas de toda la vida, ideas fáciles para el día a día y un toque retro porque... ¡me encanta el estilo pixelado y los colores brillantes!"),
                    font_size=Size.MEDIUM.value,
                    spacing="4",  # Espacio vertical entre cada línea
                    align_items="start",


                ),
                spacing=Size.DEFAULT.value,
                align_items="center",
                justify="center",
                flex_direction=styles.FLEX_DIRECTION,
                width="auto"  # ❗ Cambiado de "100%" a "auto"
            ),
            align_items="center",
            spacing=Size.BIG.value,
            style={**styles.MAX_WIDTH_style, "margin": "0 auto"},

        ),
        width="100%"
    )
