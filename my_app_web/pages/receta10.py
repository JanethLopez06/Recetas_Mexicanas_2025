# my_app_web/pages/receta10.py

import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/pambazo.png",
            alt="Pambazos",
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
        rx.text("Los pambazos son un antojito mexicano típico, preparado con un pan suave bañado en salsa de chile guajillo, relleno con papas y chorizo, y frito ligeramente para darles una textura crujiente por fuera y suave por dentro. Se acompañan con lechuga, crema, queso y salsa."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 4 panes para pambazo (o teleras suaves)"),
        rx.text("- 3 papas medianas, cocidas y en cubos"),
        rx.text("- 200 g de chorizo"),
        rx.text("- 4 chiles guajillo (sin semillas)"),
        rx.text("- 1 diente de ajo"),
        rx.text("- 1/4 de cebolla"),
        rx.text("- Sal al gusto"),
        rx.text("- Aceite vegetal para freír"),
        rx.text("- Lechuga picada, crema, queso rallado y salsa al gusto para acompañar"),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Licúa los chiles guajillo con ajo, cebolla, un poco de agua y sal hasta formar una salsa."),
        rx.text("2. Cocina el chorizo, añade las papas y sofríe todo junto hasta integrar bien."),
        rx.text("3. Corta los panes a la mitad sin separarlos completamente."),
        rx.text("4. Sumerge cada pan en la salsa y fríe en una sartén con un poco de aceite por ambos lados."),
        rx.text("5. Rellena con la mezcla de papa y chorizo."),
        rx.text("6. Decora con lechuga, crema, queso y salsa al gusto."),

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
                            <tr><td>Proteínas</td><td>12 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 30 minutos"),
        rx.text("🔥 Tiempo de cocción: 20 minutos"),
        rx.text("🍽️ Rinde para: 4 pambazos"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes usar pan de telera si no encuentras pan de pambazo."),
        rx.text("✔️ Si no deseas freír, puedes calentar los pambazos en sartén sin aceite."),
        rx.text("✔️ Agrega un poco de chipotle a la salsa si prefieres un toque más picante."),
        rx.text("✔️ También se pueden rellenar con frijoles y queso para una opción vegetariana."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🥤 Agua de tamarindo o jamaica"),
        rx.text("🌶️ Salsa roja casera"),
        rx.text("🥗 Ensalada fresca de nopales"),

        rx.box(
            rx.image(
                src="/recetas/acom10.png",
                alt="Pambazos",
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
            rx.html('<a href="/receta9" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta11" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta10() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Pambazos",
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
