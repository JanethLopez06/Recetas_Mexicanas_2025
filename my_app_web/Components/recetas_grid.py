import reflex as rx
from my_app_web.Styles.styles import Size, Color


def recetas_grid(index: int) -> rx.Component:
    categorias_colores = [
        Color.ENTRADA.value,
        Color.ANTOJITOS.value,
        Color.P_FUERTES.value,
        Color.POSTRES.value,
    ]

    categoria_index = index // 6

    recetas_nombres = [
        "Guacamole", "Tacos Dorados", "Sopes", "Pozole", "Chiles Rellenos", "Arroz",
        "Quesadillas", "Tostadas de Tinga", "Empanadas", "Pambazos", "Enchiladas", "Gorditas",
        "Chiles en Nogada", "Carne Asada", "Tampiqueña", "Pescado", "Birria", "Pollo Verde",
        "Arroz con Leche", "Gelatina", "Plátanos", "Flan", "Buñuelos", "Paletas"
    ]

    receta_nombre = recetas_nombres[index]
    color_fondo = categorias_colores[categoria_index]

    return rx.box(
        rx.link(
            rx.box(
                rx.image(
                    src=f"/recetas/{index+1}.png",
                    alt=receta_nombre,
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    border_radius=Size.VERY_BIG.value,
                ),
                rx.box(
                    rx.text(
                        receta_nombre,
                        font_family="'Press Start 2P', cursive",
                        font_size="0.5em",
                        color="white",
                        text_align="center",
                        px="4px",
                    ),
                    position="absolute",
                    bottom="0",
                    width="100%",
                    bg="rgba(0, 0, 0, 0.7)",
                    padding="4px",
                    # No se muestra en SSR (mobile), sí en cliente
                    display=["none", "block"],
                ),
                position="relative",
                width="100%",
                height="100%",
            ),
            href=f"/receta{index+1}",
            width="100%",
            height="100%",
        ),
        bg=color_fondo,
        aspect_ratio="1",
        width="15em",
        max_width="100%",
        border_radius=Size.VERY_BIG.value,
        overflow="hidden",
        box_shadow="0 1px 4px rgba(0,0,0,0.15)",
        padding="10px",
        display="flex",
        justify_content="center",
        align_items="center",
        flex_direction="column",
        _hover={
            "children[0]": {
                "children[1]": {
                    "display": "block"
                }
            }
        }
    )
