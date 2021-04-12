def calcMat(matA, B):
    if len(matA) < 4:
        return gaussianElimination(matA, B)
    else:
        print("Use Lu")

def calcAnswer(matA, matB):
    return "asaf" + " david"

def detCalculator(matA): #it works!!!
    matLen = len(matA)
    if matLen < 2:
        return None
    if matLen == 2:
        return (matA[0][0] * matA[1][1]) - (matA[0][1] * matA[1][0])
    else:
        sum = 0
        currentRow = 0
        # will calculate det of first row
        # We assume that its a square matrix
        for currentCol in range(matLen):
            newMat = [x[:] for x in matA]
            for row in range(matLen):
                del newMat[row][currentCol]
            del newMat[currentRow]
            pivot = matA[currentRow][currentCol]
            if currentCol % 2 != 0:
                pivot *= -1
            printMatrix(newMat)
            sum += pivot * detCalculator(newMat)
        return sum

# def elementryInverse(A):

def gaussianElimination(matA, matB):
    matA, matB = makeUpperTriangular(matA, matB)
    x = calcAnswer(matA,matB)
    return matA

def inverse(mat):
    inverseMat = makeIdentityMat(len(mat))
    matCopy = [x[:] for x in mat]
    dim = len(mat)
    for row in range(dim):
        if matCopy[row][row] == 0:
        #for column in range(dim):
            print("im done for today, C ya tomorrow")
    return 0

def LU(matA, matB):
    I = makeIdentityMat(len(matA))
    makeUpperTriangular(pivoting(matA), matB, I)

def makeIdentityMat(dim):
    # Works for square mat only
    identityMat = []
    for i in range(dim):
        rowMat = []
        for j in range(dim):
            if i == j:
                rowMat.append(1)
            else:
                rowMat.append(0)
        identityMat.append(rowMat)
    return identityMat

def makeUpperTriangular(matA, matB, I = None):
    dim = len(matA)
    for i in range(dim):
        for j in range(i + 1):
            # print("[", i, "]", " [", j, "]")
            if i == j:
                matA, matB = makePivotOne(i, matA, matB, I)
            else:
                matA, matB = makePivotZero(i, j, matA, matB, I)
    return (matA, matB)

def makePivotZero(i, j, matA, matB, I):
    if matA[j][j] == 0:
        return matA
    if I == None:
        I = makeIdentityMat(len(matA))
    I[i][j] = -matA[i][j] / matA[j][j]
    return (matMultiply(I, matA), matMultiply(I, matB))

def makePivotOne(i, matA, matB, I = None):
    if matA[i][i] == 0:
        return matA
    if I == None:
        I = makeIdentityMat(len(matA))
    I[i][i] = 1 / matA[i][i]
    return (matMultiply(I, matA), matMultiply(I, matB))

def matMultiply(matA, matB):
    # multiply from the left: A * B.
    result = []
    for i in range(len(matA)):
        rowMat = []
        for j in range(len(matB[i])):
            index = 0
            for k in range(len(matB)):
                index += matA[i][k] * matB[k][j]
            rowMat.append(index)
        result.append(rowMat)
    return result

def norm(matA):
    result = 0
    for row in matA:
        currentRowSum = 0
        for column in matA[row]:
            currentRowSum += abs(matA[row][column])
        if currentRowSum > result:
            result = currentRowSum
    return result

def pivoting(matA):
    # find max pivot in each column
    n = len(matA)
    for row in range(n):
        for col in range(row,n):
            if abs(matA[col][row]) > abs(matA[row][row]):
                matA[row], matA[col] = matA[col],matA[row]
    return matA

def printMat(mat):
    for row in mat:
            print(row)

# _______________________________________________________________


Q = [[1, 3, 5, 9],
     [1, 3, 1, 7],
     [4, 3, 9, 7],
     [5, 2, 0, 9]]

A = [[11, 13, 7],
     [6.5, 12, 3],
     [13, 0, 9]]

B = [[4],[3],[2]]

S = [[1, 3, 2],
     [2, 6, 4],
     [1, 0, 3]]

print(pivoting(A))
# print(matMultiply(A, B))
# print(calcMat(A, B))
# print(detCalculator(A))
