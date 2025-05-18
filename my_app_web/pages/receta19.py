import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/arroz.png",
            alt="Arroz con Leche",
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
        rx.text("El arroz con leche es un postre tradicional cremoso y dulce preparado con arroz, leche, azúcar y canela."),

        rx.heading("Ingredientes:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("- 1 taza de arroz blanco."),
        rx.text("- 4 tazas de leche entera."),
        rx.text("- 1 taza de agua."),
        rx.text("- 1 rama de canela."),
        rx.text("- 1 lata de leche condensada."),
        rx.text("- 1 cucharadita de esencia de vainilla (opcional)."),
        rx.text("- Canela en polvo para decorar."),

        rx.heading("Preparación:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Hervir el arroz: Cocina el arroz con el agua y la rama de canela hasta que el agua se absorba."),
        rx.text(
            "2. Agregar la leche: Añade la leche y cocina a fuego bajo, removiendo constantemente."),
        rx.text(
            "3. Endulzar: Agrega la leche condensada y la vainilla. Cocina hasta que espese un poco."),
        rx.text("4. Servir: Deja enfriar y espolvorea con canela antes de servir."),

        rx.heading("Tabla nutricional", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>200 kcal</td></tr>
                            <tr><td>Proteínas</td><td>5 g</td></tr>
                            <tr><td>Carbohidratos</td><td>35 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 10 minutos"),
        rx.text("🔥 Tiempo de cocción: 30 minutos"),
        rx.text("🍽️ Rinde para: 6 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa leche entera para una textura más cremosa."),
        rx.text("✔️ Remueve constantemente para evitar que se pegue."),
        rx.text("✔️ Puedes agregar pasas o ralladura de limón para un sabor especial."),

        rx.box(
            rx.image(
                src="/recetas/acom19.png",
                alt="Arroz con Leche",
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
                '<a href="/receta18" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta20" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta19() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Arroz con Leche",
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
