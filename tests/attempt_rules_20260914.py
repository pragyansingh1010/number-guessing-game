def valid_attempts(value):
    return isinstance(value, int) and value >= 0

assert valid_attempts(0)
assert valid_attempts(5)
assert not valid_attempts(-1)
print('Attempt rules passed')
