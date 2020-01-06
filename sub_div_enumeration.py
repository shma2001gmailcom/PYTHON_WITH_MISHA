def sub_enum(n, a):
    answer = [[]]
    if n == 0:
        return answer
    for offset in range(0, len(a)):
        less_n = n - a[offset]
        if less_n >= 0:
            for x in sub_enum(less_n, a):
                x.append(a[offset])
                answer.append(x)
    return answer


def check_sum(array, pattern):
    s = 0
    for e in array:
        s += e
    return s == pattern


def presentation_to_string(integer_to_present, x):
    result = str(integer_to_present) + '='
    for j in range(0, len(x)):
        if j == 0:
            result += str(x[j])
        else:
            result += '+' + str(x[j])
    return result


def main():
    for integer_to_present in [1, 2, 3, 4, 5, 6]:
        print()
        print("presentations of " + str(integer_to_present) + ' as a sum of 1, 2, 3:')
        for x in sub_enum(integer_to_present, [1, 2, 3]):
            if check_sum(x, integer_to_present):
                print(presentation_to_string(integer_to_present, x))


main()
