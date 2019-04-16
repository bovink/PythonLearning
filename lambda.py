def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)

print(twice(2))
print(twice('word'))
