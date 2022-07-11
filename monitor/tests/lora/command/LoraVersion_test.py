from src.lora.command.BaseCommand import BaseCommand
from src.lora.command.LoraVersion import LoraVersion
from src.lora.command.Version import Version
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestLoraVersion(BaseTestCommand):
    def test(self):
        self.validate(
            cmd=LoraVersion(),
            pattern="\+"
            + BaseCommand.LORA_PREFIX
            + ": "
            + Version.COMMAND_VERSiON
            + ", V\d+",
        )
