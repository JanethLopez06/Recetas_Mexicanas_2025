import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/enchiladas.png",
            alt="Enchiladas Verdes",
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
        rx.text("Las enchiladas verdes son un platillo tradicional mexicano preparado con tortillas de maíz rellenas (generalmente de pollo), bañadas en salsa verde hecha con tomatillo y chile, y gratinadas con queso. Se sirven calientes y decoradas con crema, cebolla y cilantro."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 12 tortillas de maíz"),
        rx.text("- 2 pechugas de pollo cocidas y desmenuzadas"),
        rx.text("- 500 g de tomatillo (verde)"),
        rx.text("- 2 chiles serranos o jalapeños (ajustar al gusto)"),
        rx.text("- 1/4 de cebolla"),
        rx.text("- 1 diente de ajo"),
        rx.text("- Cilantro fresco al gusto"),
        rx.text("- 1/4 taza de crema ácida"),
        rx.text("- Queso rallado (queso fresco o manchego)"),
        rx.text("- Aceite vegetal"),
        rx.text("- Sal al gusto"),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Cocina los tomatillos, chiles, ajo y cebolla en agua hasta que estén suaves."),
        rx.text("2. Licúa con cilantro, sal y un poco del agua de cocción hasta obtener una salsa verde homogénea."),
        rx.text("3. Fríe ligeramente las tortillas en aceite caliente para suavizarlas."),
        rx.text("4. Rellena cada tortilla con pollo desmenuzado, enróllalas y colócalas en un refractario."),
        rx.text("5. Baña con la salsa verde caliente y espolvorea el queso encima."),
        rx.text("6. Hornea o gratina por 10 minutos o hasta que el queso se derrita."),
        rx.text("7. Sirve con crema, cebolla y cilantro por encima."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>320 kcal</td></tr>
                            <tr><td>Proteínas</td><td>18 g</td></tr>
                            <tr><td>Carbohidratos</td><td>22 g</td></tr>
                            <tr><td>Grasas</td><td>18 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 25 minutos"),
        rx.text("🔥 Tiempo de cocción: 20 minutos"),
        rx.text("🍽️ Rinde para: 4 personas"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes usar muslos de pollo si prefieres más sabor."),
        rx.text("✔️ Para una versión más ligera, evita freír las tortillas."),
        rx.text("✔️ Si quieres más cremosidad, añade un poco de crema a la salsa al licuar."),
        rx.text("✔️ Acompáñalas con arroz o frijoles refritos."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🍚 Arroz rojo o blanco"),
        rx.text("🥑 Guacamole o aguacate en rodajas"),
        rx.text("🥗 Ensalada fresca de lechuga"),
        rx.text("🥤 Agua de horchata o tamarindo"),

        rx.box(
            rx.image(
                src="/recetas/acom11.png",
                alt="Enchiladas Verdes",
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
            rx.html('<a href="/receta10" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta12" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta11() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Enchiladas Verdes",
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
