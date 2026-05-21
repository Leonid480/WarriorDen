from functools import filter
def remove_evens(func):
    def wrapper(numbers, *args, **kwargs):
        filtered_numbers = [lambda num:num % 2 == 0, numbers]
        return func(filtered_numbers, *args, **kwargs)
    
    return wrapper
