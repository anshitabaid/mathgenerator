from .__init__ import *


def dataSummaryFunc(number_values=15, minval=5, maxval=50):
    random_list = []

    for i in range(number_values):
        n = random.randint(minval, maxval)
        random_list.append(n)

    a = sum(random_list)
    mean = a / number_values

    var = 0
    for i in range(number_values):
        var += (random_list[i] - mean)**2

    # we're printing stuff here?
    print(random_list)
    print(mean)
    print(var / number_values)
    print((var / number_values)**0.5)

    problem = "Find the mean,standard deviation and variance for the data" + \
        str(random_list)
    solution = "The Mean is {} , Standard Deviation is {}, Variance is {}".format(
        mean, var / number_values, (var / number_values)**0.5)
    return problem, solution
