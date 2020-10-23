# ProblemURL: https://projecteuler.net/problem=18
myMap = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

pathChecked = [[""]*i for i in range(1, 16, 1)]
tempPaths = [[[0, 0], 100-myMap[0][0]]]
while True:
    tempShortestPath = float("inf")
    bestFrom = []
    bestTo = []
    pathway = 0
    for path in tempPaths:
        if path[0][0] == 14:
            print(1500 - tempPaths[-1][1])
            exit()
        for i in range(2):
            if str(i) not in pathChecked[path[0][0]][path[0][1]]:
                pathlength = path[1] + 100-myMap[path[0][0]+1][path[0][1]+i]
                if pathlength < tempShortestPath:
                    tempShortestPath = pathlength
                    bestFrom = path[0]
                    bestTo = [path[0][0]+1, path[0][1]+i]
                    pathway = str(i)
    tempPaths.append([bestTo, tempShortestPath])
    pathChecked[bestFrom[0]][bestFrom[1]] += pathway
    print(f"{bestFrom}->{bestTo}, {tempShortestPath}")