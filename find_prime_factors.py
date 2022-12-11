# find prime factors (OffSec PEN100 cryptography)
# BUGGY !!!!

import time

# Find the prime factors of a number N = 382387, where n = p * q

# list of primes up to 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def find_prime_factors(n, prime_list):
    """find list of prime factors of a large prime number n

    Args:
        n (int): _description_
        prime_list (list): _description_

    Returns:
        list: List of prime factors of n
    """
    factors = []

    while n != 1:
        time_start = time.time()
        num_factors_start = len(factors)

        for i in prime_list:
            if n % i == 0:
                factor = i
                factors.append(factor)
                n //= i
                print(f"n: {n}, current factor: {factor} factors: {factors}")
                time_stop = time.time()
                num_factors_end = len(factors)
                delta_time = time_start - time_stop
                if delta_time > 1000000 and num_factors_start == num_factors_end:
                    break
    return factors


# factor_list = find_prime_factors(100, primes)
# print(factor_list) # works

factor_list = find_prime_factors(382387, primes)
print(factor_list)
