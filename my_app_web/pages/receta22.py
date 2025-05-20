import reflex as rx
from my_app_web.Styles.styles import  Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/flan.png",
            alt="Flan Napolitano",
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
        rx.text("El flan napolitano es un postre clásico y cremoso con un delicioso sabor a vainilla y caramelo, perfecto para cualquier ocasión."),

        rx.heading("Ingredientes:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("- 1 lata de leche condensada."),
        rx.text("- 1 lata de leche evaporada."),
        rx.text("- 4 huevos."),
        rx.text("- 1 cucharada de extracto de vainilla."),
        rx.text("- 1/2 taza de azúcar para el caramelo."),

        rx.heading("Preparación:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar el caramelo: Calienta el azúcar en una sartén hasta que se derrita y tome color dorado. Vierte en un molde para flan."),
        rx.text("2. Licuar los ingredientes: Mezcla la leche condensada, leche evaporada, huevos y vainilla hasta obtener una mezcla homogénea."),
        rx.text("3. Verter en el molde: Coloca la mezcla sobre el caramelo en el molde."),
        rx.text("4. Cocinar: Hornea a baño maría a 180°C por 50-60 minutos o hasta que al insertar un palillo, este salga limpio."),
        rx.text("5. Enfriar: Deja enfriar completamente y refrigera antes de desmoldar."),

        rx.heading("Tabla nutricional", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>320 kcal</td></tr>
                            <tr><td>Proteínas</td><td>8 g</td></tr>
                            <tr><td>Carbohidratos</td><td>40 g</td></tr>
                            <tr><td>Grasas</td><td>15 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 15 minutos"),
        rx.text("🔥 Tiempo de cocción: 60 minutos"),
        rx.text("🍽️ Rinde para: 8 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Asegúrate de que el caramelo no se queme para evitar un sabor amargo."),
        rx.text("✔️ Puedes agregar queso crema a la mezcla para una textura más rica."),
        rx.text("✔️ Usa moldes individuales para porciones más elegantes."),

        rx.box(
            rx.image(
                src="/recetas/acom22.png",
                alt="Flan Napolitano",
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
            rx.html('<a href="/receta21" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta23" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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

def receta22() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Flan Napolitano",
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
