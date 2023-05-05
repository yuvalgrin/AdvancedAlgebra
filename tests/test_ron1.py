from models.finite_field import *
from models.finite_field_element import *
from utils.prime_utils import is_prime
from models.prime_field_element import PrimeFieldElement
from models.prime_field_element import *
from itertools import product
import math
import numpy as np

def generate_extended_field_elements(MyField):
    # Generate a list of PrimeFieldElement objects
    n = len(MyField.f)-1
    p = MyField.p
    prime_field_elements = [PrimeFieldElement(i, p) for i in range(p)]
    # Generate all possible combinations of n elements taken from prime_field_elements
    #result = list(product(prime_field_elements, repeat=n))
    result = set(product(prime_field_elements, repeat=n))
    return result

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

# def generate_e0(p,n):
#     # result = [PrimeFieldElement(0, p) for i in range(n)]
#
#     # prime_field_elements = [PrimeFieldElement(i, p) for i in range(p)]
#     prime_field_elements = [PrimeFieldElement(0, p) for i in range(n)]
#     # Generate all possible combinations of n elements taken from prime_field_elements
#     # result = list(product(prime_field_elements, repeat=n))
#     result = set(product(prime_field_elements, repeat=n))
#     return result

# def generate_e1(p,n):
#     # result = [PrimeFieldElement(1, p)]+[PrimeFieldElement(0, p) for i in range(n-1)]
#     # result = [PrimeFieldElement(1, p)] + [PrimeFieldElement(0, p) for _ in range(p**n - 2)]
#     # prime_field_elements = [PrimeFieldElement(1, p)] + [PrimeFieldElement(0, p) for i in range(n-1)]
#     # result = set(product(prime_field_elements, repeat=n))
#
#     return set(result)

def generate_e0(MyField):
    polyorder = len(MyField.f)-1
    my_list = [0] * (polyorder)
    MyFieldElement = FiniteFieldElement(MyField, my_list)
    result = MyFieldElement
    return result

def generate_e1(MyField):
      polyorder = len(MyField.f)-1
      my_list = [1] + [0] * (polyorder - 1)
      MyFieldElement = FiniteFieldElement(MyField, my_list)
      result = MyFieldElement
      return result

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









def main():
    print("Benjamin, Ron, and Yuval")
# my_field = FiniteField(3, [1, 0, 1])
my_field = FiniteField(7, [3, 6, 1])
my_element1 = FiniteFieldElement(my_field, [0,1])
my_element2 = FiniteFieldElement(my_field, [1, 1])
my_e1 = generate_e1(my_field)
my_e0 = generate_e0(my_field)
MyFiniteFieldElements = set()
MyFiniteFieldElements.add(my_element2)
# MyFiniteFieldElements.add(my_e1)
MyFiniteFieldElements.add(my_e0)
my_set_of_elements = generate_set_of_extended_field_elements(my_field)
print(MyFiniteFieldElements)
if my_e0 in MyFiniteFieldElements:
    print("Yes, 'e0' is in this set")
else:
    print("No, 'e0' is not in this set")
MyGen = MyFiniteElementGenerator(my_field)
print("my generator is")
print(MyGen)
print("To test it, let us evaluate the order of my generator")
print(MyFiniteElementOrder(MyGen))
print("The number of elements in my set is {}".format(len(MyFiniteFieldElements)))
MyFiniteFieldElements.discard(my_e0)
if my_e0 in MyFiniteFieldElements:
    print("Yes, 'e0' is in this set")
else:
    print("No, 'e0' is not in this set")
print(MyFiniteFieldElements)
print(my_e0.field.p)
# print("The number of elements in my set is {}".format(len(MyFiniteFieldElements)))

# print(MyFiniteFieldElements.pop())
# print(my_element2)
# print(FiniteFieldElement(FiniteField(3, [1, 0, 1]), [1 (mod 3), 1 (mod 3)]))
# elementest = FiniteFieldElement(FiniteField(3, [1, 0, 1]), (1 (mod 3), 0 (mod 3)))
# elementest2 = FiniteFieldElement(FiniteField(3, [1, 0, 1]), [1 (mod 3), 2 (mod 3)])
# print(FiniteFieldElement(FiniteField(3, [1, 0, 1]), (1 (mod 3), 0 (mod 3))))
# element3 = FiniteFieldElement(FiniteField(3, [1, 0, 1]), [1 (mod 3), 2 (mod 3)])
# element4 = FiniteFieldElement(FiniteField(3, [1, 0, 1]), [1, 2])
# print(element4)
# print(my_set_of_element_names)
# my_set_of_element_names = generate_extended_field_elements(my_field)
# pop_element = FiniteFieldElement(my_field, my_set_of_element_names.pop())
# print(pop_element)
# print(my_set_of_elements)
# my_prime_field_element1 = PrimeFieldElement(2,7)
# my_prime_field_element2 = PrimeFieldElement(5,7)
# my_set_of_elements = set()
# my_set_of_elements.add(my_element1)
# print("my multiplicative unit element")
# print(my_e1)
# print("my additive unit element")
# print(my_e0)
#print(my_prime_field_element2*my_prime_field_element1)
#print(my_element2 * my_element1)
# print(my_element2 / my_element2)
# print(my_element1)
# print(my_element1.coeffs)
# print("printing the prime used in the field")
# print(my_field.p)
# print("printing the polynomial order")
# print(len(my_field.f)-1)
# print(my_field.f)
# myset1 = set()
# myset1.add(tuple(my_element1.coeffs))
# myset1.add(tuple(my_element2.coeffs))
# print(myset1)
# # print(myset1.pop())
# p = 3
# n = 2
# my_set_of_element_coeffs = generate_extended_field_elements(my_field)
# print(my_set_of_element_coeffs)
# print("removing e0 from my_set_of_element_coeffs ")
# my_set_of_element_coeffs.remove(tuple(my_e0.coeffs))
# print(my_set_of_element_coeffs)
# print("randomly picking up an element from the list")
# my_random_element = FiniteFieldElement(my_field, list(my_set_of_element_coeffs.pop()))
# print("printing that element")
# print(my_random_element)
# print("multiplying it by itself and getting")
# my_random_element = my_random_element * my_random_element
# print(my_random_element)
# print(my_random_element == my_e0)
# print("testing MyFiniteElementOrder with the identity")
# print(MyFiniteElementOrder(my_e1))
# print("testing MyFiniteElementOrder with my_random_element")
# print(MyFiniteElementOrder(my_random_element))
# print("checking again, my random element is")
# print(my_random_element.coeffs)
# print("Let us confirm that our generator is (1,1)")
# print(MyFiniteElementOrder(my_element2))
# print("Let us see if we get exception for e0")
# print(MyFiniteElementOrder(my_e0))
##
# print((my_random_element * my_random_element).coeffs)
# result = generate_prime_field_elements(p, n)
# print("printing the set for p=3 and n=2")
# print(result)
# print("The number of elements in a set is")
# print(len(result))
# print("poping an element from the set")
# print(result.pop())
# result1 = generate_extended_field_elements(p, n)
# result2 = generate_e0(p,n)
# result3 = generate_e1(p,n)
# print(result3)
# print("The number of elements in a set is")
# print(len(result3))
## Let us construct a function that recieves a finite field element, and outputs the order of the element
# -this function should then be implemented as a method in FiniteFieldElement








if __name__ == "__main__":
    main()