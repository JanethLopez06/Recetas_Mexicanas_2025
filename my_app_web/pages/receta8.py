import reflex as rx

from my_app_web.Styles.styles import  Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/tinga.png",
            alt="Tostadas de Tinga",
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
        rx.text("Las tostadas de tinga son un platillo tradicional mexicano hecho con pollo desmenuzado cocido en una salsa de jitomate con chipotle y cebolla. Se sirven sobre tostadas crujientes y se decoran con crema, lechuga, queso y otros ingredientes frescos."),

        rx.heading("Ingredientes:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("- 2 pechugas de pollo cocidas y desmenuzadas."),
        rx.text("- 3 jitomates grandes."),
        rx.text("- 1/2 cebolla blanca (en rebanadas finas)."),
        rx.text("- 2 chiles chipotles en adobo (ajustar al gusto)."),
        rx.text("- 1 diente de ajo."),
        rx.text("- 1/4 de taza de caldo de pollo."),
        rx.text("- Aceite vegetal."),
        rx.text("- Sal al gusto."),
        rx.text("- Tostadas de maíz."),
        rx.text("- Crema al gusto."),
        rx.text("- Queso fresco desmoronado."),
        rx.text("- Lechuga finamente picada."),
        rx.text("- Rodajas de aguacate (opcional)."),




        rx.heading("Preparación:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Cocinar la salsa: Licúa los jitomates, chipotles, ajo y el caldo de pollo hasta obtener una salsa homogénea."),
        rx.text("2. Saltear la cebolla: En una sartén grande, calienta un poco de aceite y sofríe la cebolla hasta que esté transparente."),
        rx.text(
            "3. Agregar la salsa: Vierte la salsa en la sartén con la cebolla y cocina durante 5-7 minutos."),
        rx.text("4. Incorporar el pollo: Añade el pollo desmenuzado, mezcla bien y cocina por 10 minutos más a fuego medio. Ajusta de sal."),
        rx.text("5. Montar las tostadas: Coloca una porción de tinga sobre cada tostada y decora con crema, queso, lechuga y aguacate si deseas."),


        rx.heading("Tabla nutricional", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>250 kcal</td></tr>
                            <tr><td>Proteínas</td><td>20 g</td></tr>
                            <tr><td>Carbohidratos</td><td>15 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 20 minutos"),
        rx.text("🔥 Tiempo de cocción: 15 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones (8 tostadas aprox.)"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes usar muslos de pollo si prefieres más sabor."),
        rx.text("✔️ Si la salsa está muy espesa, añade un poco más de caldo."),
        rx.text(
            "✔️ Las tostadas se pueden calentar ligeramente en el comal antes de montar."),
        rx.text(
            "✔️ Si no te gusta el picante, usa solo un chile chipotle o retíralo por completo."),



        rx.heading("Acompañamientos sugeridos:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa roja o verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz a la mexicana"),
        rx.text("🥗 Ensalada fresca de nopales"),
        rx.text("🥤 Agua fresca de limón o jamaica"),



        rx.box(
            rx.image(
                src="/recetas/acom8.png",
                alt="Tostadas de Tinga",
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
                '<a href="/receta7" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta9" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta8() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Tostadas de Tinga",
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
