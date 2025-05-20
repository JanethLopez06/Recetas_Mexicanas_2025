# """Welcome to Reflex! This file outlines the steps to create a basic app."""

# import reflex as rx
# import my_app_web.Styles.styles as styles
# from my_app_web.Styles.styles import Size
# from my_app_web.Views.navbar import navbar
# from my_app_web.Views.header import header
# from my_app_web.Views.instructions import instructions
# from my_app_web.Views.partners import partners
# from my_app_web.Views.author import author
# from my_app_web.Views.footer import footer
# from my_app_web.Components.kitchen import kitchen
# from my_app_web.Views.recetas import recetas

# title = "Recetas de Cocina Mexicana 2025"


# def index() -> rx.Component:
#     return rx.box(  # Como un div
#         rx.html('<script src="/js/emojiRain.js"></script>'),
#         navbar(),
#         rx.center(
#             rx.vstack(
#                 header(),
#                 instructions(),
#                 recetas(),
#                 author(),
#                 partners(),
#                 footer(),
#                 kitchen(),

#                 width="100%",
#                 spacing=Size.VERY_BIG.value
#             )

#         )
#     ),


# # Página Estática
# app = rx.App(
#     stylesheets=styles.STYLESHEETS,
#     style=styles.BASE_STYLE,
# )
# app.add_page(
#     index,
#     title="Recetas Mexicanas",
#     description="¡Descubre, aprende y saborea algo nuevo cada día!"
# )

# app.py (o donde configures tu server)
from my_app_web.Styles.styles import Size, Color
import reflex as rx
import my_app_web.Styles.styles as styles
from my_app_web.Styles.styles import Size
from my_app_web.Views.navbar import navbar
from my_app_web.Views.header import header
from my_app_web.Views.instructions import instructions
from my_app_web.Views.partners import partners
from my_app_web.Views.author import author
from my_app_web.Views.footer import footer
from my_app_web.Components.kitchen import kitchen
from my_app_web.Views.recetas import recetas

# Importación automática de las 24 páginas de recetas


def import_recetas():
    from importlib import import_module
    return [
        (f"receta{i}", import_module(
            f"my_app_web.pages.receta{i}").__getattribute__(f"receta{i}"))
        for i in range(1, 25)
    ]


def index() -> rx.Component:
    # <– Esto debería aparecer en la consola del servidor
    print("Cargando index()")

    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.html('<script src="/js/emojiRain.js"></script>'),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                recetas(),
                author(),
                partners(),
                footer(),
                kitchen(),
                width="100%",
                spacing="4"
            )
        )
    )


# Página Estática
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

# Página principal
app.add_page(
    index,
    title="Recetas Mexicanas",
    description="¡Descubre, aprende y saborea algo nuevo cada día!"
)

# Agregar las 24 páginas de recetas
for nombre, funcion in import_recetas():
    app.add_page(
        funcion,
        route=f"/{nombre}",
        title=f"Receta {nombre[-1]}",
        description=f"Preparación de la receta {nombre}"
    )


# components/recetas_grid.py


def recetas_grid(index: int) -> rx.Component:
    """
    Componente de grid para recetas.
    index: número de receta (1-24)
    """
    return rx.box(
        rx.link(
            rx.image(
                src=f"/assets/recetas/{index}.png",
                alt=f"Receta {index}",
                width="100%",
                height="100%",
                object_fit="cover"
            ),
            href=f"/receta{index}",  # Debe existir la ruta en app.py
            is_external=False,
            display="block",
            width="100%",
            height="100%"
        ),
        bg=Color.SECONDARY.value,
        aspect_ratio="1",
        width="6em",  # Ajustable al gusto
        max_width="100%",
        border_radius=Size.SMALL.value,
        overflow="hidden",
        box_shadow="0 1px 4px rgba(0,0,0,0.15)"
    )
