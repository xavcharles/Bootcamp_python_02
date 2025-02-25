def what_are_the_vars(*args, **kwargs):
    """
    ...
    """
    obj = ObjectC()
    if args:
        for i in range(len(args)):
            if (hasattr(obj, f"var_{i}")):
                return None
            setattr(obj, f"var_{i}", args[i])
    if kwargs:
        for keys, values in kwargs.items():
            if (hasattr(obj, keys)):
                return None
            setattr(obj, keys, values)
    return obj
    # ... Your code here ...

class ObjectC(object):
    def __init__(self):
        pass
    
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)