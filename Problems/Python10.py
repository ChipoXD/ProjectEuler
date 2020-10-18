# ProblemURL: https://projecteuler.net/problem=10
import multiprocessing as mp

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
    return True

output = 2
bigList = list(range(3, 2000001, 2))
for i in bigList:
    if not isprime(i):
        for j in range(i, 2000001, i):
            print(j)
            try:
                bigList.remove(j)
            except ValueError:
                pass
    print(i)
print(bigList)


def main():
    pool = mp.Pool(mp.cpu_count())

if __name__ == "__main__":
  main()
