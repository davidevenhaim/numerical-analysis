def calcAnswer(matA, result):
    n = len(matA)
    vector = [0] * n
    vector[n-1] = result[n-1][0]
    for i in range(n - 2 , -1, -1):
        vector[i] = result[i][0]
        for j in range(n - 1, i , -1):
            if matA[i][j] != 0:
                vector[i] -= matA[i][j] * vector[j]
        vector[i] /= matA[i][i]
    return vector

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
            sum += pivot * detCalculator(newMat)
        return sum

def elementryInverse(matA, i, j = None):
    if j is None:
        j = i
    if matA[i][j] != 1:
        matA[i][j] = -matA[i][j]
    return matA
    
def elementaryListMultiplicate(elementaryList, dim):
    X = makeIdentityMat(dim)
    for i in range(len(elementaryList)):
        X = matMultiply(X, elementaryList[i])
    return X

def gaussianElimination(matA, result):
    matA , result = pivoting(matA, result)
    matA, result = makeUpperTriangular(matA, result)
    return calcAnswer(matA, result)

def getElementaryList(matA, result):
    elementaryList = []
    dim = len(matA)
    for j in range(dim):
        for i in range(j):
            print("I is: ", i)
            print("J is: ", j)
            elementary = None
            if i != j:
                matA,elementary = makePivotZero(j, i, matA, result, True)
                elementaryList.append(elementary)
    return (matA, elementaryList)

def inverse(mat):
    inverseMat = makeIdentityMat(len(mat))
    matCopy = [x[:] for x in mat]
    dim = len(mat)
    # for row in range(dim):
        # if matCopy[row][row] == 0:
        #for column in range(dim):
    return 0

def LU(matA, result):
    dim = len(matA)
    U, elementaryList =  getElementaryList(matA, result)
    L = elementaryListMultiplicate(elementaryList, dim)
    print("U is:")
    printMat(U)
    print("L is:")
    printMat(L)

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

def makeUpperTriangular(matA, result):
    dim = len(matA)
    for i in range(dim):
        for j in range(i + 1):
            if i == j:
                matA, result = makePivotOne(i, matA, result)
            else:
                matA, result = makePivotZero(i, j, matA, result)
    return (matA, result)

def makePivotZero(i, j, matA, result, LU = False):
    if matA[j][j] == 0:
        return matA
    I = makeIdentityMat(len(matA))
    I[i][j] = -matA[i][j] / matA[j][j]
    if LU is True: 
        return (matMultiply(I, matA),elementryInverse(I, i, j))
    return (matMultiply(I, matA), matMultiply(I, result))

def makePivotOne(i, matA, result, LU = False):
    if matA[i][i] == 0:
        return matA
    I = makeIdentityMat(len(matA))
    I[i][i] = 1 / matA[i][i]
    if LU is True: 
        return elementryInverse(I, i)
    return (matMultiply(I, matA), matMultiply(I, result))

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
    if result!= None:
        return (matA, result)
    return matA
        
def printMat(mat):
    for row in mat:
            print(row)

def startMatrixCalculation(matA, result):
    if len(matA) < 4:
        return gaussianElimination(matA, result)
    else:
        return LU(matA, result)

# _______________________________________________________________

Q = [[1, 3, 5, 9],
     [1, 12, 1, 7],
     [4, 13, 9, 7],
     [5, 2, 3, 9]]

C = [[11],[5],[4], [13]]

print(startMatrixCalculation(Q, C))