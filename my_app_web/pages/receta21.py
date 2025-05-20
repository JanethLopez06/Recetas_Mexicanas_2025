import reflex as rx
from my_app_web.Styles.styles import  Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/platanos.png",
            alt="Plátanos Fritos",
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
        rx.text("Los plátanos fritos son un postre o acompañamiento tradicional, crujientes por fuera y suaves por dentro, perfectos para cualquier comida."),

        rx.heading("Ingredientes:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("- 4 plátanos maduros."),
        rx.text("- Aceite vegetal para freír."),
        rx.text("- Canela en polvo (opcional)."),
        rx.text("- Azúcar al gusto (opcional)."),

        rx.heading("Preparación:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("1. Pelar los plátanos y cortarlos en rodajas sesgadas o longitudinales."),
        rx.text("2. Calentar el aceite en una sartén a fuego medio-alto."),
        rx.text("3. Freír los plátanos hasta que estén dorados por ambos lados."),
        rx.text("4. Retirar del aceite y escurrir en papel absorbente. Espolvorear con canela y azúcar si se desea."),

        rx.heading("Tabla nutricional", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>200 kcal</td></tr>
                            <tr><td>Proteínas</td><td>1 g</td></tr>
                            <tr><td>Carbohidratos</td><td>35 g</td></tr>
                            <tr><td>Grasas</td><td>7 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 10 minutos"),
        rx.text("🔥 Tiempo de cocción: 10 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Muy fácil"),

        rx.heading("Consejos de cocina:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa plátanos bien maduros para un sabor más dulce."),
        rx.text("✔️ Puedes acompañarlos con crema o queso rallado si los sirves como desayuno."),
        rx.text("✔️ También puedes hornearlos si prefieres una versión más ligera."),



        rx.hstack(
            rx.html('<a href="/receta20" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta22" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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

def receta21() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Plátanos Fritos",
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
