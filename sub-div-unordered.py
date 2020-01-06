# Calculates a number of different expressions of 'n' as a sum of at most 'k' terms
# belonging to the set 'a'. The order of the terms in expression is considered as inessential.


def sums(n, k, a):
    if n < 0:
        return 0
    for e in a:
        if e < 0:
            return 0
    if n == 0 and k <= 0:
        return 1
    if n != 0 and k <= 0:
        return 0
    if len(a) == 0 and n == 0:
        return 1
    if len(a) == 0 and n != 0:
        return 0
    if a[0] > n:
        return sums(n, k, a[1:])
    return sums(n - a[0], k - 1, a) + sums(n, k, a[1:])


print(sums(6, 3, [1, 2, 3]))
print(sums(11, 4, [1, 7]))
print(sums(11, 5, [1, 7]))
print(sums(6, 9, [1, 2, 4]))
print(sums(11, 11, [2, 4, 6]))
