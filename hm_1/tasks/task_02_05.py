def detect_index(some_iterable_object, position):
    if isinstance(some_iterable_object, dict):
        if position in list(some_iterable_object.keys()):
            return list(some_iterable_object.keys()).index(position)
        else:
            return list(some_iterable_object.values()).index(position)
    return some_iterable_object.index(position)


def detect_stop_start_step(some_iterable_object, args):
    if not args:
        args = 0, len(some_iterable_object), 1
        return args
    elif len(args) == 1:
        args = 0, detect_index(some_iterable_object, args[0]), 1
        return args
    elif len(args) == 2:
        args = (
            detect_index(some_iterable_object, args[0]),
            detect_index(some_iterable_object, args[1]),
            1,
        )
        return args
    elif len(args) == 3:
        args = (
            detect_index(some_iterable_object, args[0]),
            detect_index(some_iterable_object, args[1]),
            args[2],
        )
        return args
    else:
        return "Wrong values"


def custom_range(some_iterable_object, *args):
    if not some_iterable_object:
        return "Wrong values"
    start, stop, step = detect_stop_start_step(some_iterable_object, args)
    if isinstance(some_iterable_object, list) or isinstance(
        some_iterable_object, tuple
    ):
        return some_iterable_object[start:stop:step]
    if isinstance(some_iterable_object, dict):
        return list(some_iterable_object.items())[start:stop:step]
    return list(some_iterable_object)[start:stop:step]
