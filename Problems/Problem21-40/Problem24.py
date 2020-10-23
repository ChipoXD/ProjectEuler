# ProblemURL: https://projecteuler.net/problem=24
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


perm = allperm(10)
perm.sort()
print(perm[999999])
