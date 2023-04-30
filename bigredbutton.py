from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static, TextLog
from textual import events

class BigRedButton(Static):
    """A big red button widget."""

    def compose(self) -> ComposeResult:
        yield Button("Big Red Button", id="brb", variant="success")


class EventLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

    def on_mouse_move(self, event: events.MouseMove) -> None:
        self.write(event)

    def on_mouse(self, event: events.Click) -> None:
        self.write(event)

class BigRedButtonApp(App):

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
        self.query_one(EventLogger).
        
if __name__ == "__main__":
    app = BigRedButtonApp()
    app.run()
