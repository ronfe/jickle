# jickle
A package for JSON pickle

## Usage
```{python}
from jickle import *
import json

a = {"a": 1, "b": {"b1": 2, "b2": 3}}
b = json.loads(a)
c = Jickle(b)

# if you want to change 3 to [333] at anywhere in a
c.substitute(3, [333])

# let's output the new dict
c.update()
d = c.output_dict()

```
