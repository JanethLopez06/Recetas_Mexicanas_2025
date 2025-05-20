import reflex as rx
from my_app_web.Styles.styles import  Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/tampiquena.png",
            alt="Tampiqueña",
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
        rx.text("La tampiqueña es un platillo tradicional de la región de Tampico, Tamaulipas. Se compone de carne asada acompañada de una enchilada, frijoles, arroz y guacamole."),

        rx.heading("Ingredientes:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("- 500 g de arrachera o carne para asar."),
        rx.text("- 2 enchiladas rojas."),
        rx.text("- 1/2 taza de frijoles refritos."),
        rx.text("- 1/4 de taza de arroz."),
        rx.text("- 1 aguacate."),
        rx.text("- 1/4 de taza de cebolla morada picada."),
        rx.text("- 1 chile serrano."),
        rx.text("- Jugo de 1 limón."),
        rx.text("- Sal y pimienta al gusto."),

        rx.heading("Preparación:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("1. Marinar la carne: Sazona la carne con sal, pimienta y jugo de limón."),
        rx.text("2. Asar la carne: Cocina la carne en una parrilla caliente por 4-5 minutos de cada lado."),
        rx.text("3. Preparar las enchiladas: Fría las enchiladas y acompáñalas con frijoles y arroz."),
        rx.text("4. Hacer el guacamole: Machaca el aguacate con cebolla, chile serrano y jugo de limón."),
        rx.text("5. Servir: Sirve la carne junto con las enchiladas, frijoles, arroz y guacamole."),

        rx.heading("Tabla nutricional", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>450 kcal</td></tr>
                            <tr><td>Proteínas</td><td>32 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
                            <tr><td>Grasas</td><td>22 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 15 minutos"),
        rx.text("🔥 Tiempo de cocción: 20 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Si prefieres carne más jugosa, puedes usar filete de res."),
        rx.text("✔️ Las enchiladas pueden ser de pollo o carne al gusto."),
        rx.text("✔️ Sirve con arroz y frijoles para un platillo completo."),

        rx.heading("Acompañamientos sugeridos:", margin_top="4em", font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz blanco"),
        rx.text("🥗 Ensalada de nopales"),

        rx.box(
            rx.image(
                src="/recetas/acom14.png",
                alt="Tampiqueña",
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
                '<a href="/receta13" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta15" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta14() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Tampiqueña",
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
