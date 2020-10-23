# ProblemURL: https://projecteuler.net/problem=30
a = 1000001
digitFifthPowers = [False]*a
for i in range(2, a):
    print(i)
    mySum = 0
    for j in str(i):
        mySum += int(j)**5
    if mySum == i:
        digitFifthPowers[i] = True
index = [i for i, j in enumerate(digitFifthPowers) if j]
print(index)
print(f"sum={sum(index)}")