def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("not a function or not callable")
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("not iterable")
    if (len(iterable) >= 2):
        x = function_to_apply(iterable[0], iterable[1])
        for i in range(2, len(iterable)):
            y = iterable[i]
            x = function_to_apply(x, y)
        return x

