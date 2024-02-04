import unittest
from unittest.mock import patch
from project import takeCommand

class TestProjectFunctions(unittest.TestCase):
    @patch('builtins.input', return_value='Hello')
    def test_takeCommand_with_input(self, mock_input):
        result = takeCommand()
        self.assertEqual(result, 'Hello')

    @patch('builtins.input', side_effect=Exception("Some Error Occurred. Extremely sorry SIR!!"))
    def test_takeCommand_with_error(self, mock_input):
        result = takeCommand()
        self.assertEqual(result, "Some Error Occurred. Extremely sorry SIR!!")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
