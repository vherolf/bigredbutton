from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual import events


class KeyLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

    def on_mouse_move(self, event: events.MouseMove) -> None:
        self.write(event)

    def on_mouse(self, event: events.Click) -> None:
        self.write(event)

class InputApp(App):
    """App to display key events."""

    CSS = """
    Screen {
    layout: grid;
    grid-size: 2 2;
    grid-columns: 1fr;
}

KeyLogger {  
    border: blank;
}

KeyLogger:hover {
    border: wide $secondary;
}

KeyLogger:focus {
    border: wide $accent;
}

    """

    def compose(self) -> ComposeResult:
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()


if __name__ == "__main__":
    app = InputApp()
    app.run()
