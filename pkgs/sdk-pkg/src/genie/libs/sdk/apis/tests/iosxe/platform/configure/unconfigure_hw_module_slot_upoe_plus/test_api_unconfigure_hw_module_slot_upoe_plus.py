import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform.configure import unconfigure_hw_module_slot_upoe_plus


class TestUnconfigureHwModuleSlotUpoePlus(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          9407R-dut1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['9407R-dut1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_hw_module_slot_upoe_plus(self):
        result = unconfigure_hw_module_slot_upoe_plus(self.device, 2)
        expected_output = None
        self.assertEqual(result, expected_output)
