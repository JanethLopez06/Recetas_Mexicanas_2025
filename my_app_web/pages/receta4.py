import reflex as rx

from my_app_web.Styles.styles import  Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/pozole.png",
            alt="Pozole",
            width="100%",
            max_width="200px",
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
        rx.text("Un platillo tradicional mexicano hecho con maíz cacahuazintle, carne de cerdo o pollo, y un caldo rojo condimentado con chiles. Se sirve con una variedad de acompañamientos frescos y crujientes."),

        rx.heading("Ingredientes:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("- 500 g de maíz pozolero precocido."),
        rx.text("- 500 g de carne de cerdo (espaldilla, pierna o costilla)."),
        rx.text("- 1/2 cebolla."),
        rx.text("- 2 dientes de ajo. "),
        rx.text("- 3 chiles guajillo. "),
        rx.text("- Sal al gusto."),
        rx.text("- Agua suficiente."),


        rx.heading("Preparación:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("1. Cocina el maíz pozolero en una olla grande con agua hasta que reviente (aprox. 1 hora si es precocido)."),
        rx.text(
            "2. En otra olla, cocina la carne con ajo, cebolla y sal hasta que esté suave. Deshebra si lo prefieres."),
        rx.text(
            "3. Asa y remoja los chiles en agua caliente por 10 min. Luego licúa con ajo, cebolla y un poco de agua. Cuela la salsa."),
        rx.text("4. Añade la carne cocida y la salsa colada al maíz. Cocina todo junto por 30–40 minutos a fuego medio. Ajusta la sal."),
        rx.text(
            "5. Sirve caliente y acompaña con los ingredientes frescos al gusto."),
    

        rx.heading("Tabla nutricional (aproximado por porción):", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class="nes-table-responsive" style="margin-top:1em;">
                    <table class="nes-table is-bordered is-centered">
                        <thead>
                            <tr><th>Nutriente</th><th>Cantidad</th></tr>
                        </thead>
                        <tbody>
                            <tr><td>Calorías</td><td>360 kcal</td></tr>
                            <tr><td>Proteínas</td><td>20 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
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

        rx.heading("Información adicional:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("⏱️ Tiempo de preparación: 30 minutos"),
        rx.text("🔥 Tiempo de cocción: 1.5 a 2 horas"),
        rx.text("🍽️ Rinde para: 6 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="2em",font_size=Size.DEFAULT.value),
        rx.text("✔️ Usa maíz pozolero natural si quieres un sabor más auténtico (requiere remojar una noche antes)."),
        rx.text("✔️ Puedes sustituir el cerdo por pollo para una versión más ligera."),
        rx.text("✔️ No olvides espumar el caldo para que quede más claro y limpio."),
        rx.text("✔️ La salsa puede hacerse más o menos picante según los chiles que uses."),

        rx.heading("Acompañamientos sugeridos:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("🥬 Lechuga o repollo finamente picado."),
        rx.text("🔴 Rábanos en rodajas."),
        rx.text("🧅 Cebolla picada."),
        rx.text("🍋 Limones en mitades."),
        rx.text("🧂 Orégano seco."),
        rx.text("🟡 Tostadas o tortillas."),
        rx.text("🔥 Salsa picante."),



        rx.box(
            rx.image(
                src="/recetas/acom4.png",
                alt="Pozole",
                width="100%",
                max_width="200px",
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
                '<a href="/receta3" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta5" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta4() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Pozole Rojo Mexicano",
                font_size=Size.MED.value,
                text_align="center",
                margin_top="1em",
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
            padding_y="2",
            padding_x="1em",
            spacing="8",
            max_width="1200px",
            width="100%"
        )
    )
