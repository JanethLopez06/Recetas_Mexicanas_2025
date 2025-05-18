import reflex as rx

import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/sopes.png",
            alt="Sopes Mexicanos",
            width="100%",
            max_width="400px",
            style={
                "border": "4px solid #000",
                "borderRadius": "6px",
                "objectFit": "contain",
                "marginTop": "1em"
            }
        ),
        width="100%",
        # padding="1em",
        display="flex",
        justify_content="center"
    )


def contenido_box():
    return rx.box(
        rx.text(
            "¡Una delicia tradicional hecha con masa de maíz, frijoles y toppings al gusto!"),

        rx.heading("Ingredientes:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("- 2 tazas de masa de maíz"),
        rx.text("- 1/2 taza de frijoles refritos"),
        rx.text("- Lechuga picada"),
        rx.text("- Crema, queso fresco, salsa y cebolla"),
        rx.text("- Aceite para freír"),

        rx.heading("Preparación:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Forma círculos con la masa y cocínalos en comal."),
        rx.text("2. Pellizca las orillas para formar los bordes."),
        rx.text("3. Fríelos ligeramente para dar textura."),
        rx.text("4. Unta frijoles y añade los ingredientes al gusto."),

        rx.heading("Tabla nutricional:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
        <div class="nes-table-responsive" style="margin-top:1em;">
            <table class="nes-table is-bordered is-centered">
                <thead>
                    <tr><th>Nutriente</th><th>Cantidad</th></tr>
                </thead>
                <tbody>
                    <tr><td>Calorías</td><td>280 kcal</td></tr>
                    <tr><td>Proteínas</td><td>10 g</td></tr>
                    <tr><td>Carbohidratos</td><td>34 g</td></tr>
                    <tr><td>Grasas</td><td>12 g</td></tr>
                </tbody>
            </table>
        </div>
    """),
            width="100%",  # Asegura que ocupe todo el ancho disponible
            display="flex",  # Usa flexbox para centrar
            justify_content="center",  # Centrado horizontal
            align_items="center",  # Centrado vertical
            margin_top="2em",  # Margen superior para separación
        ),

        rx.heading("Información adicional:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 20 minutos"),
        rx.text("🔥 Tiempo de cocción: 10 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Si la masa está muy seca, puedes agregarle un poco de agua tibia."),
        rx.text("✔️ Usa un comal bien caliente para que los sopes se cocinen parejo."),
        rx.text(
            "✔️ Para un toque más crujiente, fríe ligeramente después de cocer en el comal."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("Para complementar estos deliciosos sopes, puedes servirlos con una rica agua de jamaica, "
                "un poco de arroz rojo o una salsa verde picante casera."),

        rx.box(
            rx.image(
                src="/recetas/acom3.png",
                alt="Sopes",
                width="100%",
                max_width="400px",
                style={
                    "border": "2px dashed #333",
                    "borderRadius": "6px",
                    "marginTop": "1em"
                }
            ),
            display="flex",
            justify_content="center",
            width="100%"
        ),


        rx.hstack(
            rx.html(
                '<a href="/receta2" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta4" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
            justify="center",
            margin_top="2em",
            width="100%",  # Asegura que ocupe todo el ancho disponible
            display="flex",  # Se asegura de que los botones se distribuyan correctamente
            flex_wrap="wrap",  # Permite que los botones se ajusten a diferentes tamaños de pantalla
            gap="1em"  # Espacio entre los botones
        ),
        width="100%",
        padding="1em"
    )


def receta3() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Sopes Mexicanos",
                size="lg",
                text_align="center",
                width="100%"  # ✅ Centrado correcto
            ),

            rx.box(
                imagen_box(),
                contenido_box(),
                display="flex",
                flex_direction=FLEX_DIRECTION,
                flex_wrap="wrap",
                gap="2em",
                width="100%",
                justify_content="center"
            ),

            padding_y="2em",
            padding_x="1em",  # ✅ Margen horizontal para móviles
            spacing="2em",
            max_width="1200px",
            width="100%"
        )
    )
