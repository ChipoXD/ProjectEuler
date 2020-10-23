# ProblemURL: https://projecteuler.net/problem=31
target = 201
ways = 0
for a in range(target, 0, -200):
    for b in range(a, 0, -100):
        for c in range(b, 0, -50):
            for d in range(c, 0, -20):
                for e in range(d, 0, -10):
                    for f in range(e, 0, -5):
                        for i in range(f, 0, -2):
                                ways += 1
print(ways)