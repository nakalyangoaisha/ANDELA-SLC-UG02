from math import sqrt


def generatePrimeNumbers(number):
    prime_list = []
    if isinstance(number, int):
        if number >= 3:
            prime_list.append(2)
            nextprime = 3
            while nextprime < number:
                isprime = True
                sqrt_value = sqrt(nextprime)
                sample_range = [i for i in prime_list if i <= sqrt_value]
                for i in sample_range:
                    if nextprime % i == 0:
                        isprime = False
                        break
                if isprime:
                    prime_list.append(nextprime)
                nextprime += 2
            return prime_list
        else:
            raise ValueError('Argument should be greater or equal to 3')
    else:
        raise TypeError('Argument should be a positive integer')
