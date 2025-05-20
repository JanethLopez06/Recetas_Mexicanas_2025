
import reflex as rx
from my_app_web.Styles.styles import  Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/nogada.png",
            alt="Chiles en Nogada",
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
        rx.text("El chile en nogada es un platillo típico de la gastronomía mexicana, originario de Puebla. Consiste en un chile poblano relleno de picadillo de carne de res y cerdo, bañado en una salsa de nuez y decorado con granada."),

        rx.heading("Ingredientes:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("- 6 chiles poblanos."),
        rx.text("- 500 g de carne de res molida."),
        rx.text("- 500 g de carne de cerdo molida."),
        rx.text("- 2 jitomates."),
        rx.text("- 1 cebolla."),
        rx.text("- 2 dientes de ajo."),
        rx.text("- 1/2 taza de almendras picadas."),
        rx.text("- 1/4 de taza de pasas."),
        rx.text("- 1/2 taza de acitrón (opcional)."),
        rx.text("- 1 taza de nuez de Castilla."),
        rx.text("- 1/4 de taza de crema fresca."),
        rx.text("- 1 granada."),
        rx.text("- Sal y pimienta al gusto."),

        rx.heading("Preparación:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("1. Asa los chiles poblanos, quítales la piel, las semillas y las venas."),
        rx.text("2. Cocina las carnes con la cebolla, el ajo y los jitomates picados hasta que estén doradas."),
        rx.text("3. Agrega las almendras, pasas y acitrón, y cocina por 5 minutos más."),
        rx.text("4. Rellena los chiles con el picadillo y colócalos en una fuente para hornear."),
        rx.text("5. Licúa las nueces con la crema y baña los chiles con esta salsa."),
        rx.text("6. Decora con granada y sirve caliente."),

        rx.heading("Tabla nutricional", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>350 kcal</td></tr>
                            <tr><td>Proteínas</td><td>20 g</td></tr>
                            <tr><td>Carbohidratos</td><td>25 g</td></tr>
                            <tr><td>Grasas</td><td>22 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 30 minutos"),
        rx.text("🔥 Tiempo de cocción: 45 minutos"),
        rx.text("🍽️ Rinde para: 6 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Si no encuentras acitrón, puedes omitirlo o usar ciruelas pasas."),
        rx.text("✔️ Asegúrate de quitar completamente las semillas y venas de los chiles."),
        rx.text("✔️ Puedes servir los chiles con arroz blanco para acompañar."),

        rx.heading("Acompañamientos sugeridos:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa de molcajete"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz blanco"),
        rx.text("🥤 Agua fresca de horchata"),

        rx.box(
            rx.image(
                src="/recetas/acom13.png",
                alt="Chiles en Nogada",
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
                '<a href="/receta12" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta14" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta13() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Chiles en Nogada",
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
