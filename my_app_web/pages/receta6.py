import reflex as rx

import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/arrozm.png",
            alt="Arroz a la Mexicana",
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
        rx.text("Clásico arroz rojo preparado con jitomate, ajo y cebolla, ideal como guarnición para platillos mexicanos."),

        rx.heading("Ingredientes:", margin_top="2em",font_size=Size.DEFAULT.value),
        rx.text("- 1 taza de arroz blanco."),
        rx.text("- 2 jitomates maduros"),
        rx.text("- 1/4 de cebolla."),
        rx.text("- 1 diente de ajo. "),
        rx.text("- 2 tazas de caldo de pollo o agua."),
        rx.text("- 2 cucharadas de aceite."),
        rx.text("- 1/2 taza de zanahoria y chícharos (opcional)."),
        rx.text("- Sal al gusto."),


        rx.heading("Preparación:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("1. Enjuaga el arroz bajo agua fría hasta que salga clara."),
        rx.text(
            "2. Licúa los jitomates, cebolla y ajo."),
        rx.text("3. En una olla, calienta aceite y sofríe el arroz hasta que esté dorado."),
        rx.text("4. Agrega el puré de jitomate colado y cocina 3 minutos."),
        rx.text("5. Vierte el caldo caliente y añade sal."),
        rx.text("6. Incorpora las verduras si las usas."),
        rx.text("7. Tapa y cocina a fuego bajo hasta que el líquido se absorba (~ 15-20 min)."),
    


        rx.heading("Tabla nutricional", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>210 kcal</td></tr>
                            <tr><td>Proteínas</td><td>4 g</td></tr>
                            <tr><td>Carbohidratos</td><td>35 g</td></tr>
                            <tr><td>Grasas</td><td>6 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 10 minutos"),
        rx.text("🔥 Tiempo de cocción: 20 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="1.5em",
                   font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa caldo de pollo para más sabor."),
        rx.text(
            "✔️ No muevas el arroz mientras se cocina."),
        rx.text("✔️ Si prefieres, agrégale elote o pimiento en cubos."),


        rx.heading("Acompañamientos sugeridos:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
        rx.text("🌶️ Chiles rellenos."),
        rx.text("🍗 Pollo en mole."),
        rx.text("🥤 Agua fresca de jamaica."),



        rx.box(
            rx.image(
                src="/recetas/acom6.png",
                alt="Arroz",
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
                '<a href="/receta5" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta7" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta6() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Arroz a la Mexicana",
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
