## Advanced Algebra course project
Authors: Yuval Grinberg, Ron Cohen, Benjamin Ramati

### Project structure
- algo
  - algorithms and calculation logic like matrix embedding and BSGS
- models
  - data structure that represent the finite field and element
- utils
  - common util methods
- tests
  - unit tests that assert validity of the methods
- main: run examples

### How to use the code?
Create the respective data structures
```python
p = 7
irreducible_polynom = [3, 6, 1]
finite_field = FiniteField(p, irreducible_polynom)
```

Find a generator element in the field
```python
generator_element = find_generator_for_field(finite_field)
```

Run the baby step giant step algorithm to get the result
```python
t = 40 % finite_field.p
exp_element = gen ** t
bsgs = baby_step_giant_step(generator_element, exp_element)
assert bsgs == t
```

