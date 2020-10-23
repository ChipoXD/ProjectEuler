# ProblemURL: https://projecteuler.net/problem=31
def coinreturnways(cointypes, amount):
    ways = []
    originialcoinhandler = [0]*len(cointypes)
    coinamount = amount
    for index, coin in enumerate(cointypes):
        while coin <= coinamount:
            coinamount -= coin
            originialcoinhandler[index] += 1
    #ways.append(originialcoinhandler.copy())
    ways = []
    temp = []
    for n in range(len(cointypes)-1):
        temp = [0]*len(cointypes)
        temp[n] = int(amount/cointypes[n])
        ways.append(temp.copy())
        while temp[n] != 0:
            for i in range(1, len(cointypes) + 1):
                if temp[-(i+1)] > 0:
                    temp[-(i+1)] -= 1
                    temp[-i] += int(cointypes[-(i+1)]/cointypes[-i])
                    if cointypes[-(i+1)] % cointypes[-i] != 0:
                        temp[-(i-1)] += 1
                    ways.append(temp.copy())
                    break
        ways.pop()
    return ways


coins = [200, 100, 50, 20, 10, 5, 2, 1]
a = 200
c = coinreturnways(coins, a)
print(c)
print(len(c))
