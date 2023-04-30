import logging

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Static, TextLog
from textual import events

import asyncio

import os
logdir = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(logdir,'bigredbutton.log'),
    encoding='utf-8'
)

class BigRedButton(Static):
    """A big red button widget."""

    def compose(self) -> ComposeResult:
        yield Button("Big Red Button", id="bigredbutton", variant="success")

    async def runcommand(self):
        command = 'date'
        process = await asyncio.create_subprocess_shell(command,
                                            stdout=asyncio.subprocess.PIPE,
                                            stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        logging.debug(stdout.decode())
        return stdout.decode()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        logging.debug(str(event.button))
        await self.runcommand()

class EventLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

    def on_mouse_move(self, event: events.MouseMove) -> None:
        self.write(event)

class BigRedButtonApp(App):
    def on_mount(self) -> None:
        logging.debug("Started")

    CSS= """
    Screen {
        layout: grid;
        grid-size: 1 2;
        grid-columns: 1fr;
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
      
if __name__ == "__main__":
    app = BigRedButtonApp()
    app.run()
