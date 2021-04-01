# I decided to write a code that generates data filtering object from a list of keyword parameters:
# example of usage:
# positive_even = Filter(lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99
# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        result = [item for item in data if all(i(item) for i in self.functions)]
        return "It is faulty case" if not result else result


def make_filter(**keywords):

    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(lambda x: x[key] == value)
    if not filter_funcs:
        return "It is faulty case"
    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    {"is_dead": False, "kind": "swallow", "type": "bird", "name": "polly"},
    {"is_dead": True, "kind": "fish", "type": "fish", "name": "molly"},
]
