import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.ospf.configure import configure_ospf_routing


class TestConfigureOspfRouting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          stack3-nyquist-1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat8k
            model: c8000v
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['stack3-nyquist-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_ospf_routing(self):
        result = configure_ospf_routing(self.device, 200, None, False, True, 'cisco', True, 'debug detail', None, None, True)
        expected_output = None
        self.assertEqual(result, expected_output)
