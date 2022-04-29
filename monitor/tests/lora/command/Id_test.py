from src.lora.command.BaseCommand import BaseCommand
from src.lora.command.Id import Id
from src.lora.command.Mode import Mode
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestId(BaseTestCommand):
    def testRead(self):
        self.validate(cmd=Id(), pattern="\+" + Id.COMMAND_ID + ": ")

    def testDevAddr(self):
        self.modem.send(Mode.abp())
        self.validate(
            cmd=Id.devAddr("01:23:45:67"),
            pattern="\+"
            + Id.COMMAND_ID
            + ": "
            + Id.ID_DEV_ADDR
            + BaseCommand.COMMAND_COMMA
            + " \d{2}:\d{2}:\d{2}:\d{2}",
        )

    def testDevEui(self):
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=Id.devEui("2C:F7:F1:20:32:30:65:C5"),
            pattern="(?i)\+"
            + Id.COMMAND_ID
            + ": "
            + Id.ID_DEV_EUI
            + BaseCommand.COMMAND_COMMA
            + " [a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}",
        )

    def testAppEui(self):
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=Id.appEui("80:00:00:00:00:00:00:06"),
            pattern="(?i)\+"
            + Id.COMMAND_ID
            + ": "
            + Id.ID_APP_EUI
            + BaseCommand.COMMAND_COMMA
            + " [a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}",
        )
