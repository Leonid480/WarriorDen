def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(lambda *args, **kwargs: [::-1])
    return wrapper
