import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/pescado.png",
            alt="Pescado a la Veracruzana",
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
        rx.text("El pescado a la veracruzana es un platillo típico de la región del Golfo de México, preparado con pescado fresco, tomate, aceitunas y alcaparras."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 4 filetes de pescado (como huachinango o robalo)."),
        rx.text("- 2 tomates grandes (picados)."),
        rx.text("- 1/4 de taza de aceitunas verdes o negras."),
        rx.text("- 2 cucharadas de alcaparras."),
        rx.text("- 1/4 de cebolla morada (en rodajas)."),
        rx.text("- 2 dientes de ajo picados."),
        rx.text("- 1/2 taza de caldo de pescado."),
        rx.text("- Jugo de 1 limón."),
        rx.text("- 2 cucharadas de aceite de oliva."),
        rx.text("- Sal y pimienta al gusto."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar la salsa: En una sartén, calienta el aceite y sofríe la cebolla, el ajo y los tomates hasta que estén suaves."),
        rx.text("2. Agregar el caldo: Vierte el caldo de pescado, las aceitunas, las alcaparras y el jugo de limón. Cocina a fuego lento durante 10 minutos."),
        rx.text("3. Cocinar el pescado: Coloca los filetes de pescado en la sartén, cubre con la salsa y cocina durante 5-7 minutos por cada lado."),
        rx.text("4. Servir: Sirve el pescado con la salsa veracruzana sobre él y acompáñalo con arroz o ensalada."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>220 kcal</td></tr>
                            <tr><td>Proteínas</td><td>25 g</td></tr>
                            <tr><td>Carbohidratos</td><td>10 g</td></tr>
                            <tr><td>Grasas</td><td>12 g</td></tr>
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
        rx.text("✔️ Puedes acompañarlo con arroz o papas fritas."),
        rx.text("✔️ Si no tienes caldo de pescado, puedes usar caldo de pollo."),
        rx.text("✔️ Sirve con rodajas de aguacate y salsa picante."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa roja o verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz blanco o a la mexicana"),
        rx.text("🥗 Ensalada fresca"),

        rx.box(
            rx.image(
                src="/recetas/acom15.png",
                alt="Pescado a la Veracruzana",
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
                '<a href="/receta14" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta16" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta15() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Pescado a la Veracruzana",
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
