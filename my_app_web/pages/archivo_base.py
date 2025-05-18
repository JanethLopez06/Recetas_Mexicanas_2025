import reflex as rx

import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


# Función para la imagen de la receta
def imagen_box(imagen_src: str, alt_text: str):
    return rx.box(
        rx.image(
            src=imagen_src,
            alt=alt_text,
            width="100%",
            max_width="500px",
            style={
                "border": "4px solid #000",
                "borderRadius": "8px",
                "objectFit": "contain"
            }
        ),
        width="100%",
        padding="1em",
        display="flex",
        justify_content="center"
    )


# Función para el contenido de la receta
def contenido_box(titulo_ingredientes: str, ingredientes: list, 
                  titulo_preparacion: str, preparacion: list, 
                  tabla_nutricional: str, tiempo_preparacion: str, tiempo_coccion: str, 
                  raciones: str, dificultad: str, consejos: list, acompañamientos: list, imagen_acompanamiento: str):
    return rx.box(
        rx.text("¡Deliciosa receta lista para preparar!"),

        rx.heading(titulo_ingredientes, margin_top="2em", font_size=Size.DEFAULT.value),
        *[rx.text(ingrediente) for ingrediente in ingredientes],

        rx.heading(titulo_preparacion, margin_top="2em", font_size=Size.DEFAULT.value),
        *[rx.text(paso) for paso in preparacion],

        rx.heading("Tabla nutricional:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.html(tabla_nutricional),

        rx.heading("Información adicional:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text(f"⏱️ Tiempo de preparación: {tiempo_preparacion}"),
        rx.text(f"🔥 Tiempo de cocción: {tiempo_coccion}"),
        rx.text(f"🍽️ Rinde para: {raciones}"),
        rx.text(f"⭐ Dificultad: {dificultad}"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        *[rx.text(consejo) for consejo in consejos],

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        *[rx.text(acomp) for acomp in acompañamientos],

        rx.image(
            src=imagen_acompanamiento,
            alt="Acompañamiento",
            width="100%",
            max_width="400px",
            style={"border": "2px dashed #333", "borderRadius": "6px", "marginTop": "1em"}
        ),

        rx.hstack(
            rx.html('<a href="/receta2" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta4" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
            justify="center",
            margin_top="2em",
            width="100%",
            display="flex",
            flex_wrap="wrap",
            gap="1em"
        ),
        width="100%",
        padding="1em"
    )


# Función base para cada receta
def receta_base(titulo_receta: str, imagen_receta: str, alt_text: str,
                titulo_ingredientes: str, ingredientes: list,
                titulo_preparacion: str, preparacion: list,
                tabla_nutricional: str, tiempo_preparacion: str, 
                tiempo_coccion: str, raciones: str, dificultad: str,
                consejos: list, acompañamientos: list, imagen_acompanamiento: str) -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                titulo_receta,
                size="lg",
                text_align="center",
                width="100%"
            ),

            rx.box(
                imagen_box(imagen_receta, alt_text),
                contenido_box(titulo_ingredientes, ingredientes, titulo_preparacion, 
                              preparacion, tabla_nutricional, tiempo_preparacion, 
                              tiempo_coccion, raciones, dificultad, consejos, 
                              acompañamientos, imagen_acompanamiento),
                display="flex",
                flex_direction=FLEX_DIRECTION,
                flex_wrap="wrap",
                gap="2em",
                width="100%",
                justify_content="center"
            ),

            padding_y="2em",
            padding_x="1em",
            spacing="2em",
            max_width="1200px",
            width="100%"
        )
    )
