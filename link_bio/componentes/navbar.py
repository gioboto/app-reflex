import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack (
        rx.text(
            "Mi PAg..."
            
        ),
        position="sticky",
        bg="ligthgray",
        padding_x="16px",
        padding_y="16px",
        z_index="999"
    )