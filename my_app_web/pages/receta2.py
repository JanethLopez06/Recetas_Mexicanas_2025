import reflex as rx
from my_app_web.Styles.styles import  Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/tacos.png",
            alt="Tacos",
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
        rx.text("Crujientes tacos de tortilla rellenos con un suave puré de papa sazonado, fritos hasta dorar y acompañados de lechuga, crema, queso y salsa. Una receta económica, deliciosa y muy popular en la cocina mexicana."),

        rx.heading("Ingredientes:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("- 4 papas medianas peladas"),
        rx.text("- 12 tortillas de maíz"),
        rx.text("- 1/4 de cebolla picada finamente"),
        rx.text("- Aceite vegetal para freír"),
        rx.text("- Lechuga pocada (para servir)"),
        rx.text("- Sal al gusto"),
        rx.text("- Crema, queso fresco rallado y salsa al gusto"),

        rx.heading("Preparación:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("1. Hierve las papas hasta que estén suaves."),
        rx.text("2. Escúrrelas y aplástalas con un tenedor; añade cebolla picada y sal al gusto."),
        rx.text("3. Calienta ligeramente las tortillas para que se doblen sin romperse."),
        rx.text("4. Coloca una porción de papa en cada tortilla, dóblalas y sujétalas con un palillo si es necesario."),
        rx.text("5. Fríe los tacos en aceite caliente hasta que estén dorados y crujientes."),
        rx.text("6. Escúrrelos en papel absorbente y sirve con lechuga, crema, queso y salsa. "),

        rx.heading("Tabla nutricional (por porción -3 tacos):", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>350 kcal</td></tr>
                            <tr><td>Proteínas</td><td>8 g</td></tr>
                            <tr><td>Carbohidratos</td><td>38 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 25 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa tortillas del día anterior para evitar que se rompan al doblarlas."),
        rx.text("✔️ Si prefieres una opción más saludable, puedes hornearlos en lugar de freírlos."),
        rx.text("✔️ Añade un poco de ajo en polvo o pimienta al puré para más sabor."),

        rx.heading("Acompañamientos sugeridos:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text(" Agua de horchata o jamaica bien fría"),
        rx.text("Arroz rojo mexicano"),
        rx.text("Salsa verde casera"),

        rx.box(
            rx.image(
                src="/recetas/acom2.png",
                alt="Tacos dorados",
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
                '<a href="/receta1" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta3" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta2() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Tacos Dorados de Papa",
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
