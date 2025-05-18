import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/gorditas.png",
            alt="Gorditas de Chicharrón",
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
        rx.text("Las gorditas de chicharrón son un platillo delicioso que consiste en tortillas rellenas de chicharrón prensado, acompañadas de salsa y crema."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 500 g de chicharrón prensado."),
        rx.text("- 1 kg de masa para tortillas."),
        rx.text("- 1/4 de cebolla picada finamente."),
        rx.text("- 2 dientes de ajo picados."),
        rx.text("- 1 chile serrano o jalapeño (opcional)."),
        rx.text("- Salsa roja o verde al gusto."),
        rx.text("- Crema al gusto."),
        rx.text("- Queso fresco desmoronado."),
        rx.text("- Sal al gusto."),
        rx.text("- Aceite para freír."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Preparar el chicharrón: En una sartén, calienta un poco de aceite y sofríe la cebolla, ajo y chile hasta que estén dorados."),
        rx.text("2. Agregar el chicharrón prensado: Incorpora el chicharrón y cocina por unos minutos. Agrega un poco de agua si es necesario para que no se seque."),
        rx.text("3. Formar las gorditas: Con la masa para tortillas, forma pequeñas bolitas y haz una hendidura en el centro, rellenando con la mezcla de chicharrón."),
        rx.text("4. Cocinar las gorditas: Cocina las gorditas en un comal caliente, dándoles vuelta hasta que estén bien cocidas y doradas por ambos lados."),
        rx.text("5. Servir: Abre las gorditas y rellénalas con salsa, crema, queso fresco y más chicharrón si lo deseas."),

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
                            <tr><td>Proteínas</td><td>15 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
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
        rx.text("🔥 Tiempo de cocción: 15 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes añadir nopales o papas fritas dentro del relleno."),
        rx.text("✔️ Asegúrate de que el chicharrón no quede demasiado seco."),
        rx.text("✔️ Si prefieres un toque más crujiente, puedes freír las gorditas en lugar de cocinarlas en comal."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa roja o verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz mexicano"),
        rx.text("🥗 Ensalada fresca"),

        rx.box(
            rx.image(
                src="/recetas/acom12.png",
                alt="Gorditas de Chicharrón",
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


def receta12() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Gorditas de Chicharrón",
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






















































