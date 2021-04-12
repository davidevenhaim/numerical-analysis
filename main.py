def calcMat(matA, result):
    if len(matA) < 4:
        return gaussianElimination(matA, result)
    else:
        print("Use Lu")

def calcAnswer(matA, result):
    n = len(matA)
    print(matA)
    print(result)
    vector = [0] * n
    vector[n-1] = result[n-1][0]
    print(vector)
    for i in range(n - 2 , -1, -1):
        vector[i] = result[i][0]
        for j in range(n - 1, i , -1):
            if matA[i][j] != 0:
                vector[i] -= matA[i][j] * vector[j]
        vector[i] /= matA[i][i]
    print(matA)
    print(result)
    print(vector)

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

def gaussianElimination(matA, result):
    matA, result = makeUpperTriangular(matA, result)
    x = calcAnswer(matA,result)
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

def LU(matA, result):
    I = makeIdentityMat(len(matA))
    matA , result = pivoting(matA, result)
    matA, result = makeUpperTriangular(matA, result)
    calcAnswer(matA, result)
    # printMat(matA)
    # print(result)

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

def pivoting(matA, result = None):
    # find max pivot in each column
    n = len(matA)
    for i in range(n):
        for j in range(i,n):
            if abs(matA[j][i]) > abs(matA[i][i]):
                matA[i], matA[j] = matA[j],matA[i]
                if result != None: 
                    result[i], result[j] = result[j], result[i]
    return (matA, result)

def printMat(mat):
    for row in mat:
            print(row)

# _______________________________________________________________


Q = [[1, 3, 5, 9],
     [1, 3, 1, 7],
     [4, 3, 9, 7],
     [5, 2, 0, 9]]

A = [[11, 13, 7],
     [16.5, 12, 3],
     [13, 20, 9]]

B = [[4],[3],[2]]

S = [[1, 3, 2],
     [2, 6, 4],
     [1, 0, 3]]

LU(A, B)
# print(matMultiply(A, B))
# print(calcMat(A, B))
# print(detCalculator(A))
