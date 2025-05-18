import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/carne.png",
            alt="Carne Asada a la Mexicana",
            width="100%",
            max_width="200px",
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
        rx.text("La carne asada a la mexicana es un platillo delicioso que combina carne de res marinada y asada, servida con cebollitas, chiles y salsa fresca."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 1 kg de carne para asar (como arrachera o bistec)."),
        rx.text("- 2 cebollas medianas (cortadas en rodajas)."),
        rx.text("- 2 chiles serranos o jalapeños."),
        rx.text("- 1 manojo de cilantro fresco."),
        rx.text("- Jugo de 2 limones."),
        rx.text("- Sal y pimienta al gusto."),
        rx.text("- Aceite para asar."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Marinar la carne: Exprime el jugo de limón sobre la carne y sazona con sal y pimienta. Deja reposar por 15 minutos."),
        rx.text("2. Asar la carne: Cocina la carne en una parrilla o sartén caliente por 4-5 minutos de cada lado."),
        rx.text("3. Asar las cebollas y chiles: Coloca las rodajas de cebolla y los chiles sobre la parrilla y cocina hasta que estén dorados."),
        rx.text("4. Servir: Corta la carne en tiras y acompáñala con las cebollas y chiles asados. Decora con cilantro fresco y acompaña con tortillas."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>250 kcal</td></tr>
                            <tr><td>Proteínas</td><td>28 g</td></tr>
                            <tr><td>Carbohidratos</td><td>8 g</td></tr>
                            <tr><td>Grasas</td><td>14 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 10 minutos"),
        rx.text("🔥 Tiempo de cocción: 15 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes acompañar con arroz o frijoles."),
        rx.text("✔️ Si prefieres un sabor más picante, puedes agregar más chiles."),
        rx.text("✔️ Usa una parrilla para obtener un sabor ahumado delicioso."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa roja o verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz mexicano"),
        rx.text("🥗 Ensalada fresca"),

        rx.box(
            rx.image(
                src="/recetas/acom18.png",
                alt="Carne Asada a la Mexicana",
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
                '<a href="/receta17" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta19" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta18() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Carne Asada a la Mexicana",
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
