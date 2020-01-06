def presentations_enum(int_to_present, components):
    answer = [[]]
    if int_to_present == 0:
        return answer
    for offset in range(0, len(components)):
        less_number = int_to_present - components[offset]
        if less_number >= 0:
            for x in presentations_enum(less_number, components):
                x.append(components[offset])
                answer.append(x)
    return answer


def check_sum(array, pattern):
    aggregate = 0
    for e in array:
        aggregate += e
    return aggregate == pattern


def presentation_to_string(integer_to_present, presentation_array):
    result = str(integer_to_present) + '='
    for j in range(0, len(presentation_array)):
        if j == 0:
            result += str(presentation_array[j])
        else:
            result += '+' + str(presentation_array[j])
    return result


def main():
    components = [2, 3, 5, 7]
    for integer_to_present in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
        print()
        print("presentations of " + str(integer_to_present) + ' as a sum of ' + str(components) + ':')
        for x in presentations_enum(integer_to_present, [2, 3, 5, 7]):
            if check_sum(x, integer_to_present):
                print(presentation_to_string(integer_to_present, x))


main()
