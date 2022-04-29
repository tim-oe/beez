from src.lora.command.Temperature import Temperature
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestTemprature(BaseTestCommand):
    def test(self):
        self.validate(
            cmd=Temperature(), pattern="\+" + Temperature.COMMAND_TEMP + ": [\d\.]+"
        )
