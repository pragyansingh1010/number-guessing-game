def valid_attempts(attempts):
    return attempts >= 1

assert valid_attempts(1)
assert not valid_attempts(0)
