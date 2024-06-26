# Python
import unittest

# ATS
from pyats.topology import Device
from unittest.mock import Mock

# Genie
from genie.libs.ops.terminal.iosxr.terminal import Terminal
from genie.libs.ops.terminal.iosxr.tests.terminal_output import TerminalOutput

# Parser
from genie.libs.parser.iosxr.show_terminal import ShowTerminal

outputs = {
    'show terminal' : TerminalOutput.ShowTerminal
}
def mapper(key, **kwargs):
    return outputs[key]

class test_show_terminal(unittest.TestCase):

    def setUp(self):
        self.device = Device(name='aDevice', os='iosxr')
        self.device.custom.setdefault("abstraction", {})["order"] = ["os"]
        self.device.mapping = {'cli': 'cli'}
        mock_connection = Mock()
        mock_connection.device = self.device
        self.device.connectionmgr.connections['cli'] = mock_connection
        mock_connection.execute.side_effect = mapper

    def test_empty_output(self):
        self.maxDiff = None
        show_term = Terminal(device=self.device)

        # Get outputs
        show_term.maker.outputs[ShowTerminal] = {"": {}}

        # Learn the feature
        show_term.learn()

        # Check info was not created
        self.assertFalse(hasattr(show_term, 'info'))

    def test_complete_output(self):
        self.maxDiff = None
        show_term = Terminal(device=self.device)

        # Get outputs
        show_term.maker.outputs[ShowTerminal] = {
            '': TerminalOutput.ShowTerminal
        }

        # Learn the feature
        show_term.learn()
        # Verify Ops was created successfully
        self.assertEqual(show_term.info, TerminalOutput.ShowTerminalInfo)


if __name__ == '__main__':
    unittest.main()