import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.dot1x.configure import config_identity_ibns


class TestConfigIdentityIbns(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Switch:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: None
            type: c9200
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Switch']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_config_identity_ibns(self):
        result = config_identity_ibns(self.device, 'DOT1X-MUST-SECURE-UPLINK', 'Gi1/0/1', True, 'auto', None, 'both')
        expected_output = None
        self.assertEqual(result, expected_output)
