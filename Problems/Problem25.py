# ProblemURL: https://projecteuler.net/problem=25
def febonacci(arrgin):
    output = [0, 1]
    if arrgin == 0:
        return 0
    for i in range(arrgin-1):
        output.append(output[-1] + output[-2])
    return output[-1]


def firstfebonacciatlen(arrgin):
    output = [0, 1]
    if arrgin == 0:
        return 0
    while len(str(output[-1])) < arrgin:
        output.append(output[-1] + output[-2])
    return str(f"{len(output) - 1}: {output[-1]}")


print(firstfebonacciatlen(1000))