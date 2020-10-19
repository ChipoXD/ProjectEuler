def numberspelled(argin):
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


longstring = ""
for i in range(1, 1001):
    longstring += numberspelled(i)
print(len(longstring))
