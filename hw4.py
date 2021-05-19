import sympy as sp


x = sp.symbols("x")

def Bisection_Method(f, pStart, pEnd, epsilion = 0.0001):
    print("Good day")


def Newton_Raphson(f, pStart, pEnd, epsilion = 0.0001):
    print("I said good day")


def secant_method(f, pStart, pEnd, epsilion = 0.0001):
    print("good day")

def findSuspectPoint(f, pStart, pEnd, section):
    x = pStart + section
    while x < pEnd:
        sign = (f(x - section) > 0)
        if (f(x) > 0) != sign:
            return x - section, x
        x += section




def main():
    polinom = x
    derivative = sp.diff(polinom, x)
    polinom = sp.lambdify(x, polinom)

    # print(polinom(1))
    # print(derivative)

    pStart = -2
    pEnd = 2
    section = 0.1

    print(findSuspectPoint(polinom, pStart, pEnd, section))

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