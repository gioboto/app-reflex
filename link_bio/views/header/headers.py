import reflex as rx
from link_bio.componentes.info_text import info_text
from link_bio.styles.styles import Spacer as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
from link_bio.componentes.link_icon import link_icon
from link_bio.componentes.title import title

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Jorg N.",
                      size="xl",
                      src="fehu.png",
                      color=TextColor.BODY.value,
                      bg=Color.CONTENT.value,
                      padding="2px",
                      border="4px",
                      border_color=Color.PRIMARY.value  
                      ),
            rx.vstack(
                rx.heading("Jorge N",
                         
                ),
                rx.text(
                    "  @El boto",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                link_icon("icons/youtube.svg","http://fehu.me", "Alt text"),
                link_icon("icons/youtube.svg","http://fehu.me", "Alt text"),
                link_icon("icons/youtube.svg","http://fehu.me", "Alt text")
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
        
        rx.text(" tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto ",
                color= TextColor.BODY.value,
                font_size=Size.DEFAULT.value,
                ),
        spacing=Size.BIG.value,
        align_items="start"
    )
    