import reflex as rx

from my_app_web.Styles.styles import Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/chiles.png",
            alt="Chiles Rellenos",
            width="100%",
            max_width="300px",
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


def contenido_box():
    return rx.box(
        rx.text("Tradicional platillo mexicano hecho con chiles poblanos rellenos, capeados y bañados en salsa. Su sabor ahumado y relleno jugoso los hace irresistibles."),

        rx.heading("Ingredientes:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("- 4 chiles poblanos grandes."),
        rx.text("- 200 g de queso Oaxaca o panela."),
        rx.text("- 3 huevos (separar claras y yemas)."),
        rx.text("- 2 dientes de ajo. "),
        rx.text("- 1/2 taza de harina. "),
        rx.text("- Aceite vegetal para freír."),
        rx.text("- Sal al gusto."),


        rx.heading("Preparación:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Asa los chiles sobre fuego directo hasta que la piel esté negra."),
        rx.text(
            "2. Colócalos en una bolsa de plástico 10 min, luego pélalos cuidadosamente."),
        rx.text("3. Haz un corte lateral y retira las semillas."),
        rx.text("4. Rellena con queso."),
        rx.text(
            "5. Bate las claras a punto de nieve, añade las yemas y mezcla suavemente"),
        rx.text("6. Pasa los chiles por harina, luego por el huevo batido."),
        rx.text("7. Fríe en aceite caliente hasta dorar."),
        rx.text("Escúrrelos sobre papel absorbente"),



        rx.heading("Tabla nutricional", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>320 kcal</td></tr>
                            <tr><td>Proteínas</td><td>14 g</td></tr>
                            <tr><td>Carbohidratos</td><td>18 g</td></tr>
                            <tr><td>Grasas</td><td>20 g</td></tr>
                        </tbody>
                    </table>
                </div>
            """),
            width="100%",
            display="flex",
            justify_content="center",
            align_items="center",
            margin_top="2em",
        ),

        rx.heading("Información adicional:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 30 minutos"),
        rx.text("🔥 Tiempo de cocción: 15 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes rellenarlos también con picadillo."),
        rx.text(
            "✔️ Para un capeado más esponjoso, asegúrate de que las claras estén bien batidas."),
        rx.text("✔️ Sirve con salsa de jitomate casera caliente."),


        rx.heading("Acompañamientos sugeridos:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("🌾 Arroz a la mexicana"),
        rx.text("🥗 Ensalada de lechuga con jitomate"),
        rx.text("🟡 Tortillas de maíz calientes"),



        rx.box(
            rx.image(
                src="/recetas/acom5.png",
                alt="Chiles Rellenos",
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
                '<a href="/receta4" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta6" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta5() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Chiles Rellenos",
                font_size=Size.MED.value,
                text_align="center",
                width="100%"
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
            padding_x="1em",
            spacing="8",
            max_width="1200px",
            width="100%"
        )
    )
