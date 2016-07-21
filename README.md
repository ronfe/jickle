# jickle
A package for JSON pickle

## Install
```
pip3 install jickle
```

## Usage
It is SPECIFICALLY useful if you intend to update data from a nested JSON and then return them to JSON.

```{python}
from jickle import *
import json

a = {"a": 1, "b": {"b1": 2, "b2": 3}}
b = json.dumps(a)
c = Jickle(b)

# if you want to change 3 to [333] at anywhere in a
c.substitute(3, [333])

# let's output the new dict
c.update()
c.output_dict
# output: {'a': 1, 'b': {'b2': [333], 'b1': 2}}

```
