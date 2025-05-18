import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import TextColor, Size, FLEX_DIRECTION

def imagen_box():
    return rx.box(
        rx.image(
            src="/recetas/bunuelos.png",
            alt="Buñuelos",
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
        rx.text("Los buñuelos son un postre tradicional crujiente y espolvoreado con azúcar y canela, muy popular en celebraciones navideñas en México."),

        rx.heading("Ingredientes:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("- 2 tazas de harina de trigo."),
        rx.text("- 1 huevo."),
        rx.text("- 1/4 taza de mantequilla derretida."),
        rx.text("- 1/2 taza de agua tibia."),
        rx.text("- 1 pizca de sal."),
        rx.text("- Aceite para freír."),
        rx.text("- Azúcar y canela para espolvorear."),

        rx.heading("Preparación:", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.text("1. Mezclar la harina, sal, huevo, mantequilla y agua hasta formar una masa suave."),
        rx.text("2. Amasar y dejar reposar la masa tapada por 30 minutos."),
        rx.text("3. Dividir la masa en porciones, extender en forma de discos delgados."),
        rx.text("4. Freír los discos en aceite caliente hasta que estén dorados y crujientes."),
        rx.text("5. Escurrir en papel absorbente y espolvorear con azúcar y canela."),

        rx.heading("Tabla nutricional", margin_top="2em", font_size=Size.DEFAULT.value),
        rx.box(
            rx.html("""
                <div class=\"nes-table-responsive\" style=\"margin-top:1em;\">
                    <table class=\"nes-table is-bordered is-centered\">
                        <thead><tr><th>Nutriente</th><th>Cantidad</th></tr></thead>
                        <tbody>
                            <tr><td>Calorías</td><td>210 kcal</td></tr>
                            <tr><td>Proteínas</td><td>4 g</td></tr>
                            <tr><td>Carbohidratos</td><td>30 g</td></tr>
                            <tr><td>Grasas</td><td>10 g</td></tr>
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
        rx.text("🔥 Tiempo de cocción: 10 minutos"),
        rx.text("🍽️ Rinde para: 6 porciones"),
        rx.text("⭐ Dificultad: Media"),

        rx.heading("Consejos de cocina:", margin_top="1.5em", font_size=Size.DEFAULT.value),
        rx.text("✔️ Puedes agregar ralladura de naranja a la masa para un toque especial."),
        rx.text("✔️ Asegúrate de que el aceite esté bien caliente antes de freír."),
        rx.text("✔️ Espolvorea el azúcar y canela mientras los buñuelos estén calientes para que se adhiera mejor."),

    

        rx.hstack(
            rx.html('<a href="/receta22" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Anterior Receta</a>'),
            rx.html('<a href="/" class="nes-btn is-success" style="padding: 1em 2em;">Menú Principal</a>'),
            rx.html('<a href="/receta24" class="nes-btn is-primary" style="margin-left: 1em; padding: 1em 2em;">Siguiente Receta</a>'),
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

def receta23() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Buñuelos",
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
