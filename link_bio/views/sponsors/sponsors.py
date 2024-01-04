import reflex as rx
from link_bio.componentes.title import title
from link_bio.componentes.link_sponsor import link_sponsor
import link_bio.contantes as const
from link_bio.styles.styles import Spacer as Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.responsive_grid(
            link_sponsor(
                "sponsor1.jpeg",
                const.SPONSOR1,
                "texto sponsor"
                
            ),
            link_sponsor(
                "sponso2.jpeg",
                const.SPONSOR2,
                "texto sponsor"                
            ),
            spacing=Size.DEFAULT.value,
            columns=[1,2]
        ),
        width="100%",
        align_items="start"
    )