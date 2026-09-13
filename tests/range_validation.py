def valid_guess(value, low=1, high=100):
    return isinstance(value, int) and low <= value <= high

assert valid_guess(1)
assert valid_guess(100)
assert not valid_guess(0)
assert not valid_guess(101)
print("Guess range tests passed")
