import functools


def tracer(func):
    func._depth = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = ', '.join(repr(arg) for arg in args)
        if kwargs:
            kwargs_repr = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
            args_str = f"{args_repr}, {kwargs_repr}" if args_repr else kwargs_repr
        else:
            args_str = args_repr

        indent = "  " * func._depth

        print(f"{indent}-> {func.__name__}({args_str})")
        func._depth += 1

        try:
            result = func(*args, **kwargs)
            func._depth -= 1
            indent = "  " * func._depth
            print(f"{indent}<- {func.__name__}({args_str}) = {result!r}")

            return result
        except Exception as e:
            func._depth -= 1
            indent = "  " * func._depth
            print(f"{indent}<- {func.__name__}({args_str}) raised {type(e).__name__}: {e}")

            raise

    return wrapper
