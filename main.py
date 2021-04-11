def matMultiply(A, B):
    # multiply from the left: A * B.
    result = []
    for i in range(len(A)):
        rowMat = []
        for j in range(len(B[i])):
            index = 0
            for k in range(len(B)):
                index += A[i][k] * B[k][j]
            rowMat.append(index)
        result.append(rowMat)
    return result

def determinant(A):
    sum = 0
    matLen = len(A)
    currentRow = 0
    # will calculate det of first row
    # We assume that its a square matrix
    for index in range(matLen):
        newMat = []
        currentCol = index
        for i in range(matLen):
            newMatRow = []
            for j in range(matLen):
                if i != currentRow and j != currentCol:
                    newMatRow.append(A[i][j])
            if len(newMatRow) > 0:
                newMat.append(newMatRow)
        if len(newMat) != 2:
            pivot = A[currentRow][currentCol]
            if index % 2 != 0:
                pivot *= -1
            sum += pivot * determinant(newMat)
        else: 
            pivot = A[currentRow][currentCol]
            if currentCol % 2 != 0:
                pivot *= -1
            sum += pivot * detCalculator(newMat)
    return sum

def detCalculator(A):
    if len(A) != 2:
        return None
    else:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

def makeIdentityMat(dimension):
    # Works for square matrix only
    identityMat = [] 
    for i in range(dimension):
        rowMat = []
        for j in range(dimension):
            if i == j: rowMat.append(1)
            else: rowMat.append(0)
        identityMat.append(rowMat)
    return identityMat

def makeUpperTriangular(A):
    dimension = len(A)
    for i in range(dimension):
        for j in range(i + 1):
            # print("[", i, "]", " [", j, "]")
            if i == j:
               A = makePivotOne(i, A)
            else:
                A = makePivotZero(i, j, A)
    return A

def makePivotZero(i, j, A):
    if A[j][j] == 0:
        return A
    I = makeIdentityMat(len(A))
    I[i][j] = -A[i][j] / A[j][j]
    return matMultiply(I, A)

def makePivotOne(i, A):
    if A[i][i] == 0:
        return A
    I = makeIdentityMat(len(A))
    I[i][i] = 1 / A[i][i]
    return matMultiply(I, A)

def gaussianElimination(A):
    A = makeUpperTriangular(A)
    return A


def calcMat(A):
    if len(A) < 4:
        return gaussianElimination(A)
    else: 
        print("Use Lu") 

# _______________________________________________________________

Q = [[1,3,5,9], 
     [1,3,1,7],
     [4,3,9,7],
     [5,2,0,9]]

Z = [[11,3,7],
     [6.5,12,13],
     [0,0,9]]

print(calcMat(Z))