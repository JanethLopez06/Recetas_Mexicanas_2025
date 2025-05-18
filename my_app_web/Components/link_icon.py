import reflex as rx

def link_icon(icon:str, url: str) -> rx.Component:

    return rx.link(
        rx.box(class_name=f"nes-icon {icon} is-large"),
        class_name="icon-link",
        href=url,
        is_external=True
    )

