    from datetime import datetime
    import sys
    from random import randint
    from strassen import *

    d = int(sys.arv[2])
    t = [15, 20, 25, 35, 45, 60, 90, 100]
    original_trials = 1
    trials = original_trials
    begin = datetime.datetime.now()

    while (trials > 0):
        m1 = populate_matrix(generate_matrix(d))
        m2 = populate_matrix(generate_matrix(d))
        print("MATRIX 1")
        printmatrix(m1)
        print("MATRIX 2")
        printmatrix(m2)
        product = strassen(m1, m2, t)
        print("MATRIX PRODUCT " + str(trials) + ":")
        printmatrix(product)
        trials -= 1

    end = datetime.datetime.now()
    time = end - begin
    print("dimension: " + str(d))
    print("threshold: " + str(t))
    print("trials: " + str(original_trials))
    print("total time: " + str(time))
    print("time per trial: " + str(time/original_trials))   