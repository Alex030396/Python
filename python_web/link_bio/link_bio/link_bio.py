import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("hola Mundo")

app = rx.App()
app.add_page(index)