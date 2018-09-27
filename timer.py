import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        time_dif = time.time() - start
        print('Function: {} with {} was working for: {:.2f}' .format(
            func.__name__, args, time_dif))
        return func_result

    return wrapper
