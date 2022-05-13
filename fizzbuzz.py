from functools import partial, reduce
from itertools import zip_longest, repeat
from operator import mod, itemgetter, methodcaller

from more_itertools import last

from utils import reverse_args, compose

correct = '\n'.join(map(str, [
    1,
    2,
    "Fizz",
    4,
    "Buzz",
    "Fizz",
    7,
    8,
    "Fizz",
    "Buzz",
    11,
    "Fizz",
    13,
    14,
    "FizzBuzz",
    16,
    17,
    "Fizz",
    19,
    "Buzz",
    "Fizz",
    22,
    23,
    "Fizz",
    "Buzz",
    26,
    "Fizz",
    28,
    29,
    "FizzBuzz",
    31,
    32,
    "Fizz",
    34,
    "Buzz",
    "Fizz",
    37,
    38,
    "Fizz",
    "Buzz",
    41,
    "Fizz",
    43,
    44,
    "FizzBuzz",
    46,
    47,
    "Fizz",
    49,
    "Buzz",
    "Fizz",
    52,
    53,
    "Fizz",
    "Buzz",
    56,
    "Fizz",
    58,
    59,
    "FizzBuzz",
    61,
    62,
    "Fizz",
    64,
    "Buzz",
    "Fizz",
    67,
    68,
    "Fizz",
    "Buzz",
    71,
    "Fizz",
    73,
    74,
    "FizzBuzz",
    76,
    77,
    "Fizz",
    79,
    "Buzz",
    "Fizz",
    82,
    83,
    "Fizz",
    "Buzz",
    86,
    "Fizz",
    88,
    89,
    "FizzBuzz",
    91,
    92,
    "Fizz",
    94,
    "Buzz",
    "Fizz",
    97,
    98,
    "Fizz",
    "Buzz"
]))

to_test = []
register = lambda f: last((to_test.append(f), f))


@register
def classic():
    s = ''
    for i in range(1, 100 + 1):
        _3 = i % 3
        _5 = i % 5

        if _3 == 0 and _5 == 0:
            s += 'FizzBuzz'
        elif _3 == 0:
            s += 'Fizz'
        elif _5 == 0:
            s += 'Buzz'
        else:
            s += str(i)

        if i != 100:
            s += '\n'

    return s


@register
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


@register
def simple():
    return '\n'.join(
        ('Fizz' * (not i % 3) + 'Buzz' * (not i % 5)) or str(i)
        for i in range(1, 100 + 1)
    )


@register
def simple_():
    return '\n'.join(
        (('Fizz' if not i % 3 else '') + ('Buzz' if not i % 5 else '')) or str(i)
        for i in range(1, 100 + 1)
    )


@register
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


@register
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


@register
def middle2():

    return '\n'.join(
        map(
            lambda i: repeat(i),
            range(1, 100 + 1)
        )
    )


if __name__ == '__main__':
    for f in to_test:
        if f() != correct:
            print(f())
            assert False, f.__name__
