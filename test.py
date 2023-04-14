from bisect import bisect_left, bisect_right, insort_right
a = [1, 2, 2, 2, 3, 3, 3, 5]
insort_right(a, 2)
print(a)