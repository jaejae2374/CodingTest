import bisect
b = [[1,2], [2,3], [3,4]]
bisect.bisect_left(b, [1,5], key=lambda x: x[1])
print(b)