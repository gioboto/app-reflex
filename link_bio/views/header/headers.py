import reflex as rx
from link_bio.componentes.info_text import info_text
from link_bio.styles.styles import Spacer as Size
from link_bio.componentes.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Jorg N.",
                      size="xl"),
            rx.vstack(
                rx.heading("Jorge N", 
                        size="lg"
                ),
                rx.text(
                    "  @El boto",
                    margin_top="0px !important"
                ),
                rx.hstack(
                link_icon("http://fehu.me"),
                link_icon("http://fehu.me"),
                link_icon("http://fehu.me")
                ),
            ),
            
            align_items="start"
        ),
        
        rx.flex(
            info_text("+5 ", "años de experiencia"),
            rx.spacer(),
            info_text("+5 ", "años de experiencia"),
            rx.spacer(),
            info_text("+5 ", "años de experiencia"),
            width="100%"
        ),
        
        rx.text(" tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto "),
        spacing=Size.BIG.value,
        align_items="start"
    )
    