import unittest
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fsm import FSM
from mod_fsm import compute_binary_mod

class TestFSM(unittest.TestCase):

    def test_fsm_outputs(self):
        # FSM with output values on states
        states = {'S0', 'S1'}
        transitions = {
            ('S0', '0'): 'S0',
            ('S0', '1'): 'S1',
            ('S1', '0'): 'S0',
            ('S1', '1'): 'S1',
        }
        outputs = {
            'S0': 0,
            'S1': 1
        }
        fsm = FSM(states, transitions, 'S0', outputs=outputs)
        result = fsm.process_sequence("0110")
        self.assertEqual(result, [0, 1, 1, 0])

    def test_binary_mod_fsm_acceptance(self):
        fsm = compute_binary_mod(3)

        # 6 = binary "110", divisible by 3
        self.assertTrue(fsm.is_accepted("110"))

        # 7 = binary "111", not divisible by 3
        self.assertFalse(fsm.is_accepted("111"))

        # 0 = binary "0", divisible by 3
        self.assertTrue(fsm.is_accepted("0"))

        # Empty string = 0, accepted
        self.assertTrue(fsm.is_accepted(""))

    def test_binary_mod_fsm_non_binary_input(self):
        with self.assertRaises(ValueError):
            fsm = compute_binary_mod(3)
            fsm.process_sequence("abcd")
            fsm.is_accepted("1010")


        
            

    def test_binary_mod_fsm_large(self):
        fsm = compute_binary_mod(5)


        self.assertTrue(fsm.is_accepted("1010"))  # 10 % 5 == 0
        self.assertFalse(fsm.is_accepted("1001"))  # 9 % 5 != 0

    def test_binary_mod_output_consistency(self):
        fsm = compute_binary_mod(4)
        outputs = fsm.process_sequence("1001")
        # The output should be None for all since no outputs were defined
        self.assertEqual(outputs, [None, None, None, None])


if __name__ == '__main__':
    unittest.main()