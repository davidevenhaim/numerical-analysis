def Bisection_Method(polinom, startPoint, endPoint, epsilion = 0.0001):
    print("")


def Newton_Raphson(polinom, startPoint, endPoint, epsilion = 0.0001):
    print("")


def secant_method(polinom, startPoint, endPoint, epsilion = 0.0001):
    print("")


def main():
    polinom = ""
    startPoint = ""
    endPoint = ""
    section = 0.1

    while True:
        choice = int(input("""What is the method you want to use:\n
                            1. Bisection method\n
                            2. Newton Rapshon method\n
                            3. Secant method\n
                            4. Exit
                            """))
        if choice == 1:
            Bisection_Method(polinom, startPoint, endPoint)
        if choice == 2:
            Newton_Raphson(polinom, startPoint, endPoint)
        if choice == 3:
            secant_method(polinom, startPoint, endPoint)
        if choice == 4:
            break
            