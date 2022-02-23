import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.nat.configure import configure_enable_nat_scale


class TestConfigureEnableNatScale(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Stargazer:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Stargazer']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_enable_nat_scale(self):
        result = configure_enable_nat_scale(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
