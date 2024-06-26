import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.platform.configure import configure_diagnostic_monitor_interval_module


class TestConfigureDiagnosticMonitorIntervalModule(unittest.TestCase):

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

    def test_configure_diagnostic_monitor_interval_module(self):
        result = configure_diagnostic_monitor_interval_module(self.device, 1, 'TestUnusedPortLoopback', '00:01:00', 0, 0)
        expected_output = None
        self.assertEqual(result, expected_output)
