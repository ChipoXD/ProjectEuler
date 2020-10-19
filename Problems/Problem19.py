# ProblemURL: https://projecteuler.net/problem=19
daysInYear = 365
daysInLeapYear = 366
day = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday", 6: "sunday"}
monthLength = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
monthLengthLeapYear = {0: 31, 1: 29, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}


def isleapyear(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            return False
        return True
    return False


class Month:
    def __init__(self, year, monthnumber):
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


sundayList = []
for i in range(1901, 2001, 1):
    for j in range(1, 13, 1):
        sundayList.append(Month(i, j))

sundayammount = 0
for m in sundayList:
    if m.monthFirstDay == 6:
        sundayammount += 1
print(sundayammount)