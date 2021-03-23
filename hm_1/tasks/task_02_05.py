def detect_index(some_iterable_object, position):
    return some_iterable_object.index(position)


def detect_stop_start_step(some_iterable_object, args):
    if not args:
        return 0, len(some_iterable_object), 1
    elif len(args) == 1:
        return 0, detect_index(some_iterable_object, args[0]), 1
    elif len(args) == 2:
        return (
            detect_index(some_iterable_object, args[0]),
            detect_index(some_iterable_object, args[1]),
            1,
        )
    elif len(args) == 3:
        return (
            detect_index(some_iterable_object, args[0]),
            detect_index(some_iterable_object, args[1]),
            args[2],
        )
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
    return list(some_iterable_object)[start:stop:step]
