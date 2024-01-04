import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight
#·constantes
MAX_WIDTH="600px"

#Sizes 

STYLESHEETS = {
    "https://fonts.google.com/css2?family=Poppins:wght@300;@500display=swap"
    "https://fonts.google.com/css2?family=Conforta:wght@500display=swap"
    
}

class Spacer(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    VERY_BIG = "4em"


BASE_STYLES = {
    "background_color": Color.BACKGROUND.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_family": Font.DEFAULT.value,
    rx.Heading:{
        "size":"lg",
        "color": TextColor.HEADER.value,  
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.LIGHT.value
    },
    rx.Button: {
        "width":"100%",
        "height":"100%",
        #"display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius":Spacer.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value
        },
    },
    rx.Link: {
        "text_decoration":"none",
        "_hover": {}
    }

}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.LIGHT.value,
    font_size=Spacer.DEFAULT.value
)

title_style = dict(
    size="lg",
    width="100%",
    font_family=Font.TITLE.value,
    padding_top=Spacer.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_tittle_style = dict(
    font_size=Spacer.DEFAULT.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    color= TextColor.HEADER.value
)

button_body_style = dict(
    font_size=Spacer.MEDIUM.value,
    font_family=Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value,
    color= TextColor.BODY.value
)