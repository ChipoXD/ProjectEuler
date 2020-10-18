# ProblemURL: https://projecteuler.net/problem=10
import multiprocessing as mp

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

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
    mylist = primes(2000001)
    print(sum(mylist))


if __name__ == "__main__":
    main()
