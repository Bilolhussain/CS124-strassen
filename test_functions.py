import random
import datetime
import math
  
def generate_matrix(d):
  d = int(d)
  return [[0]*d]*d
        

def populate_matrix(x):
  d = len(x)
  random.seed(datetime.datetime.now())
  for i in range(d):
    for j in range(d):
      x[i][j] = random.randint(0, 2) - 1

  return x

        
# conventional matrix mult
def matrixmultiply(m1, m2):
    product = generate_matrix(len(m1))
        # assume same dimension
        if (len(m1) != len(m2)):
            print("attempted to multiply matrices of different dimensions")
            return
        for row in range(len(m1)):
            for col in range(len(m1)):
                dot_pd = 0
                for k in range(len(m2)):
                    dot_pd += m1[row][k]*m2[k][col]
                product[row][col] = dot_pd
        return product

# multiply with strassen's algorithm and a threshold n for regular multiplication
def strassen(m1, m2, n):
        # print(len(m1))
        orig = len(m1)
        # if dimensions are at or below n, we use regular multiplication
        if orig <= n:
            return matrixmultiply(m1, m2)
          
        padded = False
        # pad if necessary
        if orig % 2 != 0:
            pad(m1)
            pad(m2)
            padded = True
        # subdivide each matrix into 4 matrices
        half = int(len(m1)/2)
        whole = int(len(m1))

        # divide matrix into four pieces:
        # allocate memory
        l = len(m1)
        q1 = generate_matrix(l/2)
        q2 = generate_matrix(l / 2)
        q3 = generate_matrix(l / 2)
        q4 = generate_matrix(l/2)
        q5 = generate_matrix(l/2)
        q6 = generate_matrix(l/2)
        q7 = generate_matrix(l / 2)
        q8 = generate_matrix(l / 2)
        # populate quarters
        for i in range(0, half):
            for j in range(0, half):
                q1[i][j] = m1[i][j]
                q2[i][j] = m1[i][j+half]
                q3[i][j] = m1[i+half][j]
                q4[i][j] = m1[i+half][j+half]
                q5[i][j] = m2[i][j]
                q6[i][j] = m2[i][j+half]
                q7[i][j] = m2[i+half][j]
                q8[i][j] = m2[i+half][j+half]

        # calculate products
        p1 = strassen(q1, subtract(q6, q8), n)
        p2 = strassen(add(q1, q2), q8, n)
        p3 = strassen(add(q3, q4), q5, n)
        p4 = strassen(q4, subtract(q7, q5), n)
        p5 = strassen(add(q1, q4), add(q5, q8), n)
        p6 = strassen(subtract(q2, q4), add(q7, q8), n)
        p7 = strassen(subtract(q1, q3), add(q5, q6), n)

        # calculate the quarters of result matrix
        pq1 = subtract(add(add(p6, p5), p4), p2)
        pq2 = add(p1, p2)
        pq3 = add(p3, p4)
        pq4 = subtract(subtract(add(p1, p5), p3), p7)

        del p1, p2, p3, p4, p5, p6, p7

        res = generate_matrix(len(m1))

        for i in range(half):
            for j in range(half):
                res[i][j] = pq1[i][j]
                res[i][j + half] = pq2[i][j]
                res[i + half][j] = pq3[i][j]
                res[i + half][j + half] = pq4[i][j]

        # print("matrix before unpadding:")
        # printmatrix(res)
        # unpad
        if padded:
            unpad(m1)
            unpad(m2)
        return [res[i][:orig] for i in range(orig)]

    # padding as we go along


def pad(m):
        l = len(m)
        for i in range(l):
            m[i] = m[i] + [0]
        row = [0] * (l + 1)
        m.insert(l, [0] * (l + 1))

    # undo padding when final matrix product is calculated

def unpad(m):
        l = len(m)
        for i in range(l):
            m[i] = m[i][:l-1]
        # m = m[:len(m)-1]
        del m[-1]

    # pretty prints a matrix


def printmatrix(m):
        l = len(m)
        for i in range(l):
            print(m[i])
        print("\n")


def add(m1, m2):
        l = len(m1)
        # assume same dimension
        if (l != len(m2)):
            print("attempted to add matrices of different dimensions")
            printmatrix(m1)
            printmatrix(m2)
            return
        summed = generate_matrix(l)
        for i in range(l):
            row = zip(m1[i], m2[i])
            summed[i] = [x + y for x, y in row]
        return summed

    # subtracts m2 from m1


def subtract(m1, m2):
        l = len(m1)
        # assume same dimension
        if (l != len(m2)):
            print("attempted to subtract matrices of different dimensions")
            return
        summed = generate_matrix(l)
        for i in range(l):
            row = zip(m1[i], m2[i])
            summed[i] = [x - y for x, y in row]
        return summed

    
