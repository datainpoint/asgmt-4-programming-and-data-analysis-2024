# asgmt-4-programming-and-data-analysis-2024

> Assignment 4: Programming and Data Analysis 2024.

- Define functions in `asgmt.py` given their names, templates, and docstrings.
- Run `test-runner.py` to validate your functions.
- Upload `asgmt.py` to [NTU COOL](https://cool.ntu.edu.tw).

## 01. Define a class `Pet` which instantiates objects with a attribute `species` and a method `make_sound()`.

```python
class Pet:
    """
    >>> dog = Pet('Dog', 'Bark')
    >>> dog.species
    'Dog'
    >>> dog.make_sound()
    'Bark'
    >>> kitty = Pet('Cat', 'Meow')
    >>> kitty.species
    'Cat'
    >>> kitty.make_sound()
    'Meow'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `Hogwarts` which instantiates objects with 3 attributes `location`, `founders`, and `houses`.

```python
class Hogwarts:
    """
    >>> hogwarts = Hogwarts()
    >>> hogwarts.location
    'Scotland'
    >>> hogwarts.founders
    ['Godric Gryffindor', 'Salazar Slytherin', 'Rowena Ravenclaw', 'Helga Hufflepuff']
    >>> hogwarts.houses
    ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class named `Gryffindor` which instantiates objects with 2 attributes `traits` and `colors`, a method `cast_a_spell()`.

```python
class Gryffindor:
    """
    >>> harry_potter = Gryffindor("Harry Potter")
    >>> harry_potter.name
    'Harry Potter'
    >>> harry_potter.traits
    ['courage', 'bravery', 'nerve', 'chivalry']
    >>> harry_potter.colors
    ['scarlet red', 'gold']
    >>> harry_potter.cast_a_spell()
    'Expelliarmus!'
    >>> hermione_granger = Gryffindor("Hermione Granger")
    >>> hermione_granger.name
    'Hermione Granger'
    >>> hermione_granger.traits
    ['courage', 'bravery', 'nerve', 'chivalry']
    >>> hermione_granger.colors
    ['scarlet red', 'gold']
    >>> hermione_granger.cast_a_spell()
    'Expelliarmus!'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `StrCase` which instantiates objects with 3 methods `upper_case()`, `lower_case()`, and `swap_case()`.

```python
class StrCase:
    """
    >>> luke = StrCase('Luke Skywalker')
    >>> luke.upper_case()
    'LUKE SKYWALKER'
    >>> luke.lower_case()
    'luke skywalker'
    >>> luke.swap_case()
    'lUKE sKYWALKER'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a class `MethodCalculator` which instantiates objects with 5 methods `add()`, `substract()`, `multiply()`, `divide()`, and `power()`.

```python
class MethodCalculator:
    """
    >>> method_calculator = MethodCalculator(10, 2)
    >>> method_calculator.add()
    12
    >>> method_calculator.subtract()
    8
    >>> method_calculator.multiply()
    20
    >>> method_calculator.divide()
    5.0
    >>> method_calculator.power()
    100
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a class `SymbolicCalculator` which instantiates objects with 1 method `calculate()`.

```python
class SymbolicCalculator:
    """
    >>> symbolic_calculator = SymbolicCalculator(10, 2)
    >>> symbolic_calculator.calculate('+')
    12
    >>> symbolic_calculator.calculate('-')
    8
    >>> symbolic_calculator.calculate('*')
    20
    >>> symbolic_calculator.calculate('/')
    5.0
    >>> symbolic_calculator.calculate('**')
    100
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a class `Reversible` which instantiates objects with a `reverse()` method that could take string, list, tuple, or dictionary as input.

```python
class Reversible:
    """
    >>> reversible = Reversible('Luke')
    >>> reversible.reverse()
    'ekuL'
    >>> reversible = Reversible([2, 5, 3, 7, 11])
    >>> reversible.reverse()
    [11, 7, 3, 5, 2]
    >>> reversible = Reversible((11, 7, 3, 5, 2))
    >>> reversible.reverse()
    (2, 5, 3, 7, 11)
    >>> reversible = Reversible({0: 'Sunday', 6: 'Saturday'})
    >>> reversible.reverse()
    {'Sunday': 0, 'Saturday': 6}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a class `SortList` which instantiates objects with 2 methods `sort_asc()` and `sort_desc()`.

```python
class SortList:
    """
    >>> sort_list = SortList([2, 5, 3, 7, 11])
    >>> sort_list.sort_desc()
    [11, 7, 5, 3, 2]
    >>> sort_list.sort_asc()
    [2, 3, 5, 7, 11]
    >>> sort_list = SortList(['p', 'y', 't', 'h', 'o', 'n'])
    >>> sort_list.sort_desc()
    ['y', 't', 'p', 'o', 'n', 'h']
    >>> sort_list.sort_asc()
    ['h', 'n', 'o', 'p', 't', 'y']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a class `WeekBuilder` which instantiates objects with a method `build()`.

```python
class WeekBuilder:
    """
    >>> week_builder = WeekBuilder(0, 1, 2)
    >>> week_builder.build()
    {0: 'Sunday', 1: 'Monday', 2: 'Tuesday'}
    >>> week_builder = WeekBuilder(5, 6)
    >>> week_builder.build()
    {5: 'Friday', 6: 'Saturday'}
    >>> week_builder = WeekBuilder(0, 6)
    >>> week_builder.build()
    {0: 'Sunday', 6: 'Saturday'}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a class `IsInstance` which instantiates objects with 5 methods `is_int()`, `is_float()`, `is_str()`, `is_bool()`, and `is_nonetype()`.

```python
class IsInstance:
    """
    >>> is_instance = IsInstance()
    >>> is_instance.is_int(5566)
    True
    >>> is_instance.is_float(3.14)
    True
    >>> is_instance.is_str('5566')
    True
    >>> is_instance.is_bool(False)
    True
    >>> is_instance.is_nonetype(None)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```