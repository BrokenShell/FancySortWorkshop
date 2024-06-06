from Fortuna import shuffle


class ValueType:

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"ValueType({self.value})"


if __name__ == '__main__':
    arr = [ValueType(i) for i in range(10)]
    shuffle(arr)
    sorted_arr = sorted(arr)
    print(arr)
    print(sorted_arr)
