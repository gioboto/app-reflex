import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width=styles.Spacer.BIG.value,
                    height=styles.Spacer.BIG.value,
                    marging=styles.Spacer.MEDIUM.value,
                    
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=styles.Spacer.SMALL.value,
                    align_items="start",
                    marging=styles.Spacer.ZERO.value,
                )
            )
            
        ),
            href=url,
            is_external=True,
            width = "100%"
            #text_decoration="none"
    )
           
    