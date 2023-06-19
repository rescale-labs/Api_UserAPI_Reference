import sys
import pickle
from decimal import Decimal
import math


def calculate_pi(max_range):
    """
    Estimate Pi using the Leibniz’s formula.
    """
    k = Decimal(1)
    s = Decimal(0)

    print("iteration\tvalue\tdiff")
    iter = 0
    for i in range(max_range):
        if i % 2 == 0:
            s += 4 / k
        else:
            s -= 4 / k
        k += 2

        iter += 1
        if iter % (max_range / 100) == 0:
            print(f"{iter}\t{s}\t{abs(s-Decimal(math.pi))}")
            sys.stdout.flush()

    return s


if __name__ == "__main__":
    with open(sys.argv[1], "r") as inp:
        max_range = int(float(inp.readline().strip()))

    print(f"Calculating PI for range:\t{max_range}")
    pi = calculate_pi(max_range)

    with open("pi_estimate.res", "w") as of:
        of.write(f"{pi}")
    with open("pi_estimate.bin", "wb") as of:
        pickle.dump(pi, of)

    print(f"Finial value of PI: {pi}")
