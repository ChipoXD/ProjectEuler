# ProblemURL: https://projecteuler.net/problem=7
def isprime(x):
    # Must be larger than 1
    if x <= 1:
        return False

    # Only even prime is 2
    if x % 2 == 0:
        if x == 2:
            return True
        else:
            return False

    # Check
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = 10001
found = 0
n = 0
while found < a:
    n += 1
    if isprime(n):
        found += 1
        print(found)
print(n)
