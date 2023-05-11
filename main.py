from algo.BSGS import baby_step_giant_step
from algo.generator_creation import find_generator_for_field
from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement, get_e0_element, get_e1_element
from models.prime_field_element import PrimeFieldElement


def main():
    print("Authors: Benjamin, Ron, and Yuval")

    # Create the respective data structures:

    # Here we create a prime field element 2 from the prime field of 23
    prime_element = PrimeFieldElement(2,23)
    print(f"You have create the prime field element {prime_element}")
    # we exponentiate 2^9 mod 23 and get
    print(f"We can exponentiate by 9 and get 2^9={prime_element ** 9}")
    # Here we create an extended field for prime field (p=7) by using a second order irreducible polynomial
    # with coefficients (3,6,1)
    p = 7
    irreducible_polynom = [3, 6, 1]
    finite_field = FiniteField(p, irreducible_polynom)

    # Creating the element (4,5) from the field
    finite_field_element = FiniteFieldElement(finite_field, [4, 5])
    print(f"You have created the element {finite_field_element}")
    #You can print it as a vector by
    print(f"You have created the element (vector form) {finite_field_element.coeffs}")
    # You can print it as a matrix by
    print("You have created the element (matrix representation):")
    print(finite_field_element.embed_in_GLn())

    # Find the order of an element (for the multiplicative group, l-{0})
    my_element_order = finite_field_element.get_multiplicative_order()
    print(f"The order of your chosen element is {my_element_order}")

    # Find a generator (for the multiplicative group, l-{0}) element in the field
    generator_element = find_generator_for_field(finite_field)
    print(f"The generator that was found is: {generator_element}")

    # BSGS:
    # Our element "finite_field_element" can be produced by exponentiating a generator to the appropriate power,
    # such that for some integer value "t" exists  finite_field_element = generator_element^t.
    # Suppose we wish to find the number "t" for which we can reach our element, to do so we may use the Baby Step Giant Step (BSGS) algorithm.
    # Here is an example, using the element and generator we have.

    t = baby_step_giant_step(generator_element, finite_field_element)
    print(f"The exponent power t={t}, for which finite_field_element = generator_element^t")




if __name__ == "__main__":
    main()
