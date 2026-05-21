double_keys = lambda **kwargs: {k * 2: v for k, v in kwargs.items()}
print(double_keys(abc=7, x=77))
