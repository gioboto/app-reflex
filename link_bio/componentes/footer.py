import reflex as  rx
import datetime
from link_bio.styles.styles import Spacer as Size
from link_bio.styles.styles import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="rune_tattoo_design__fehu_by_canislunaris_dfe7fnd-fullview.jpg",
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="logo de la web"),
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
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )