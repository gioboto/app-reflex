import reflex as rx
from link_bio.componentes.link_button import link_button
from link_bio.componentes.title import title
from link_bio.styles.styles import Spacer as Size
import link_bio.contantes as conts



def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twich", "Directos", "icons/youtube.svg", conts.DISCORD_URL),
        link_button("Youtube", "losVideos", "icons/youtube.svg", conts.YOUTUBE_URL),
        link_button("Youtube cabak secudario", "secundary cabnal", "icons/youtube.svg", "https://twich"),
        link_button("Discord","las charlas", "icons/youtube.svg", "https://twich"),
        title("Comunidad"),
        link_button("Twich", "Directos", "icons/youtube.svg", "https://twich"),
        link_button("Youtube", "losVideos", "icons/youtube.svg", "https://twich"),
        link_button("Youtube cabak secudario", "secundary cabnal", "icons/youtube.svg", "https://twich"),
        link_button("Discord","las charlas", "icons/youtube.svg", "https://twich"),
        title("Contacto"),
        link_button("Email","las charlas", "icons/youtube.svg", f"mailto:asd@web.dre"),
        width="100%",
        spacing=Size.DEFAULT.value,
    )

