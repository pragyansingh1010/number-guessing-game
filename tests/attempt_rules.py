def valid_attempts(count):
    return isinstance(count, int) and count >= 0

assert valid_attempts(0)
assert valid_attempts(5)
assert not valid_attempts(-1)
assert not valid_attempts(2.5)
print('Guess attempt rules passed')
