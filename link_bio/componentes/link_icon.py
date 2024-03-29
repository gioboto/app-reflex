import reflex as rx
from link_bio.styles.styles import Spacer as Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            witdth=Size.DEFAULT.value,
            alt=alt
            
        ),
        href=url,
        is_external=True
        
    )