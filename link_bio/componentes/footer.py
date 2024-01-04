import reflex as  rx
import datetime
from link_bio.styles.styles import Spacer as Size
from link_bio.styles.styles import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"link del footer  con {datetime.date.today().year}",
            href="http://fehu.me",
            is_external=True
        ),
        rx.text(
            "El are del footer................................................",
            font_size=Size.MEDIUM.value,
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )