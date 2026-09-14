def valid_guess(n, low=1, high=100):
    return low <= n <= high

assert valid_guess(1)
assert valid_guess(100)
assert not valid_guess(0)
assert not valid_guess(101)
print('Guess bounds passed')
