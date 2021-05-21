import copy

def main():
    A = [[2, 3, 5, 9],
     [1, 12, 1, 7],
     [4, 13, 39, 7],
     [5, 1, 1, 9]]
    
    B = [[4, 2, 0],
         [2, 10, 4],
         [0, 4, 5]]
    
    result = [[2], [6], [5]]

    result2= [[2], [6], [5], [8]]

    options = {
        # should be functions instead.
        1: lambda matA, result, epsilion = 0.00001: gaussZaidel(matA, result, epsilion),
        2: lambda matA, result, epsilion = 0.00001: jacobi(matA, result, epsilion),
    }
    # do-while Python implementation.
    while True:
        choice = int(input("What is your choice: \n 1. Gauss Zaidel \n 2.Jacobi\n"))
        if choice == 1 or choice == 2:
            break
    if(isDominantDiagonal(A)):
        options[choice](A,result2)
    else:
        # makeDominantDiagonal(A)
        print("Although the matrix has no dominant diagonal...")
        options[choice](A,result2)

    

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

def isDominantDiagonal(matA):
    for i in range(len(matA)):
        diagonalVal = 0
        lineVal = 0
        for j in range(len(matA[i])):
            if i != j:
                lineVal += abs(matA[i][j])
            else: 
                diagonalVal = matA[i][j]
        if diagonalVal < lineVal:
            return False
    return True

# def makeDominantDiagonal(matA):

def changeCol(matA, colA, colB):
    elementaryMat = buildElementary(matA, colA, colB)
    return matMultiply(matA, elementaryMat)

def changeRow(matA, rowA , rowB, result = None):
    elementaryMat = buildElementary(matA, rowA, rowB)
    if result != None:
        return (matMultiply(elementaryMat, matA), matMultiply(elementaryMat, result))
    return matMultiply(elementaryMat, matA)

def buildElementary(mat, a = None, b = None):
    # without a & b - Identity mat will be built.
    elementaryMat = []
    for i in range(len(mat)):
        lineMat = []
        for j in range(len(mat[i])):
             # (-1) because i / j starts from 0 
            if a is not None and i == a - 1:
                if j == b - 1:
                    lineMat.append(1)
                else: 
                    lineMat.append(0)
            elif b is not None and i == b - 1:
                if j == a - 1:
                    lineMat.append(1)
                else:
                    lineMat.append(0)
            else: 
                if i == j:
                    lineMat.append(1)
                else:
                    lineMat.append(0)
        elementaryMat.append(lineMat)
    return elementaryMat

def jacobi(matA, result, epsilion = 0.00001 ):
    R1 = []
    iteration = 0
    for i in range(len(matA)):
        R1.append([0])
    print("Jacobi Method:\n")
    while True:
        print("Iteration number: ", iteration, " results -> " , R1)
        iteration += 1
        R2 = copy.deepcopy(R1)
        for i in range(len(matA)):
            rowSum = 0
            for j in range(len(matA[i])):
                if j != i:
                    rowSum += matA[i][j] * R1[j][0]
            R2[i][0] = ((-rowSum + result[i][0]) / matA[i][i])
        if(checkDifference(R1, R2, epsilion)):
            break
        if(not checkDifference(R1, R2, iteration * 10)):
            print("The matirx has no dominant diagonal.")
            print("Jacobi will not give a proper answer!")
            break
        R1 = copy.deepcopy(R2)

def gaussZaidel(matA, result, epsilion = 0.00001):
    R1 = []
    iteration = 0
    for i in range(len(matA)):
        R1.append([0])
    print("Gauss-Zaidel Method:\n")
    while True:
        print("Iteration number: ", iteration, " results -> " , R1)
        iteration += 1
        R2 = copy.deepcopy(R1)
        for i in range(len(matA)):
            rowSum = 0
            for j in range(len(matA[i])):
                if j != i:
                    rowSum += matA[i][j] * R2[j][0]
            R2[i][0] = ((-rowSum + result[i][0]) / matA[i][i])
        if(checkDifference(R1, R2, epsilion)):
            break
        if(not checkDifference(R1, R2, iteration * 10)):
            print("The matirx has no dominant diagonal.")
            print("Gauss Zaidel will not give a proper answer!")
            break
        R1 = copy.deepcopy(R2)

def checkDifference(R1, R2, epsilion):
    for i in range(len(R1)):
        if abs(abs(R2[i][0]) - abs(R1[i][0])) > epsilion:
            return False
    return True

main()