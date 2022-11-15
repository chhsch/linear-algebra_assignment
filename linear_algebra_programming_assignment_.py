# -*- coding: utf-8 -*-
"""Linear Algebra Programming_assignment .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uPcmipid8Qtb11Vaks_l-77U2dHk7nGG
"""

import math
def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M

def identity_Matrix(n):
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0

    return IdM


def copy_matrix(M):
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MN = zeros_matrix(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MN[i][j] = M[i][j]

    return MN


def print_matrix(M, decimals=3):
    for row in M:
        print([round(x, decimals)+0 for x in row])


def transpose(M):
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0], list):
        M = [M]

    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros_matrix(cols, rows)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT


def matrix_addition(X, Y):
    # Section 1: Ensure dimensions are valid for matrix addition
    rowsX = len(X)
    colsX = len(X[0])
    rowsY = len(Y)
    colsY = len(Y[0])
    if rowsX != rowsY or colsX != colsY:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix sum
    Z = zeros_matrix(rowsX, colsY)

    # Section 3: Perform element by element sum
    for i in range(rowsX):
        for j in range(colsY):
            Z[i][j] = X[i][j] + Y[i][j]

    return Z


def matrix_subtraction(A, B):
    # Section 1: Ensure dimensions are valid for matrix subtraction
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    # Section 2: Create a new matrix for the matrix difference
    C = zeros_matrix(rowsA, colsB)

    # Section 3: Perform element by element subtraction
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C


def matrix_multiply(A, B):
    # Section 1: Ensure A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C




def check_matrix_equality(A, B, tol=None):
    # Section 1: First ensure matrices have same dimensions
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    # Section 2: Check element by element equality
    #            use tolerance if given
    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol is None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], tol) != round(B[i][j], tol):
                    return False

    return True








def check_squareness(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")
def check_non_singular(A):
    """
    Ensure matrix is NOT singular
        :param A: The matrix under consideration
        :return: determinant of A - nonzero is positive boolean
                  otherwise, raise ArithmeticError
    """



   
def determinant_fast(A):
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("MATRIX NOT INVERTIBLE")
                return -1
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a
def invert_martrix(A, tol=None):
    
    # Section 1: Make sure A can be inverted.
    check_squareness(A)
    check_non_singular(A)
 
    # Section 2: Make copies of A & I, AM & IM, to use for row ops
    n = len(A)
    AM = copy_matrix(A)
    I = identity_Matrix(n)
    IM = copy_matrix(I)
 
    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: 
            # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): 
                # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
 
    # Section 4: Make sure IM is an inverse of A with specified tolerance
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")

#第一題
A=[[2,-1],[3,5]]
B=[[-2,0],[4,2]]
C=[[-1,2,0],[2,0,3]]
D=[[2,0,-1],[1,-2,0]] 
k=[[2,0],[0,2]] 
print(matrix_addition(A, matrix_multiply(k,B)))
print(matrix_subtraction(C, D))
print(transpose(A))

#第二題
A=[[2,-1],[3,5]]
B=[[-2,0],[4,2]]
F=matrix_multiply(A, B)
G=matrix_multiply(B, A)
print(matrix_multiply(A, B))
print(matrix_multiply(B, A))
print(check_matrix_equality(F, G, tol=None))

#第三題
E=[[2,-1],[math.pi,math.log(2,10)],[-2,6]]
C=[[-1,2,0],[2,0,3]]
M=matrix_multiply(C, E)
N=matrix_multiply(E, C)
print(matrix_multiply(C, E))
print(matrix_multiply(E, C))
print(check_matrix_equality(M, N, tol=None))

#第四題
A=[[2,-1],[3,5]]
print(matrix_multiply(transpose(A), A))

#第五題
A=[[2,-1],[3,5]]
B=[[-2,0],[4,2]]
I=[[1,0],[0,1]]
F=matrix_multiply(A, B)
Q=matrix_multiply(A,invert_martrix(A, tol=1))
W=matrix_multiply(F,invert_martrix(F, tol=1))
print(invert_martrix(A, tol=1))
print(invert_martrix(F, tol=1))
print(Q)
print(W)
print(check_matrix_equality(Q,I, tol=1))
print(check_matrix_equality(W,I, tol=1))