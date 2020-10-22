# Module including all def used in ProjectEulor
import itertools


def primefactors(x):
    primes = []
    numbers = [x]
    while numbers:
        found = False
        temp = []
        for number in numbers:
            for i in range(2, int(number), 1):
                if number % i == 0:
                    temp.append(i)
                    temp.append(number / i)
                    found = True
                    break
            if not found:
                primes.append(int(number))
        numbers = temp
    return primes


def ispalindrome(x):
    for k in range(int(len(x)/2)):
        if x[k] != x[-(k+1)]:
            return False
    return True


def isprimebrute(x):
    # Must be larger than 1
    if x <= 1:
        return False

    # Only even prime is 2
    if x % 2 == 0:
        if x == 2:
            return True
        else:
            return False

    # Check
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def isfracrepeatingfromprimefactor(argin):
    if len(argin) == 1 and argin[0] == 1:
        return False
    if argin.count(2) + argin.count(5) == len(argin):
        return False
    return True


def multiplylist(mylist):
    result = 1
    for x in mylist:
        result *= int(x)
    return result


def sieve(n):  # Effective method of finding prime numbers
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


def trianglenumber(x):
    return x*(x+1)/2


def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def propperdivisorsammount(mylist):  # Ammount of divisors given from a list of primes
    d = 1
    uniqueList = list(set(mylist))
    for unique in uniqueList:
        d *= (mylist.count(unique) + 1)
    return d


def devisorfromprimefactor(mylist):
    tempList = []
    unqieList = list(set(mylist))
    for unqiue in unqieList:
        a = []
        for n in range(1, mylist.count(unqiue) + 1, 1):
            a.append(unqiue**n)
        tempList.append(a)
    return tempList


def collatz(argin):  # Algorythm which takes x / 2 for even and (x*3)+1 for odds
    myList = [argin]
    while myList[-1] > 1:
        if myList[-1] % 2 == 0:
            myList.append(myList[-1] / 2)
        else:
            myList.append((myList[-1] * 3) + 1)
    return myList


def binomial(argin1, argin2):
    return (fact(argin1))/(fact(argin2)*(fact(argin1-argin2)))


def numberspelled(argin):  # Can spell numbers from 1 to 1000
    onesDigitSpell = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                      9: "nine"}
    tensDigitSpell = {0: "", 1: "teen", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy",
                      8: "eighty", 9: "ninety"}
    output = ""
    start = 0
    numberList = [int(x) for x in str(argin)]
    if len(numberList) >= 2:
        if numberList[-2] == 1 and numberList[-1] == 0:
            output = "ten"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 1:
            output = "eleven"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 2:
            output = "twelve"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 3:
            output = "thirteen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 4:
            output = "fourteen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 5:
            output = "fifteen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 6:
            output = "sixteen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 7:
            output = "seventeen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 8:
            output = "eighteen"
            start = 2
        elif numberList[-2] == 1 and numberList[-1] == 9:
            output = "nineteen"
            start = 2

    for i in range(1 + start, len(numberList) + 1, 1):
        if i == 1:
            output = output + onesDigitSpell[numberList[-i]]
        if i == 2:
            output = tensDigitSpell[numberList[-i]] + output
        if i == 3:
            if numberList[-1] != 0 or numberList[-2] != 0:
                output = "and" + output
            output = onesDigitSpell[numberList[-i]] + "hundred" + output
        if i == 4:
            output = onesDigitSpell[numberList[-i]] + "thousand"

    return output


def isleapyear(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            return False
        return True
    return False


def allproductpairs(mylist):
    output = []
    for x in mylist:
        x.append(1)
    combination = list(itertools.product(*mylist))
    for x in combination:
        temp = 1
        for y in x:
            temp *= y
        output.append(temp)
    output.sort()
    output.pop(-1)
    return output


def allsumpairs(mylist):
    output = []
    combination = list(itertools.product(*mylist))
    for x in combination:
        temp = 0
        for y in x:
            temp += y
        if temp not in output:
            output.append(temp)
    output.sort()
    return output


def allperm(x):
    output = ["0"]
    for i in range(x-1):
        chunks = (i+2)
        chunklength = len(output)
        output = output*chunks
        for j in range(chunks):
            for k in range(chunklength):
                output[j*chunklength+k] = output[j*chunklength+k][:j] + str(i+1) + output[j*chunklength+k][j:]
    return output


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


class Month:
    def __init__(self, year, monthnumber):
        daysInYear = 365
        daysInLeapYear = 366
        monthLength = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
        monthLengthLeapYear = {0: 31, 1: 29, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
        self.year = year
        self.monthnumber = monthnumber
        days = 0
        for x in range(1900, year, 1):
            if isleapyear(x):
                days += daysInLeapYear
            else:
                days += daysInYear
        for x in range(monthnumber - 1):
            if isleapyear(year):
                days += monthLengthLeapYear[x]
            else:
                days += monthLength[x]
        self.monthFirstDay = days % 7