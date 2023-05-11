## Advanced Algebra course project
Authors: Yuval Grinberg, Ron Cohen, Benjamin Ramati

### Project structure
- **algo**: algorithms and calculation logic like matrix embedding and BSGS
- **models**: data structure that represent the finite field and element
- **utils**: common util methods
- **tests**: unit tests that assert validity of the methods
- **main**: run examples

### How to use the code?
Create the respective data structures:
Here we create an extended field for prime field (p=7) by using a second order irreducible polynomial
with coefficients (3,6,1)
```python
p = 7
irreducible_polynom = [3, 6, 1] #It must be irreducible for prime field members (p=7)
finite_field = FiniteField(p, irreducible_polynom)
```
Creating the element (4,5) from the field
````python
finite_field_element = FiniteFieldElement(finite_field, [4, 5])
print(f"You have created the element {finite_field_element}")
````

Find the order of an element (for the multiplicative group, l-{0}) 
````python
my_element_order = finite_field_element.get_multiplicative_order()
print(f"The order of your chosen element is {my_element_order}")
````

Find a generator (for the multiplicative group, l-{0}) element in the field
```python
generator_element = find_generator_for_field(finite_field)
print(f"The generator that was found is: {generator_element}")
```

Our element "finite_field_element" can be produced by exponentiating a generator to the appropriate power,
such that for some integer value "t" exists  finite_field_element = generator_element^t.
Suppose we wish to find the number "t" for which we can reach our element, to do so we may use the Baby Step Giant Step (BSGS) algorithm.
Here is an example, using the element and generator we have.
```python
t = baby_step_giant_step(generator_element, finite_field_element)
print(f"The exponent power t={t}, for which finite_field_element = generator_element^t")
```

