from src.lora.command.Mode import Mode
from src.lora.command.Message import Message
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestMessage(BaseTestCommand):
    def test(self):
        # will error in other modes
        self.modem.send(Mode.abp())
        self.validate(
            cmd=Message("test"), pattern="\+" + Message.COMMAND_MESSAGE + ": Start"
        )
