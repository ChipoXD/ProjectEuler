# ProblemURL: https://projecteuler.net/problem=5

# FIND PRIME FACTORS
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 2^2
# 5 = 5
# 6 = 2 * 3
# 7 = 7
# 8 = 2^3
# 9 = 3^2
# 10 = 2 * 5

# FROM 1->10
# 1, 2^3, 3^2 5, 7
# 1 * 8 * 9 * 5 * 7 = 2520

# 11 = 11
# 12 = 4 * 3 = 2^2 * 3
# 13 = 13
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2^4
# 17 = 17
# 18 = 2 * 9 = 2 * 3^2
# 19 = 19
# 20 = 2 * 10 = 2 * 2 * 5 = 2^2 * 5

# FROM 1->20
# 1, 2^4, 3^2, 5, 7, 11, 13, 17, 19
# 1 * 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19


def primefactors(x):
    primes = []
    numbers = [x]
    while numbers:
        found = False
        temp = []
        for number in numbers:
            for i in range(2, int(number), 1):
                if number % i == 0:
                    temp.append(i)
                    temp.append(number / i)
                    found = True
                    break
            if not found:
                primes.append(int(number))
        numbers = temp
    return primes


print(primefactors(2520))
