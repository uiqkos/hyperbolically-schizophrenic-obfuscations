from functools import wraps, reduce


def reverse_args(f):
    @wraps(f)
    def wrapper(*args):
        return f(*reversed(args))

    return wrapper


def compose(*fs):
    return reduce(lambda f1, f2: lambda *args, **kwargs: f2(f1(*args, **kwargs)), fs)
