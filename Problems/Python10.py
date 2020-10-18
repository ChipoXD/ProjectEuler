# ProblemURL: https://projecteuler.net/problem=10
import multiprocessing as mp
def is_prime2(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True



def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def isprime(argin):
    # Must be larger than 1
    if argin <= 1:
        return False

    # Only even prime is 2
    if argin % 2 == 0:
        if argin == 2:
            return True
        else:
            return False

    # Check
    for i in range(2, argin):
        if argin % i == 0:
            return False
    print(f"{argin} is prime")
    return True


def main():
    mylist = []
    for i in range(2000001):
        print(i)
        mylist.append(is_prime2((i)))
    print(mylist)


if __name__ == "__main__":
    main()
