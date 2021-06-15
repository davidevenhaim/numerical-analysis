import sympy as sp
import numpy as np
import math
x = sp.symbols("x")

METHODS = ["Bisection", "Newton Raphson", "Secant"]
EPSILION = 0.0001
SECTION = 0.1


def derivatie(f, x):
    fTag = sp.diff(f, x)
    return sp.lambdify(x, fTag)


def Bisection_Method(f, a, b, epsilion=EPSILION):
    maxIter = -(np.log(epsilion / (b - a))) / np.log(2)
    iterations = 0
    while (b - a) > epsilion:
        if iterations > maxIter:
            print("Max iterations limit.")
            return None
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        iterations += 1
    return [c, iterations]


def Newton_Raphson(f, fTag, a, b, epsilion=EPSILION):
    x0 = (a + b) / 2
    x1 = a
    iteration = 0
    while abs(x1-x0) > epsilion:
        if fTag(x0) == 0:
            print("cant divide by zero")
            break
        temp = x1
        x1 = x0-(f(x0)/fTag(x0))
        x0 = temp
        iteration += 1
    return [x1, iteration]


def secant_method(f, a, b, epsilion=EPSILION):
    x2 = (a + b) / 2
    x1 = b
    x0 = a
    iteration = 0
    while abs(x2 - x1) > epsilion:
        if f(x1) - f(x0) == 0:
            return None
        temp = x2
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = temp
        iteration += 1
    return [x1, iteration]


def find_suspect_point(f, pStart, pEnd, section=SECTION):
    x = pStart + section
    i = 0
    while x < pEnd:
        # i += 1
        # print("Iteration number: ", i, " ---- x = ", x, " --- f(x) = ", f(x))
        if (f(x) * f(x - section)) < 0:
            return x - section, x, i
        x += section
    return False


def start_calc(f, fTag, pStart, pEnd, method, section=SECTION, epsilion=EPSILION):
    fx = sp.lambdify(x, f)
    fTagx = sp.lambdify(x, fTag)
    answers = []
    methodName = METHODS[method-1]
    root = []
    # every root contain: [value, iterations till value reached]

    area = find_suspect_point(fx, pStart, pEnd, section)

    while area:
        if method == 1:
            root = (Bisection_Method(fx, area[0], area[1], epsilion))
        if method == 2:
            root = Newton_Raphson(fx, fTagx, area[0], area[1], epsilion)
        if method == 3:
            root = secant_method(fx, area[0], area[1], epsilion)
        if root is not None:
            root[1] += area[2]
            answers.append(root)
        area = find_suspect_point(fx, area[1], pEnd, section)

    # using the derivative
    area = find_suspect_point(fTagx, pStart, pEnd, section)
    while area:
        if method == 1:
            root = (Bisection_Method(fTagx, area[0], area[1], epsilion))
        if method == 2:
            root = Newton_Raphson(fTagx, derivatie(fTag, x), area[0], area[1], epsilion)
        if method == 3:
            root = secant_method(fTagx, area[0], area[1], epsilion)
        if root is not None:
            if abs(fx(root[0])) < epsilion:
                root[1] += area[2]
                answers.append((abs(root[0]), root[1]))
        area = find_suspect_point(fTagx, area[1], pEnd, section)

    print("\n_________________")
    print("Using", methodName, "method:")
    for i in range(len(answers)):
        print("The", i + 1, "root is:", "%.3f" % answers[i][0], "\nThe number of iterations to find the answer are:", answers[i][1])
    print("_________________ \n")


def main():
    f = x ** 4 + x ** 3 - 3 * x ** 2
    f2 = math.sin(x ** 4 + 5 * x - 6) / 2 * math.exp() ** -2 * x + 5
    fTag = sp.diff(f, x)
    f2Tag = sp.diff(f2, x)
    pStart = -2.5
    pEnd = 1.9

    while True:
        method = int(input(
        "What is the method you want to use:\n" +
        "1. Bisection method\n" +
        "2. Newton Rapshon method\n" +
        "3. Secant method\n" +
        "4. Exit\n"))

        if method == 4:
            print("Good day")
            break
        start_calc(f2, f2Tag, pStart, pEnd, method)



main()
