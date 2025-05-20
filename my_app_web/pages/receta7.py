import reflex as rx

from my_app_web.Styles.styles import  Size, FLEX_DIRECTION


def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/quesadillas.png",
            alt="Quesadillas Fritas",
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
        rx.text("Las quesadillas fritas son una deliciosa botana mexicana, hechas con tortillas de maíz rellenas de queso y otros ingredientes, que se fríen hasta dorarse y quedar crujientes. Son perfectas para acompañar con salsa y crema."),

        rx.heading("Ingredientes:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("- 10 tortillas de maíz."),
        rx.text("- 250 g de queso Oaxaca (o cualquier queso rallado de tu preferencia)."),
        rx.text("- 1/2 taza de frijoles refritos (opcional)."),
        rx.text("- Aceite para freír."),
        rx.text("- Salsa al gusto (verde, roja o de tu preferencia)."),
        rx.text("- Crema al gusto."),
        rx.text("- Sal al gusto."),



        rx.heading("Preparación:", margin_top="4em",font_size=Size.DEFAULT.value),
        rx.text("1. Preparar las tortillas: Calienta las tortillas ligeramente en un comal o sartén, solo para que se suavicen un poco y sean fáciles de doblar."),
        rx.text("2. Rellenar las quesadillas: Coloca una pequeña cantidad de queso en el centro de cada tortilla. Si deseas, agrega frijoles refritos antes de agregar el queso."),
        rx.text("3. Cerrar las quesadillas: Doble las tortillas por la mitad, formando una media luna, asegurándote de que el queso quede bien cubierto."),
        rx.text("4. Freír: En una sartén grande, calienta suficiente aceite a fuego medio-alto. Fría las quesadillas por ambos lados hasta que estén doradas y crujientes, aproximadamente 2-3 minutos por lado."),
        rx.text("5. Escurrir: Coloca las quesadillas sobre papel absorbente para eliminar el exceso de aceite."),
        rx.text("6. Servir: Sirve las quesadillas calientes, acompañadas de salsa, crema y, si lo deseas, un poco de guacamole."),


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
                            <tr><td>Calorías</td><td>200 kcal</td></tr>
                            <tr><td>Proteínas</td><td>7 g</td></tr>
                            <tr><td>Carbohidratos</td><td>20 g</td></tr>
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
        rx.text("⏱️ Tiempo de preparación: 15 minutos"),
        rx.text("🔥 Tiempo de cocción: 10 minutos"),
        rx.text("🍽️ Rinde para: 4 porciones"),
        rx.text("⭐ Dificultad: Fácil"),

        rx.heading("Consejos de cocina:", margin_top="2em",
                   font_size=Size.DEFAULT.value),
       rx.text("✔️ Usa queso fresco para un mejor sabor y textura."),
       rx.text("✔️ Si prefieres una opción más saludable, puedes hornear las quesadillas en lugar de freírlas."),
       rx.text("✔️ No sobrecargues las quesadillas de queso, ya que puede dificultar el cierre de la tortilla."),
       rx.text("✔️ Asegúrate de que el aceite esté lo suficientemente caliente para que las quesadillas queden crujientes, pero sin quemarse."),



        rx.heading("Acompañamientos sugeridos:", margin_top="4em",
                   font_size=Size.DEFAULT.value),
        rx.text("🌶️ Salsa roja o verde"),
        rx.text("🥑 Guacamole"),
        rx.text("🍚 Arroz a la mexicana"),
        rx.text("🥗 Ensalada fresca de nopales"),
        rx.text("🥤 Agua fresca de limón o jamaica"),



        rx.box(
            rx.image(
                src="/recetas/acom7.png",
                alt="Quesadillas Fritas",
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
                '<a href="/receta6" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html(
                '<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html(
                '<a href="/receta8" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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


def receta7() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Quesadillas Fritas",
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
