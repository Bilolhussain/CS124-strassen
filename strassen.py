from test_functions import generate_matrix, printmatrix, strassen, matrixmultiply
import datetime
import random
import sys

def main():
    flag = int(sys.argv[1])
    d = int(sys.argv[2])
    filename = sys.argv[3]

    # get file
    f = open(filename)

    m1 = generate_matrix(d)
    m2 = generate_matrix(d)

    # populate matrices
    i = 0
    j = 0
    for row in f:
        if i < d:
            m1[i][j] = int(row.strip())
        else:
            m2[i-d][j] = int(row.strip())
        j += 1
        if j > d-1:
            j = 0
            i += 1

    product = strassen(m1, m2, 35)
    print("MATRIX PRODUCT:")
    printmatrix(product)

if __name__ == "__main__":
    main()
