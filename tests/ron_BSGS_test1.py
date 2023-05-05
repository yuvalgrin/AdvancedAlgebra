from models.finite_field import *
from models.finite_field_element import *
from utils.prime_utils import is_prime
from models.prime_field_element import PrimeFieldElement
from models.prime_field_element import *
from itertools import product
import math
import time
import numpy as np

def generate_set_of_extended_field_elements(MyField):
    # Evaluating the order of the polynomial
    n = len(MyField.f)-1
    # The prime number of our initial field
    p = MyField.p
    prime_field_elements = [PrimeFieldElement(i, p) for i in range(p)]
    # Generate all possible combinations of n elements taken from prime_field_elements
    MyLists = list(product(prime_field_elements, repeat=n))
    my_set_of_field_elements=set()
    for coeffs in MyLists:
        newfield = FiniteFieldElement(MyField, coeffs)
        my_set_of_field_elements.add(newfield)
    return my_set_of_field_elements
#
def generate_e0(MyField):
    polyorder = len(MyField.f)-1
    my_list = [0] * (polyorder)
    MyFieldElement = FiniteFieldElement(MyField, my_list)
    result = MyFieldElement
    return result
#
def generate_e1(MyField):
      polyorder = len(MyField.f)-1
      my_list = [1] + [0] * (polyorder - 1)
      MyFieldElement = FiniteFieldElement(MyField, my_list)
      result = MyFieldElement
      return result
#
def MyFiniteElementOrder(MyFieldElement):
    MyField = MyFieldElement.field
    e0 = generate_e0(MyField)
    if e0 == MyFieldElement:
        raise Exception('You entered the zero element. Please enter a valid element')
    o=1
    n = len(MyField.f)-1
    p = MyField.p
    L = p ** n -1
    FloorL = L // 2
    e1 = generate_e1(MyField)
    a = MyFieldElement
    while o <= FloorL:
         if a == e1:
             return o
         else:
             o = o+1
             a = a * MyFieldElement
    o=L
    return o
#
def MyFiniteElementGenerator(MyField):
    n = len(MyField.f) - 1
    p = MyField.p
    L = p ** n - 1
    FloorL = L // 2
    e0 = generate_e0(MyField)
    e1 = generate_e1(MyField)
    MySet = generate_set_of_extended_field_elements(MyField)
    MySet.discard(e0)
    MySet.discard(e1)
    while len(MySet) > 1:
        element = MySet.pop()
        a = element
        o = 1
        while a != e1:
            o = o + 1
            a = a * element
            MySet.discard(a)
            if o > FloorL:
                return element
    return MySet.pop()

def TimeMyFunction(func, *arg):
    start = time.time()
    func(*arg)
    end = time.time()
    time_elapsed = end - start
    return time_elapsed








def main():
    print("Benjamin, Ron, and Yuval")
# my_field = FiniteField(3, [1, 0, 1])
my_field = FiniteField(7, [3, 6, 1])
# my_field = FiniteField(383, [378, 1, 0, 1])
# my_field = FiniteField(47, [42 , 3, 0, 1])
# my_field = FiniteField(97, [92 , 9, 0, 1])
my_element1 = FiniteFieldElement(my_field, [0,1])
my_element2 = FiniteFieldElement(my_field, [1, 1])
my_element3 = FiniteFieldElement(my_field, [5, 3])
# start = time.time()
# MyGen = MyFiniteElementGenerator(my_field)
# print(f"My generator is {MyGen}")
# MyGen2 = MyGen * MyGen
# MyGen3 = MyGen2 * my_element3
my_set_of_elements = generate_set_of_extended_field_elements(my_field)
my_random_element = my_set_of_elements.pop()
# print(my_element1 ** 1)
print(f"My random element {my_random_element}" )
print(f"My random element to the power of 1 {my_random_element ** 1}" )
my_rand_squared = my_random_element * my_random_element
print(f"My random element squared {my_rand_squared}")
my_rand_cubed = my_rand_squared * my_random_element
print(f"My random element cubed {my_rand_cubed}")
my_rand_inverse = my_random_element ** (-1)
print(f"My random element inverse {my_rand_inverse}" )
print(f"My random element inverse multiplied by my random element {my_rand_inverse * my_random_element}" )
print(f"My random element divided by my random element {my_random_element / my_random_element}" )
# print(f"Order of myelement1 {MyFiniteElementOrder(my_element1)}")
# print(my_element1 ** 3)
# MyExp = MyGen ** 2
# print(MyGen2.coeffs)
# print(MyExp.coeffs)
# end = time.time()
# elapsed_time  = end - start
# print("my generator is")
# print(MyGen)
# print(f"The time elapsed for finding the generator is {elapsed_time}")
# print("To test it, let us evaluate the order of my generator")
# start = time.time()
# print(MyFiniteElementOrder(MyGen))
# end = time.time()
# elapsed_time  = TimeMyFunction(MyFiniteElementOrder,MyGen)
# print(f"The time elapsed for verifying the generator is {elapsed_time}")
# elapsed_time = TimeMyFunction(generate_set_of_extended_field_elements,my_field)
# print(f"The time elapsed for running the function is {elapsed_time}")







if __name__ == "__main__":
    main()