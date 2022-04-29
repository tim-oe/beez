from src.lora.command.Join import Join
from src.lora.command.Mode import Mode
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestId(BaseTestCommand):
    def test(self):
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=Join(), pattern="\+" + Join.COMMAND_JOIN + ": " + Join.JOIN_NORMAL
        )

    # not working?
    def force(self):
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=Join(True), pattern="\+" + Join.COMMAND_JOIN + ": " + Join.JOIN_NORMAL
        )
