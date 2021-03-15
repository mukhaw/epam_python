def custom_range(some_iterable_object, start=1, stop=1, step=1):
    start = some_iterable_object.index(start)
    stop = some_iterable_object.index(stop)
    return list(some_iterable_object[start:stop:step])
