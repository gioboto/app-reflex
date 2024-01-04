import reflex as rx
import link_bio.styles.styles as style
from link_bio.styles.styles import Spacer as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(title, 
                font_weight="bold", 
                color=Color.PRIMARY.value
            ),
        f"{body}", 
        font_size=Size.MEDIUM.value,
        color= TextColor.BODY.value
    )
    