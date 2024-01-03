import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Jorg N.", size="xl"),
        rx.text(" @El boto"),
        rx.text(" Hola mi nombre es Jhon Connor"),
        rx.text(" tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto  tesxto testto texto "),
    )
    