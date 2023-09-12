# hyperbolically-schizophrenic-obfuscations
ss rank obfuscations
## FizzBuzz
[source](fizzbuzz.py)
### Simple
даже объяснять не надо
```python
def simple():
    return '\n'.join(
        ('Fizz' * (not i % 3) + 'Buzz' * (not i % 5)) or str(i)
        for i in range(1, 100 + 1)
    )
```
### Simple v2
остаток от деления как индекс
```python
def simple2():
    return '\n'.join(
        map(
            lambda s, i: s + str(i) * (len(s) == 0),
            map(
                str.__add__,
                map(
                    ['Fizz', *[''] * 2].__getitem__,
                    map(partial(reverse_args(mod), 3), range(1, 100 + 1))
                ),
                map(
                    ['Buzz', *[''] * 4].__getitem__,
                    map(partial(reverse_args(mod), 5), range(1, 100 + 1))
                )
            ),
            range(1, 100 + 1)
        )
    )
```
### Simple v3
повторяющийся паттерн
```python
def simple3():
    return '\n'.join(map(str, reduce(
        list.__add__,
        ([
            *range(i, i + 2), 'Fizz',
            *range(i + 3, i + 4), 'Buzz', 'Fizz',
            *range(i + 6, i + 8), 'Fizz', 'Buzz',
            *range(i + 10, i + 11), 'Fizz',
            *range(i + 12, i + 14), 'FizzBuzz',
        ] for i in range(1, 100 + 1, 15))
    )[:100]))
```
### Middle fp
100 вложенных лямбд
```python
def middle():
    result = []

    list(
        map(
            methodcaller('__call__', list(range(1, 101))),
            map(
                compose,
                map(itemgetter, range(100)),
                repeat(lambda i: ('Fizz' * (not i % 3) + 'Buzz' * (not i % 5)) or str(i)),
                repeat(result.append)
            )
        )
    )

    return '\n'.join(result)
```

### 3 5 15
```python
from functools import partial
from itertools import filterfalse
from operator import mod, methodcaller, mul

reverse = lambda f: lambda *x: f(*reversed(x))
compose2 = lambda f, g: lambda *x: f(g(*x))
print(sum(map(mul, [1, 1, -1], map(sum, map(methodcaller('__call__', range(1000)),
      map(compose2(partial(partial, filterfalse), partial(partial, reverse(mod))), [3, 5, 15]))))))

```
