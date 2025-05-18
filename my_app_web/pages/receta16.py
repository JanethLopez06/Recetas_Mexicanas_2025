import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/birria.png",
            alt="Birria de Res",
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
        rx.text("La birria de res es un platillo tradicional mexicano, originario de Jalisco, preparado con carne de res cocida en un guiso de chiles y especias."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 1 kg de carne de res (chuck roast o espaldilla)."),
        rx.text("- 4 chiles guajillos secos."),
        rx.text("- 2 chiles anchos secos."),
        rx.text("- 3 dientes de ajo."),
        rx.text("- 1/2 cebolla."),
        rx.text("- 1 rama de canela."),
        rx.text("- 4 clavos de olor."),
        rx.text("- 1 hoja de laurel."),
        rx.text("- Sal y pimienta al gusto."),
        rx.text("- 1/4 de taza de vinagre de manzana."),
        rx.text("- 1/2 taza de caldo de res."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar la salsa: Hidrata los chiles guajillo y ancho en agua caliente. Licúa con el ajo, cebolla, vinagre, canela y clavos hasta obtener una salsa suave."),
        rx.text("2. Cocinar la carne: En una olla grande, coloca la carne, la salsa y el caldo de res. Cocina a fuego lento por 2-3 horas hasta que la carne esté tierna."),
        rx.text("3. Desmenuzar la carne: Una vez cocida, desmenuza la carne y sirve en un plato hondo con un poco del caldo."),
        rx.text("4. Servir: Acompaña con cebolla picada, cilantro y limones. Puedes comerla con tortillas o en tacos."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>350 kcal</td></tr>
                            <tr><td>Proteínas</td><td>45 g</td></tr>
                            <tr><td>Carbohidratos</td><td>15 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 20 minutos"),
        rx.text("🔥 Tiempo de cocción: 3 horas"),
        rx.text("🍽️ Rinde para: 6-8 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes acompañar la birria con arroz o frijoles."),
        rx.text("✔️ Si prefieres un toque más picante, añade un chile de árbol al guiso."),
        rx.text("✔️ Puedes hacer birria en cazuela de barro para un sabor más auténtico."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🌮 Tacos de birria"),
        rx.text("🍞 Pan de elote"),
        rx.text("🥑 Guacamole"),
        rx.text("🌿 Salsa de chile de árbol"),

        rx.box(
            rx.image(
                src="/recetas/acom16.png",
                alt="Birria de Res",
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
                '<a href="/receta15" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta17" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta16() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Birria de Res",
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
