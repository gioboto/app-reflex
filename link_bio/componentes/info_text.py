import reflex as rx
import link_bio.styles.styles as style
from link_bio.styles.styles import Spacer as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(title, font_weight="bold", color="blue"),
        body, font_size=Size.MEDIUM.value
        
    )