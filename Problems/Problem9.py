# ProblemURL: https://projecteuler.net/problem=9
# We can generate Pythagorean triplet a^2 + b^2 = c^2
# a = m**2 - n**2,  b = 2 * n * m,  c = n**2 + m**2 for m > n
# ---------------------------------------------------------------
# We need to find a + b + c = 100, which means:
# m^2 - n^2 + 2nm + n^2 + m^2 = 100
# n = (50/m) - m for m > n

m = 2
while True:
    for n in range(1, m):
        if n == (50 / m) - m:
            print(f"{n} {m}")
            exit()
    m += 1

    print(m)
