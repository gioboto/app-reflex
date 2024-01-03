import reflex as rx
from link_bio.styles.styles import Spacer as Size

def navbar() -> rx.Component:
    return rx.hstack (
        rx.text(
            "Mi PAg..."
            
        ),
        position="sticky",
        bg="ligthgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )