import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/gelatina.png",
            alt="Gelatina de Mosaico",
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
        rx.text("La gelatina de mosaico es un postre colorido y divertido hecho con cubos de gelatina de sabores mezclados en una base de gelatina con leche."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 3 sobres de gelatina de diferentes sabores (fresa, limón, uva)."),
        rx.text("- 1 lata de leche condensada."),
        rx.text("- 1 lata de leche evaporada."),
        rx.text("- 1 taza de agua caliente."),
        rx.text("- 2 sobres de grenetina natural."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar las gelatinas de sabores según las instrucciones del paquete y dejar cuajar en moldes planos. Luego cortar en cubos."),
        rx.text("2. Disolver la grenetina en el agua caliente y dejar enfriar un poco."),
        rx.text("3. Mezclar la leche condensada, leche evaporada y la grenetina disuelta."),
        rx.text("4. Colocar los cubos de gelatina en un molde grande y verter la mezcla de leche. Refrigerar hasta que cuaje."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>180 kcal</td></tr>
                            <tr><td>Proteínas</td><td>4 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
                            <tr><td>Grasas</td><td>5 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 20 minutos (+ tiempo de refrigeración)"),
        rx.text("🔥 Tiempo de cocción: 0 minutos"),
        rx.text("🍽️ Rinde para: 8 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa moldes de silicona para facilitar el desmolde."),
        rx.text("✔️ Asegúrate de que la mezcla de leche esté fría antes de verter sobre los cubos de gelatina."),
        rx.text("✔️ Puedes agregar esencia de vainilla para más sabor."),

        rx.box(
            rx.image(
                src="/recetas/acom20.png",
                alt="Gelatina de Mosaico",
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
            rx.html('<a href="/receta19" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta21" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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

def receta20() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Gelatina de Mosaico",
                size="lg",
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
            spacing="2em",
            max_width="1200px",
            width="100%"
        )
    )
