from components.ui.title import Title
from components.ui.input import Display
from components.ui.button import Buttons
from services.calculations import CalculatorService

class AppLayout:
    def __init__(self, root):
        self.service = CalculatorService()

        Title(root)
        self.display = Display(root)

        Buttons(
            root,
            on_click=self.handle_click
        )

    def handle_click(self, value):
        result = self.service.process(value)
        self.display.update(result)
