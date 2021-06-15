from sympy import true


def linear_interpolation(thePoints, findPoint):
    for row in range(len(thePoints) - 1):
        if (findPoint > thePoints[row][0]) and findPoint < thePoints[row + 1][0]:
            x1 = thePoints[row][0]
            x2 = thePoints[row + 1][0]
            y1 = thePoints[row][1]
            y2 = thePoints[row + 1][1]
            return (((y1 - y2) / (x1 - x2)) * findPoint) + ((y2 * x1 - y1 * x2) / (x1 - x2))


def matrix_multiply(matA, matB):
    rowsA = len(matA)
    colsA = len(matA[0])
    rowsB = len(matB)
    colsB = len(matB[0])
    if colsA != rowsB:
        print('The columns number of matrix-A must be equal to rows  number of matrix-B')
    resMat = []
    while len(resMat) < rowsA:
        resMat.append([])
        while len(resMat[-1]) < colsB:
            resMat[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matA[i][k] * matB[k][j]
            resMat[i][j] = total
    return resMat


def polynomial_interpolation(thePoints, findPoint):
    mat = list(range(len(thePoints)))
    for i in range(len(mat)):
        mat[i] = list(range(len(mat)))

    for row in range(len(thePoints)):
        mat[row][0] = 1
    for row in range(len(thePoints)):
        for col in range(1, len(thePoints)):
            mat[row][col] = pow(thePoints[row][0], col)
    resMat = list(range(len(thePoints)))
    for i in range(len(resMat)):
        resMat[i] = list(range(1))
    for row in range(len(resMat)):
        resMat[row][0] = thePoints[row][1]
    vectorA = matrix_multiply(inverse_matrix(mat), resMat)
    sum_ = 0
    for i in range(len(vectorA)):
        if i == 0:
            sum_ = vectorA[i][0]
        else:
            sum_ += vectorA[i][0] * findPoint ** i
    return sum_


def create_unit(matrix):

    identityMat = list(range(len(matrix)))
    for i in range(len(identityMat)):
        identityMat[i] = list(range(len(identityMat)))

    for i in range(len(identityMat)):
        for j in range(len(identityMat[i])):
            identityMat[i][j] = 0.0

    for i in range(len(identityMat)):
        identityMat[i][i] = 1.0
    return identityMat


def inverse_matrix(matrix):
    newMat = create_unit(matrix)
    count = 0
    flag = False
    while count <= len(matrix) and not flag:
        if matrix[count][0] != 0:
            flag = True
        count = count + 1
    if not flag:
        print("Error!")
    else:
        temp = matrix[count - 1]
        matrix[count - 1] = matrix[0]
        matrix[0] = temp
        temp = newMat[count - 1]
        newMat[count - 1] = newMat[0]
        newMat[0] = temp

        for x in range(len(matrix)):
            div = matrix[x][x]
            if div == 0:
                div = 1
            for i in range(len(matrix)):
                matrix[x][i] = matrix[x][i] / div
                newMat[x][i] = newMat[x][i] / div
            for row in range(len(matrix)):
                if row != x:
                    div = matrix[row][x]
                    for i in range(len(matrix)):
                        matrix[row][i] = matrix[row][i] - div * matrix[x][i]
                        newMat[row][i] = newMat[row][i] - div * newMat[x][i]
    return newMat


def lagrange_interpolation(thePoints, findPoint):
    sum_ = 0
    for i in range(len(thePoints)):
        mul = 1
        for j in range(len(thePoints)):
            if i == j:
                continue
            mul = mul * ((findPoint - thePoints[j][0]) / (thePoints[i][0] - thePoints[j][0]))
        sum_ = sum_ + mul * thePoints[i][1]
    return sum_


def P(m, n, thePoints, findPoint):
    if m == n:
        return thePoints[m][1]
    resP = ((findPoint - thePoints[m][0]) * P(m + 1, n, thePoints, findPoint) - (findPoint - thePoints[n][0]) *
            P(m, n - 1, thePoints, findPoint)) \
        / (thePoints[n][0] - thePoints[m][0])

    return resP


def neville_interpolation(thePoints, findPoint):
    resMat = list(range(len(thePoints)))
    for k in range(len(thePoints)):
        resMat[k] = list(range(len(thePoints)))

    for i in range(len(thePoints)):
        for j in range(i, len(thePoints)):
            resMat[i][j] = P(i, j, thePoints, findPoint)
    return resMat[0][len(thePoints) - 1]


def main():
    while true:
        user_choice = int((input("\nPlease choose one option:\n"
                                 "1. Linear Interpolation\n"
                                 "2. Polynomial Interpolation\n"
                                 "3. Lagrange Interpolation\n"
                                 "4. Neville Interpolation\n"
                                 "5.Exit\n"
                                )))

        if user_choice == 5:
            print("Bye.")
            break

        given_points = [[1, 0.7651], [1.3, 0.62], [1.6, 0.4554], [1.9, 0.2818], [2.2, 0.1103]]
        val_point = 1.5
        print("________________________________________")
        print('The points are:', given_points)
        print('The point:', val_point)

        if user_choice == 1:
            print("Using the Linear Interpolation method:")
            print('The value of point is: ', "%.4f" % linear_interpolation(given_points, val_point))

        elif user_choice == 2:
            print("Polynomial Interpolation")
            print('The value of point is: ', "%.4f" % polynomial_interpolation(given_points, val_point))

        elif user_choice == 3:
            print("Lagrange Interpolation")
            print('The value of point is: ', "%.4f" % lagrange_interpolation(given_points, val_point))

        elif user_choice == 4:
            print("Neville Interpolation")
            print('The value of point is: ', "%.4f" % neville_interpolation(given_points, val_point))

        else:
            print("Please enter a number between 1-5 only.\nPress 5 to exit.")

        print("________________________________________\n\n")


main()

