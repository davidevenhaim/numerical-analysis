# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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
        if currentCol % 2 != 0:
            pivot = -(A[currentRow][currentCol])
        else:
            pivot = A[currentRow][currentCol]
        sum += pivot * detCalculator(newMat)
    print(sum)


def detCalculator(A):
    if len(A) != 2:
        return None
    else:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matReducer(matrix3)


