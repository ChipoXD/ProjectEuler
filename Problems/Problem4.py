# ProblemURL: https://projecteuler.net/problem=4
a = 999
b = 999
largestPalindrome = 0


def ispalindrome(x):
    for k in range(int(len(x)/2)):
        if x[k] != x[-(k+1)]:
            return False
    return True


for i in range(a, 100, -1):
    for j in range(b, 100, -1):
        number = i * j
        if ispalindrome(str(number)) and number > largestPalindrome:
            largestPalindrome = number

print(largestPalindrome)
