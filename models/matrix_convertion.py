import finite_field_element


#important note: the less significant bit in the implementaion of the polynoms is the most right one
#e.g: [1,0,0,2] = x^3 + 2
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det


import time
def polynom_mul(pol1,pol2):
    new_pol = [0 for i in range(len(pol1)+len(pol2)-1)]
    for idx1,i1 in enumerate(pol1):
        for idx2,i2 in enumerate(pol2):
            new_pol[idx1+idx2] += i1*i2
    return new_pol

def polynom_plus(pol1,pol2):
    new_pol = [0 for i in range(max(len(pol1),len(pol2)))]
    for idx, i in enumerate(pol2[-1::-1]):
        new_pol[-(idx+1)] += i
    print(new_pol)
    for idx, i in enumerate(pol1[-1::-1]):
        new_pol[-(idx + 1)] += i
    return new_pol

def polynom_minus(pol):
    return [-x for x in pol]

#substarction of to polynoms(uses the addition and minus operation)
def polynom_substract(pol1,pol2):
    return polynom_plus(pol1,polynom_minus(pol2))

print(polynom_mul([-1,4],[4,-6,5]))
print(polynom_plus([7,4,3],[4,9,-6,5]))
print(polynom_minus([4,9,-6,5]))
print(polynom_substract([7,4,3],[4,7,-6,3]))
print([7,4,3][1:])

#this function take care of the cases when we get a big polynom and we want to know
#what is its form as a n_dimensional vector, we reduce every x^n | n>r by
#looking at him like x^r*x^(n-r) and we know how to reduce x^r, so we
# get somthing like x^(n-r) * (-a_r*x^(r-1)-...- a_1*x -a_0)
def modulu_polynom(input_polynom,reduction_polynom):
    while len(input_polynom)>=len(reduction_polynom):
        reduction_amplifier = [input_polynom[0] if idx == 0 else 0 for idx,_ in enumerate(range(1+len(input_polynom)-len(reduction_polynom)))]
        input_polynom = polynom_substract(input_polynom,polynom_mul(reduction_amplifier,reduction_polynom[1:]))
        input_polynom = input_polynom[1:]
    return input_polynom

print(modulu_polynom([1,0,2,5],[1,1,3]))

def get_matrix(polynom,reduction_polynom):
    unity_matrix = [[1 if idx2 == idx1 else 0 for idx2 in range(len(reduction_polynom)-1)] for idx1 in range(len(reduction_polynom)-1)]
    almost_there = [modulu_polynom(polynom_mul(I,polynom),reduction_polynom) for I in unity_matrix]
    return np.int_(almost_there)

def exp(matrix,n):
    ret = np.identity(len(matrix))
    mat = matrix
    while n != 0:
        if n % 2 == 1:
            ret = np.matmul(mat,ret)
        mat = np.matmul(mat,mat)
        n = n>>1
    return ret

def inverse_matrix(mat,p):
    inverse = det(mat)*inv(mat)
    d = det(x)
    inverse = [[x/d for x in y] for y in inverse]
    return inverse

x = get_matrix([2,3],[1,0,1])
y = get_matrix([4,1],[1,0,1])
print(x)
#print(y)
#print(x*y)
print(exp(x.astype(int),13))
print((det(x)*inv(x)))
print(inverse_matrix(x,5))
d = {}
for i in range(5):
    d[5-i] = i
print(d.keys())

