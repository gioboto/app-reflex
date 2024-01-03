import reflex as  rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"link del footer  con {datetime.date.today().year}",
        href="http://fehu.me",
        is_external=True),
        rx.text("El are del footer................................................"),
        bg="ligthgray",
    )