from .__init__ import *


def squareRootFunc(minNo=1, maxNo=12):
    b = random.randint(minNo, maxNo)
    a = b * b

    problem = "sqrt(" + str(a) + ")="
    solution = str(b)
    return problem, solution
