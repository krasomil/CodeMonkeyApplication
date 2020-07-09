# CodeMonkeyApplication

## Codebase location

[src](src)

### Working together

- Make sure to work in an indepentant branch
  
  `git branch featureName`

- Make sure commit messages are descriptive of the work done

- Feel free to ask for git help if you're unfamiliar

### Sample

Check out [Dice](src/Dice.py) as a sample python class that will be useful in the creation of our project!

## Unit Testing

### Sample

Check out [TestDice](src/TestDice.py) as a sample unittest class for testing our code!

### Coverage

`python -m coverage run -m unittest TestDice.py`
`coverage report -m`

Sample coverage output:
```
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
Dice.py           8      0   100%
TestDice.py      11      0   100%
-------------------------------------------
TOTAL            19      0   100%
```