def trace(func):
    def wrapper(*args):
        print("│ "*wrapper.space + func.__name__ + " <-- " + str(args))
        wrapper.space += 1
        val = func(*args)
        wrapper.space -=1
        print("│ "*wrapper.space + func.__name__ + " --> " + str(val))
        return val
    wrapper.space = 0
    return wrapper