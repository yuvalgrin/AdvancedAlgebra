from algo.BSGS import baby_step_giant_step
from algo.generator_creation import find_generator_for_field
from models.finite_field import FiniteField


def main():
    print("Authors: Benjamin, Ron, and Yuval")

    # Create the respective data structures
    p = 7
    irreducible_polynom = [3, 6, 1]
    finite_field = FiniteField(p, irreducible_polynom)

    # Find a generator element in the field
    generator_element = find_generator_for_field(finite_field)

    # Run the baby step giant step algorithm to get the result
    t = 40 % finite_field.p
    exp_element = generator_element ** t
    bsgs = baby_step_giant_step(generator_element, exp_element)
    print(f"BSGS result: {bsgs}")
    assert bsgs == t


if __name__ == "__main__":
    main()
