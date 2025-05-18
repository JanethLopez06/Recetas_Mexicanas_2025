import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/pollo.png",
            alt="Pollo en Salsa Verde",
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
        rx.text("El pollo en salsa verde es un platillo tradicional mexicano, ideal para acompañar con arroz o tortillas. Su sabor fresco y ligero lo hace perfecto para cualquier ocasión."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 4 piezas de pollo (piernas, muslos o pechugas)."),
        rx.text("- 4 tomates verdes (tomates de cáscara)."),
        rx.text("- 2 chiles serranos."),
        rx.text("- 1/4 de cebolla blanca."),
        rx.text("- 2 dientes de ajo."),
        rx.text("- 1/4 de taza de cilantro fresco."),
        rx.text("- 2 cucharadas de aceite de oliva."),
        rx.text("- Sal y pimienta al gusto."),
        rx.text("- 1 taza de caldo de pollo."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar la salsa: Hervir los tomates verdes, los chiles serranos, la cebolla y el ajo hasta que estén suaves. Licúa todo con el cilantro y un poco de caldo de pollo."),
        rx.text("2. Cocinar el pollo: En una sartén grande, calienta el aceite y fríe las piezas de pollo hasta que estén doradas por todos lados."),
        rx.text("3. Añadir la salsa: Vierte la salsa verde sobre el pollo, cubre con el resto del caldo de pollo y cocina a fuego lento durante 20 minutos."),
        rx.text("4. Servir: Sirve el pollo con la salsa verde, acompañándolo con arroz, frijoles o tortillas."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>300 kcal</td></tr>
                            <tr><td>Proteínas</td><td>35 g</td></tr>
                            <tr><td>Carbohidratos</td><td>12 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 15 minutos"),
        rx.text("🔥 Tiempo de cocción: 30 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes añadir un poco de crema al final para un toque cremoso."),
        rx.text("✔️ Si prefieres un toque más picante, agrega más chiles serranos."),
        rx.text("✔️ Acompáñalo con papas fritas o una ensalada fresca."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🍚 Arroz mexicano"),
        rx.text("🌮 Tacos de pollo"),
        rx.text("🥑 Guacamole"),
        rx.text("🍞 Tortillas de maíz"),

        rx.box(
            rx.image(
                src="/recetas/acom17.png",
                alt="Pollo en Salsa Verde",
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
                '<a href="/receta16" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta18" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta17() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Pollo en Salsa Verde",
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
