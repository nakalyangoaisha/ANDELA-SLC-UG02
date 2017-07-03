import unittest
from Generate_prime_numbers import generatePrimeNumbers


class TestGeneratePrimeNumbers(unittest.TestCase):
    def setUp(self):
        self.arg_limit = 32
        self.sample_prime = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31]
        self.sample_prime_length = 11

    def test_function_returns_error_message_if_arg_not_integer(self):
        self.assertRaises(TypeError, generatePrimeNumbers, 'two')

    def test_function_returns_error_if_arg_is_less_than_three(self):
        self.assertRaises(ValueError, generatePrimeNumbers, 2)
    

