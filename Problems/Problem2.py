# ProblemURL: https://projecteuler.net/problem=2
fibonacciSeq = [0, 1]
a = 4000000
sumOfEven = 0
while fibonacciSeq[-1] < a:
    fibonacciSeq.append(fibonacciSeq[-1] + fibonacciSeq[-2])
fibonacciSeq.pop()  # Need to pop because we get one element over 4.000.000
for n in fibonacciSeq:
    if n % 2 == 0:
        sumOfEven += n
print(sumOfEven)