import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.eigrp.get import get_eigrp_interfaces


class TestGetEigrpInterfaces(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          R1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['R1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_get_eigrp_interfaces(self):
        result = get_eigrp_interfaces(self.device, 'default', 3, 'ipv4')
        expected_output = []
        self.assertEqual(result, expected_output)

    def test_get_eigrp_interfaces_1(self):
        result = get_eigrp_interfaces(self.device, 'default', 3, 'ipv6')
        expected_output = ['FastEthernet0/0']
        self.assertEqual(result, expected_output)

    def test_get_eigrp_interfaces_2(self):
        result = get_eigrp_interfaces(self.device, 'default', 1, 'ipv4')
        expected_output = ['FastEthernet0/0']
        self.assertEqual(result, expected_output)

    def test_get_eigrp_interfaces_3(self):
        result = get_eigrp_interfaces(self.device, 'default', 2, 'ipv4')
        expected_output = ['FastEthernet1/0']
        self.assertEqual(result, expected_output)
