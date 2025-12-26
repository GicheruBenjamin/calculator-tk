class CalculatorService:
    def __init__(self):
        self.expression = ""

    def process(self, value):
        if value == "C":
            self.expression = ""
            return ""

        if value == "=":
            try:
                result = str(eval(self.expression))
                self.expression = result
                return result
            except Exception:
                self.expression = ""
                return "Error"

        self.expression += value
        return self.expression
