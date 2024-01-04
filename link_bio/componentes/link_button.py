import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Spacer as Size

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Spacer.BIG.value,
                    height=styles.Spacer.BIG.value,
                    marging=styles.Spacer.MEDIUM.value,
                    alt=title
                    
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=styles.Spacer.SMALL.value,
                    align_items="start",
                    #marging=styles.Spacer.ZERO.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            )
            
        ),
            href=url,
            is_external=True,
            width = "100%"
            #text_decoration="none"
    )
           
    