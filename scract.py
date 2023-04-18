import datetime
from datetime import timedelta
from random import randint

# d = {
#     "a": [3, 2, 1],
#     "b": [5, 7, 3],
#     "c": [9, 4, 2],
# }
# arr = list(d.values())
# arr.sort(key=lambda x: x[1])
# print(arr)

arr = [datetime.datetime.now() - timedelta(days=randint(1, 10)) for _ in range(5)]
arr.sort()
print(arr)
