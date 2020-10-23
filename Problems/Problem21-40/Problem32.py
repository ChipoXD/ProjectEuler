# ProblemURL: https://projecteuler.net/problem=32
myList = []
for i in range(1, 100):
    for j in range(100, 10000):
        myStr = str(i) + str(j) + str(i * j)
        if "1" in myStr and "2" in myStr and "3" in myStr and "4" in myStr and "5" in myStr and "6" in myStr and "7" in myStr and "8" in myStr and "9" in myStr and len(myStr) == 9:
            print(f"i:{i}, j:{j} i*j={i * j}")
            myList.append(i*j)
        elif len(myStr) > 9:
            break
myList2 = list(set(myList))
myList2.sort()
print(myList2)
print(sum(myList2))