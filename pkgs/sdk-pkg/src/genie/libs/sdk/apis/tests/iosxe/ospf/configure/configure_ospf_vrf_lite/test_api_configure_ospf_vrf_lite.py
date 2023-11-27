import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.ospf.configure import configure_ospf_vrf_lite


class TestConfigureOspfVrfLite(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          PE1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: None
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['PE1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_ospf_vrf_lite(self):
        result = configure_ospf_vrf_lite(self.device, '11', 'vrf1')
        expected_output = None
        self.assertEqual(result, expected_output)
