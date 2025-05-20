import reflex as rx

from my_app_web.Styles.styles import Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/guacamole.png",
            alt="Guacamole servido con totopos",
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
        rx.text("El guacamole es una salsa mexicana cremosa y fresca a base de aguacate, perfecta para acompañar tacos, totopos o como botana."),

        rx.heading("Ingredientes:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("- 2 aguacates maduros"),
        rx.text("- 1 tomate (jitomate) picado en cubos pequeños"),
        rx.text("- 1/4 de cebolla picada finamente"),
        rx.text("- 1 chile serrano (opcional)"),
        rx.text("- Jugo de 1 limón"),
        rx.text("- Sal al gusto"),
        rx.text("- Cilantro picado al gusto (opcional)"),

        rx.heading("Preparación:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Parte los aguacates, retira la semilla y extrae la pulpa."),
        rx.text(
            "2. Tritura el aguacate con un tenedor hasta obtener una textura cremosa."),
        rx.text("3. Añade el tomate, la cebolla, el chile, el jugo de limón y la sal."),
        rx.text("4. Mezcla todo suavemente y, si deseas, incorpora el cilantro."),
        rx.text("5. Sirve inmediatamente para evitar la oxidación."),

        rx.heading("Tabla nutricional:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>160 kcal</td></tr>
                            <tr><td>Proteínas</td><td>2 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 10 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Muy fácil"),

        rx.heading("Consejos de cocina:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa aguacates maduros pero firmes para mejor textura."),
        rx.text("✔️ Si no vas a servirlo de inmediato, cubre el guacamole con plástico directamente sobre la superficie para evitar que se oxide."),
        rx.text("✔️ Ajusta el picante al gusto."),

        rx.heading("Acompañamientos sugeridos:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("Sirve con totopos, tacos, carne asada o como aderezo junto a una bebida fresca como agua de limón o jamaica."),

        rx.box(
            rx.image(
                src="/recetas/acom1.png",
                alt="Guacamole con totopos y salsa",
                width="100%",
                max_width="300px",
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
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta2" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta1() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Guacamole Casero",
                font_size=Size.MED.value,
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
