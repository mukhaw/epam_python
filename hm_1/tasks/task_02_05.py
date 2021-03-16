def detect_index(some_iterable_object, position):
    if isinstance(some_iterable_object, dict):
        if position in list(some_iterable_object.keys()):
            return list(some_iterable_object.keys()).index(position)
        else:
            return list(some_iterable_object.values()).index(position)
    return some_iterable_object.index(position)


def custom_range(some_iterable_object, start="", stop="", step=1):
    if not some_iterable_object:
        return "Wrong values"
    start = 0 if start == "" else detect_index(some_iterable_object, start)
    stop = (
        len(some_iterable_object)
        if stop == ""
        else detect_index(some_iterable_object, stop)
    )
    if isinstance(some_iterable_object, list) or isinstance(
        some_iterable_object, tuple
    ):
        return some_iterable_object[start:stop:step]
    if isinstance(some_iterable_object, dict):
        return list(some_iterable_object.items())[start:stop:step]
    return list(some_iterable_object)[start:stop:step]
