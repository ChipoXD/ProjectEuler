# ProblemURL: https://projecteuler.net/problem=67
f = open('Problem67data.txt', 'r')
content = f.read().split("\n")
f.close()
myMap = [y.split() for y in content]

pathChecked = [[""]*i for i in range(1, 101, 1)]
tempPaths = [[[0, 0], 100-int(myMap[0][0])]]
while True:
    tempShortestPath = float("inf")
    bestFrom = []
    bestTo = []
    pathway = 0
    for path in tempPaths:
        if path[0][0] == 99:
            print(10000 - tempPaths[-1][1])
            exit()
        for i in range(2):
            if str(i) not in pathChecked[path[0][0]][path[0][1]]:
                pathlength = path[1] + 100-int(myMap[path[0][0]+1][path[0][1]+i])
                if pathlength < tempShortestPath:
                    tempShortestPath = pathlength
                    bestFrom = path[0]
                    bestTo = [path[0][0]+1, path[0][1]+i]
                    pathway = str(i)
    tempPaths.append([bestTo, tempShortestPath])
    pathChecked[bestFrom[0]][bestFrom[1]] += pathway
    print(f"{bestFrom}->{bestTo}, {tempShortestPath}")