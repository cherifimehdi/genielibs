import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.nat.configure import configure_dynamic_nat_pool_overload_route_map_rule


class TestConfigureDynamicNatPoolOverloadRouteMapRule(unittest.TestCase):

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

    def test_configure_dynamic_nat_pool_overload_route_map_rule(self):
        result = configure_dynamic_nat_pool_overload_route_map_rule(self.device, 'static_rm', 'pool_b')
        expected_output = None
        self.assertEqual(result, expected_output)
