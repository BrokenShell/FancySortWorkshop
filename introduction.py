""" Fancy Sort Introduction

.sort() vs sorted()

Differences
1. While sorted leaves the original list intact, .sort is destructive and
changes the original list "in-place".
2. Sorted is a free function, .sort is a method on the list class.
3. .sort is slightly faster than sorted, especially for very large lists.
4. Sorted can be used on any iterable, .sort only works for lists or containers
that inherit from list.

Similarities
1. Both will sort a list.
2. Both can accept the key parameter for custom sorting.
3. Both have BigO(n log n)
"""
# Sort with .sort()
arr_1 = [2, 9, 1, 8, 3, 7, 4, 6, 5]
# print(arr_1)
# arr_1.sort()
# print(arr_1)

# Sort with sorted()
arr_2 = [3, 7, 4, 6, 5, 2, 9, 1, 8]
arr_3 = sorted(arr_2)
print(arr_2)
print(arr_3)
