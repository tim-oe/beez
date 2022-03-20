from src.lora.command.Key import Key
from src.lora.command.Mode import Mode
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestId(BaseTestCommand):
    def test(self):
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=Key.app("c2 11 ae 38 53 3a dc 50 e7 82 c4 2e 14 c4 d4 88"),
            pattern="\+" + Key.COMMAND_KEY + ": " + Key.KEY_APP,
        )
