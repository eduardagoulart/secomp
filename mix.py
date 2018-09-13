# MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    c = b[:2] + a[-(len(a) - 2):]
    d = a[:2] + b[-(len(b) - 2):]
    return '{} {}'.format(c, d)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {repr(got)} expected: {repr(expected)}')


test(mix_up('mix', 'pod'), 'pox mid')
test(mix_up('dog', 'dinner'), 'dig donner')
test(mix_up('gnash', 'sport'), 'spash gnort')
test(mix_up('pezzy', 'firm'), 'fizzy perm')
