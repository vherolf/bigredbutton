import logging
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static, TextLog
from textual import events
#from textual.logging import TextualHandler

logging.basicConfig(
    level=logging.DEBUG,
    filename='brb.log',
    encoding='utf-8'
)

class BigRedButton(Static):
    """A big red button widget."""

    def compose(self) -> ComposeResult:
        yield Button("Big Red Button", id="brb", variant="success")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        logging.debug(str(event.button))

class EventLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

    def on_mouse_move(self, event: events.MouseMove) -> None:
        self.write(event)

    def on_mouse(self, event: events.Click) -> None:
        self.write(event)

class BigRedButtonApp(App):
    def on_mount(self) -> None:
        logging.debug("Logged via TextualHandler")

    CSS= """
    Screen {
    layout: grid;
    grid-size: 1 2;
    grid-columns: 1fr;
}

BigRedButton {  
    border: blank;
}

BigRedButton:hover {
    border: wide $secondary;
}

BigRedButton:focus {
    border: wide $accent;
}

EventLogger {  
    border: blank;
}

EventLogger:hover {
    border: wide $secondary;
}

EventLogger:focus {
    border: wide $accent;
}
    """

    def compose(self) -> ComposeResult:
        yield BigRedButton()
        yield EventLogger()

    def on_big_red_button_pressed(self) -> None:
        #self.query_one(EventLogger)
        logging.debug("BRB pressed")
        
if __name__ == "__main__":
    app = BigRedButtonApp()
    app.run()
