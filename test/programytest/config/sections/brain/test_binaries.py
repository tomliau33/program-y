import unittest

from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.sections.brain.binaries import BrainBinariesConfiguration
from programy.config.sections.client.console import ConsoleConfiguration

class BrainBinariesConfigurationTests(unittest.TestCase):

    def test_with_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            binaries:
              save_binary: true
              load_binary: true
              binary_filename: /tmp/y-bot.brain
              load_aiml_on_binary_fail: true
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        binaries_config = BrainBinariesConfiguration()
        binaries_config.load_config_section(yaml, brain_config, ".")

        self.assertTrue(binaries_config.save_binary)
        self.assertTrue(binaries_config.load_binary)
        self.assertEquals("/tmp/y-bot.brain", binaries_config.binary_filename)
        self.assertTrue(binaries_config.load_aiml_on_binary_fail)

    def test_without_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
            binaries:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        binaries_config = BrainBinariesConfiguration()
        binaries_config.load_config_section(yaml, brain_config, ".")

        self.assertFalse(binaries_config.save_binary)
        self.assertFalse(binaries_config.load_binary)
        self.assertIsNone(binaries_config.binary_filename)
        self.assertFalse(binaries_config.load_aiml_on_binary_fail)

    def test_with_no_data(self):
        yaml = YamlConfigurationFile()
        self.assertIsNotNone(yaml)
        yaml.load_from_text("""
        brain:
        """, ConsoleConfiguration(), ".")

        brain_config = yaml.get_section("brain")

        binaries_config = BrainBinariesConfiguration()
        binaries_config.load_config_section(yaml, brain_config, ".")

        self.assertFalse(binaries_config.save_binary)
        self.assertFalse(binaries_config.load_binary)
        self.assertIsNone(binaries_config.binary_filename)
        self.assertFalse(binaries_config.load_aiml_on_binary_fail)
