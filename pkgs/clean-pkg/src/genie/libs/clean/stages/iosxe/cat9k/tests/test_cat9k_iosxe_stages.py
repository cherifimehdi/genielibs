
# Python
import logging
import unittest
from unittest.mock import Mock, MagicMock

# pyATS
from pyats.topology import Device
from pyats.aetest.steps import Steps
from pyats.aetest.base import TestItem
from pyats.kleenex.engine import KleenexEngine
from pyats.kleenex.loader import KleenexFileLoader
from pyats.aetest.signals import AEtestPassedSignal, AEtestFailedSignal, \
                                 AEtestStepPassedSignal, AEtestStepFailedSignal,\
                                 TerminateStepSignal

# Unicon
from unicon.core.errors import SubCommandFailure, ConnectionError, TimeoutError,\
                               StateMachineError

# Genie
from genie.testbed import load
from genie.libs.clean.stages.iosxe.cat9k.stages import change_boot_variable
from genie.libs.clean.stages.stages import connect

# Positive Mock Outputs
from genie.libs.clean.stages.iosxe.cat9k.tests.cat9k_iosxe_pos_stage_outputs import \
                                            StageOutputs as PassedStageOutputs,\
                                            get_execute_output as pos_execute,\
                                            get_parsed_output as pos_parsed,\
                                            get_config_output as pos_config

# Negative Mock Outputs
from genie.libs.clean.stages.iosxe.cat9k.tests.cat9k_iosxe_neg_stage_outputs import \
                                            StageOutputs as FailedStageOutputs,\
                                            get_execute_output as neg_execute,\
                                            get_parsed_output as neg_parsed,\
                                            get_config_output as neg_config

# Disable log messages
logging.disable(logging.CRITICAL)


class PositiveStages(unittest.TestCase):

    def setUp(self):
        # Load sample testbed YAML & clean YAML
        self.tb = load('./mock_testbed.yaml')
        self.clean_config = KleenexFileLoader(testbed=self.tb,
                                              invoke_clean=True).\
                                              load('./mock_clean.yaml')
        KleenexEngine.update_testbed(self.tb, **self.clean_config['devices'])

        self.steps = Steps()
        self.device = self.tb.devices['PE1']
        self.raw_output = PassedStageOutputs
        self.section = TestItem(uid='test', description='', parameters={})


    def test_stage_change_boot_variable(self):
        self.device.parse = Mock(side_effect=pos_parsed)
        self.device.configure = Mock(side_effect=pos_config)
        self.device.execute = Mock(side_effect=pos_execute)

        # Execute stage: change_boot_variable
        with self.assertRaises(AEtestPassedSignal):
            change_boot_variable(self.section, self.steps, self.device,
                                 **self.device.clean.change_boot_variable)


class NegativeStages(unittest.TestCase):

    def setUp(self):
        # Load sample testbed YAML & clean YAML
        self.tb = load('./mock_testbed.yaml')
        self.clean_config = KleenexFileLoader(testbed=self.tb,
                                              invoke_clean=True).\
                                              load('./mock_clean.yaml')
        KleenexEngine.update_testbed(self.tb, **self.clean_config['devices'])

        self.steps = Steps()
        self.device = self.tb.devices['PE1']
        self.raw_output = FailedStageOutputs
        self.section = TestItem(uid='test', description='', parameters={})


    def test_stage_change_boot_variable1(self):
        self.device.parse = Mock(side_effect=neg_parsed)
        self.device.configure = Mock(side_effect=KeyError("negative test"))
        self.device.execute = Mock(side_effect=neg_execute)

        # Execute stage: change_boot_variable
        with self.assertRaises(TerminateStepSignal):
            change_boot_variable(self.section, self.steps, self.device,
                                 **self.device.clean.change_boot_variable)


    def test_stage_change_boot_variable2(self):
        self.device.parse = Mock(side_effect=neg_parsed)
        self.device.configure = Mock(side_effect=neg_config)
        self.device.execute = Mock(side_effect=neg_execute)

        # Execute stage: change_boot_variable
        with self.assertRaises(AEtestFailedSignal):
            change_boot_variable(self.section, self.steps, self.device,
                                 **self.device.clean.change_boot_variable)


if __name__ == '__main__':
    unittest.main()
