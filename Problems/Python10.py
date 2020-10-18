# ProblemURL: https://projecteuler.net/problem=10
def sieve(n):
    prime = [True]*n
    prime[0] = False
    prime[1] = False
    i = 2
    while i * i <= n:
        if not prime[i]:
            i += 1
            continue

        j = 2 * i
        while j < n:
            prime[j] = False
            j += i

        i += 1
    return prime


num = []
myList = sieve(2000000)
for i in range(2000000):
    if myList[i]:
        num.append(i)
print(sum(num))
