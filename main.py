# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


A = [[1,3,5,9], 
     [1,3,1,7],
     [4,3,9,7],
     [5,2,0,9]]

X = [[1,2,3],
    [4 ,5,6]]

Y = [[7,8],
    [9,10],
    [11,12]]

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
    print(result)




def matReducer(A):
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
            sum += pivot * matReducer(newMat)
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

def makeUpperTriangular(A):
    print(A)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(matReducer(A))
    if matReducer(A) != 0:
        matMultiply(X,Y)
    else: print("Use LU")



