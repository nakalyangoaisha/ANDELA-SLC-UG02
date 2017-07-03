import unittest
from math import sqrt
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

    def test_function_returns_list(self):
        self.assertTrue(isinstance(generatePrimeNumbers(self.arg_limit), list))

    def test_list_returned_contains_values_greater_than_one(self):
        self.assertTrue(all(x >= 2 for x in generatePrimeNumbers(self.arg_limit)))

    def test_function_returns_prime_numbers_less_than_arg(self):
        self.assertTrue(all(x < self.arg_limit for x in generatePrimeNumbers(self.arg_limit)))

    def test_function_returns_only_prime_numbers(self):
        isprime = True
        for x in generatePrimeNumbers(self.arg_limit):
            sqrt_value = sqrt(x)
            sample_range = []
            for i in self.sample_prime:
                if i <= int(sqrt_value):
                    sample_range.append(i)
            for y in sample_range:
                if x % y == 0:
                    isprime = False
                    break
        self.assertTrue(isprime)


if __name__ == '__main__':
    unittest.main()
