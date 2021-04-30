def main():
    A = [[20, 3, 5, 9],
     [1, 12, 1, 7],
     [4, 13, 39, 7],
     [5, 1, 1, 9]]
    
    B = [[2, 1, 0],
         [4,6,1],
         [22,1,27]]

    options = {
        # should be functions instead.
        1: "Gauss Zaidel",
        2: "Jacboi"
    }
    # do-while Python implementation.
    while True:
        choice = int(input("What is your choice: \n 1. Gauss Zaidel \n 2.Jacobi"))
        if choice == 1 or choice == 2:
            break

    print(options[choice])
    print(dominantDiagonal(A))
    print(dominantDiagonal(B))

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


def changeRow(matA, rowA , rowB):
    elementaryMat = []
    for i in range(len(matA)):
        lineMat = []
        for j in range(len(matA[i])):
             # (-1) because i / j starts from 0 
            if i == rowA - 1:
                if j == rowB - 1:
                    lineMat.append(1)
                else: 
                    lineMat.append(0)
            elif i == rowB - 1:
                if j == rowA - 1:
                    lineMat.append(1)
                else:
                    lineMat.append(0)
            else: 
                if i == j:
                    lineMat.append(1)
                else:
                    lineMat.append(0)
        elementaryMat.append(lineMat)
    return matMultiply(elementaryMat, matA)

main()