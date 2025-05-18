import reflex as rx
from my_app_web.Styles.styles import Size, TextColor


def header_text(icon: str, text: str, color: str = None, font_size: str = "md") -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.heading(
            text,
            size="md",
            color=color
            ),
        spacing=Size.DEFAULT.value,
        padding_bottom=Size.BUTTON.value,
        align="center"
    )
