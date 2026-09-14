def valid_target(n):
    return 1 <= n <= 100

assert valid_target(1)
assert valid_target(50)
assert valid_target(100)
assert not valid_target(0)
assert not valid_target(101)
print('Target rules passed')
