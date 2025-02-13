def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("not a function or not callable")
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("not iterable")
    for i in iterable:
        yield function_to_apply(i)