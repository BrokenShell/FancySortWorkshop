from itertools import zip_longest

from Fortuna import shuffle
import string


class ValueType:

    def __init__(self, name: str, value: int):
        self.name = name or ''
        self.value = value or 0

    def __lt__(self, other):
        return (self.name, self.value) < (other.name, other.value)
        # if self.name < other.name:
        #     return True
        # elif self.name == other.name:
        #     return self.value < other.value
        # else:
        #     return False

    def __repr__(self):
        return f"ValueType({self.name}, {self.value})"


if __name__ == '__main__':
    alphabet = string.ascii_lowercase
    arr = [ValueType(a, i) for a, i in zip_longest(['a', 'b', 'b', 'b', 'c'], range(10))]
    shuffle(arr)
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)
