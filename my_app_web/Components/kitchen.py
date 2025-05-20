import reflex as rx
import my_app_web.constants as constants
from my_app_web.Styles.styles import Size


def kitchen() -> rx.Component:
    return rx.center(
        rx.link(
            rx.vstack(
                rx.box(
                    rx.el.span("Proyecto "),
                    rx.el.span("en GitHub"),
                    class_name="nes-balloon from-right",
                    margin_bottom=Size.BIG.value,
                    margin_top=Size.VERY_BIG.value
                ),
                rx.el.span(
                    rx.el.span(constants.VERSION, class_name="is-error"),
                    class_name="nes-badge",
                    style={"fontSize": Size.MEDIUM.value},  # Cambio aquí
                ),
            ),
            rx.box(
                class_name="nes-octocat animate"
            ),
            href=constants.GITHUB_REPO_URL,
            is_external=True,
            align_items="end",
            display="flex",
            margin_top=Size.ZERO.value
        ),
        width="100%"
    )
