def compare(guess, target):
    if guess < target:
        return 'low'
    if guess > target:
        return 'high'
    return 'correct'

assert compare(4, 5) == 'low'
assert compare(6, 5) == 'high'
assert compare(5, 5) == 'correct'
