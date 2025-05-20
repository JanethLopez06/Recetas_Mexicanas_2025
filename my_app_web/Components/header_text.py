import reflex as rx
from my_app_web.Styles.styles import HeadingSize,Size


def header_text(icon, text, color=None, font_size=HeadingSize.HUGE):
    return rx.hstack(
        rx.box(class_name=f"nes-icon is-medium {icon}"),
        rx.heading(text, size=font_size, color=color),
        spacing="2",  # Espacio entre el icono y el título
        align="center",
        margin_top=Size.BIG.value
    )
