# ProblemURL: https://projecteuler.net/problem=9
# We can generate Pythagorean triplet a^2 + b^2 = c^2
# a = m**2 - n**2,  b = 2 * n * m,  c = n**2 + m**2 for m > n
# ---------------------------------------------------------------
# We need to find a + b + c = 1000, which means:
# m^2 - n^2 + 2nm + n^2 + m^2 = 1000
# n = (500/m) - m for m > n

m = 2
while True:
    for n in range(1, m):
        if n == (500 / m) - m:
            a = m**2 - n**2
            b = 2 * n * m
            c = n**2 + m**2
            print(f"{n} {m}")
            print(f"a={a}, b={b}, c={c}")
            print(a + b + c)
            print(a * b * c)
            exit()
    m += 1
