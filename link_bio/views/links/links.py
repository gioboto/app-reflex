import reflex as rx
from link_bio.componentes.link_button import link_button
from link_bio.componentes.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twich", "Directos", "https://twich"),
        link_button("Youtube", "losVideos", "https://twich"),
        link_button("Youtube cabak secudario", "secundary cabnal", "https://twich"),
        link_button("Discord","las charlas", "https://twich"),
        title("Comunidad"),
        link_button("Twich", "Directos", "https://twich"),
        link_button("Youtube", "losVideos", "https://twich"),
        link_button("Youtube cabak secudario", "secundary cabnal", "https://twich"),
        link_button("Discord","las charlas", "https://twich"),
        width="100%"
    )

