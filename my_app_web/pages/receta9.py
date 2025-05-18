import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/empanadas.png",
            alt="Empanadas de Queso o Picadillo",
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
        rx.text("Las empanadas son una delicia tradicional mexicana elaborada con masa de maíz o trigo, rellenas con queso derretido o picadillo de carne bien sazonado. Se fríen hasta quedar doradas y crujientes, siendo perfectas como antojito, cena ligera o acompañamiento."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 2 tazas de masa de maíz nixtamalizado"),
        rx.text("- 1/4 taza de agua"),
        rx.text("- 1 pizca de sal"),
        rx.text("- 1 taza de queso Oaxaca o queso fresco"),
        rx.text("- 200 g de carne molida (res o cerdo)"),
        rx.text("- 1/4 de cebolla picada"),
        rx.text("- 1 jitomate picado"),
        rx.text("- 1 diente de ajo picado"),
        rx.text("- Sal y pimienta al gusto"),
        rx.text("- Aceite vegetal para freír"),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Mezcla la masa con sal y agua hasta que esté suave y manejable."),
        rx.text("2. Para el picadillo: sofríe cebolla y ajo, añade carne, jitomate, sazona y cocina hasta que espese."),
        rx.text("3. Forma bolitas con la masa, aplánalas, coloca el relleno y sella los bordes."),
        rx.text("4. Fríe las empanadas en aceite caliente hasta que estén doradas."),
        rx.text("5. Escúrrelas sobre papel absorbente y sirve calientes."),

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
                            <tr><td>Proteínas</td><td>9 g</td></tr>
                            <tr><td>Carbohidratos</td><td>18 g</td></tr>
                            <tr><td>Grasas</td><td>13 g</td></tr>
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
        rx.text("🔥 Tiempo de cocción: 15 minutos"),
        rx.text("🍽️ Rinde para: 6 empanadas medianas"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa un poco de harina de trigo en la masa para más crocancia."),
        rx.text("✔️ Puedes hornearlas a 200°C por 25 minutos si prefieres evitar frituras."),
        rx.text("✔️ Sella bien los bordes para que no se salga el relleno."),
        rx.text("✔️ El picadillo se puede preparar con anticipación y refrigerar."),

        rx.heading("Acompañamientos sugeridos:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa verde o roja casera"),
        rx.text("🥗 Ensalada de repollo con zanahoria"),
        rx.text("🥑 Guacamole"),
        rx.text("🥤 Agua fresca de horchata o tamarindo"),

        rx.box(
            rx.image(
                src="/recetas/acom9.png",
                alt="Empanadas de Queso o Picadillo",
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
            rx.html('<a href="/receta8" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta10" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta9() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Empanadas de Queso o Picadillo",
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
