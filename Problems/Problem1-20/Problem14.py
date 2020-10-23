# ProblemURL: https://projecteuler.net/problem=14
def collatz(argin):
    myList = [argin]
    while myList[-1] > 1:
        if myList[-1] % 2 == 0:
            myList.append(myList[-1] / 2)
        else:
            myList.append((myList[-1] * 3) + 1)
    return myList


longestChain = 0
longestChainNum = 1
for i in range(1, 1000001, 1):
    x = collatz(i)
    if len(x) > longestChain:
        longestChain = len(x)
        longestChainNum = i
        print(f"{longestChainNum}: {longestChain}")
