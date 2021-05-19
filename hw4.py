import sympy as sp


x = sp.symbols("x")


def Bisection_Method(f, fTag, pStart, pEnd, section=0.1, epsilion=0.00000000001):
    range = findSuspectPoint(f, pStart, pEnd, section)
    answers = []
    while range:
        # pStart = range[1]
        answers.append(bisection(f, range[0], range[1], epsilion))
        range = findSuspectPoint(f, range[1], pEnd, section)

    range = findSuspectPoint(fTag, pStart, pEnd, section)
    while range:
        pStart = range[1]
        c = (bisection(fTag, range[0], range[1], epsilion))
        print("c is: ", c)
        if abs(f(c)) < epsilion:
            answers.append(c)
        range = findSuspectPoint(fTag, pStart, pEnd, section)
    print(answers)


def bisection(f, a, b, epsilion):
    i = 0
    while (b - a) > epsilion:
        i += 1
        c = (a + b) / 2
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        # print("Iteration number: ", i, "f(a) = ", f(a), " ---- f(b) = ", f(b), " ---- f(c) = ", f(c), " ---- a = ", a, " ----- b = ", b, " ---- c = ", c)
    return c


def Newton_Raphson(f, fTag, pStart, pEnd, section=0.1, epsilion=0.0001):
    print("I said good day")


def secant_method(f, fTag, pStart, pEnd, section=0.1, epsilion=0.0001):
    print("good day")


def findSuspectPoint(f, pStart, pEnd, section):
    x = pStart + section
    while x < pEnd:
        if (f(x) * f(x - section)) < 0:
            return x - section, x
        x += section
    return False




def main():
    polinom = x**4+x**3-3*x**2
    derivative = sp.diff(polinom, x)
    derivative = sp.lambdify(x, derivative)
    polinom = sp.lambdify(x, polinom)
    pStart = -2.5
    pEnd = 1.9

    # print(polinom(1))
    # print(derivative)


    Bisection_Method(polinom, derivative, pStart, pEnd)

    while True:
        choice = int(input(
        "What is the method you want to use:\n" +
        "1. Bisection method\n" +
        "2. Newton Rapshon method\n" +
        "3. Secant method\n" +
        "4. Exit\n"))

        if choice == 1:
            Bisection_Method(polinom, pStart, pEnd)
        if choice == 2:
            Newton_Raphson(polinom, pStart, pEnd)
        if choice == 3:
            secant_method(polinom, pStart, pEnd)
        if choice == 4:
            print("Bye")
            break


main()