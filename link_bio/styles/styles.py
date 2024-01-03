import reflex as rx
from enum import Enum
#·constantes
MAX_WIDTH="600px"

class Spacer(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"


BASE_STYLES = {
    rx.Button: {
        "width":"100%",
        "height":"100%",
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value
    },
    rx.Link: {
        "text_decoration":"none",
        "_hover": {}
    }
    
}

title_style = dict(
    size="lg",
    width="100%",
    padding_top=Spacer.DEFAULT.value
)

button_tittle_style = dict(
    font_size=Spacer.DEFAULT.value
)

button_body_style = dict(
    font_size=Spacer.MEDIUM.value
)