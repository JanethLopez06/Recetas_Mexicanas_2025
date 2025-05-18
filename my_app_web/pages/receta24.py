import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/paleta.png",
            alt="Paletas de Fresas y Manzanas Cubiertas con Chocolate",
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
        rx.text("Estas paletas de frutas frescas cubiertas con chocolate son un postre delicioso y divertido, perfecto para cualquier ocasión especial o como un antojo dulce."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 10 fresas grandes, lavadas y secas."),
        rx.text("- 2 manzanas, cortadas en trozos grandes."),
        rx.text("- 200 g de chocolate para derretir (oscuro, con leche o blanco)."),
        rx.text("- Palitos de madera o de paleta."),
        rx.text("- Chispas de colores, nueces trituradas o coco rallado (opcional para decorar)."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Inserta un palito en cada fresa y cada trozo de manzana."),
        rx.text("2. Derrite el chocolate a baño maría o en el microondas (en intervalos de 30 segundos, revolviendo cada vez)."),
        rx.text("3. Sumerge las frutas en el chocolate derretido hasta cubrirlas completamente."),
        rx.text("4. Decora con chispas, nueces o coco antes de que el chocolate se endurezca (opcional)."),
        rx.text("5. Coloca las frutas sobre papel encerado y deja enfriar hasta que el chocolate se solidifique."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>180 kcal</td></tr>
                            <tr><td>Proteínas</td><td>2 g</td></tr>
                            <tr><td>Carbohidratos</td><td>22 g</td></tr>
                            <tr><td>Grasas</td><td>10 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 15 minutos"),
        rx.text("🔥 Tiempo de enfriado: 10 minutos"),
        rx.text("🍽️ Rinde para: 6 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Seca bien las frutas para que el chocolate se adhiera correctamente."),
        rx.text("✔️ Puedes usar chocolate blanco para un contraste de color interesante."),
        rx.text("✔️ Guárdalas en refrigeración si no se consumen de inmediato."),

        rx.box(
            rx.image(
                src="/recetas/acom24.png",
                alt="Paletas de Fresas y Manzanas Cubiertas con Chocolate",
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
            rx.html('<a href="/receta23" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
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

def receta24() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Paletas de Fresas y Manzanas Cubiertas con Chocolate",
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
