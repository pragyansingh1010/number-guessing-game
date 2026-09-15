def in_range(value, low, high):
    return low <= value <= high

assert in_range(1, 1, 10)
assert in_range(10, 1, 10)
assert not in_range(11, 1, 10)
