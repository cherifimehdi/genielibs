import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.utils import clear_counters


class TestClearCounters(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          javelin-morph-sj-full3-dut1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: router
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['javelin-morph-sj-full3-dut1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_clear_counters(self):
        result = clear_counters(self.device, 90)
        expected_output = None
        self.assertEqual(result, expected_output)
