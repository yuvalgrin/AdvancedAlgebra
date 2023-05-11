from algo.BSGS import baby_step_giant_step
from algo.generator_creation import find_generator_for_field
from models.finite_field import FiniteField
from models.finite_field_element import FiniteFieldElement, get_e0_element, get_e1_element


def main():
    print("Authors: Benjamin, Ron, and Yuval")

    # Create the respective data structures:
    # Here we create an extended field for prime field (p=7) by using a second order irreducible polynomial
    # with coefficients (3,6,1)
    p = 7
    irreducible_polynom = [3, 6, 1]
    finite_field = FiniteField(p, irreducible_polynom)

    # Creating the element (4,5) from the field
    finite_field_element = FiniteFieldElement(finite_field, [4, 5])
    print(f"You have created the element {finite_field_element}")

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
