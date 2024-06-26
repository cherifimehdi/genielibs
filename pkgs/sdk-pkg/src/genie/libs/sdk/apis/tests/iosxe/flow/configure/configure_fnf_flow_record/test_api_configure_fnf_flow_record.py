import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.flow.configure import configure_fnf_flow_record


class TestConfigureFnfFlowRecord(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          SG-HA:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: c9600
            type: c9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['SG-HA']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_fnf_flow_record(self):
        result = configure_fnf_flow_record(self.device, 'dnacrecord_1', False, None, None, None, None, None, 'True', 'True', None, None, 'True', False, False, None, None, False, None, False, False, False, None, 'source', None, None, None)
        expected_output = None
        self.assertEqual(result, expected_output)
