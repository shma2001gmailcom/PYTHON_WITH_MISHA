def presentations_enum(int_to_present, components):
    answer = [[]]
    if int_to_present == 0:
        return answer
    for offset in range(0, len(components)):  # for each components
        less_number = int_to_present - components[offset]  # subtract one of the components for recursion
        if less_number >= 0:  # consider only non-negative reductions
            for presentations_of_less_number in presentations_enum(less_number, components):  # recursion
                presentations_of_less_number.append(components[offset])  # obtain new representation from old one
                answer.append(presentations_of_less_number)  # add new representation to result
    return answer


def check_sum(array, pattern):  # checks if sum of array elements is equals to 'pattern'
    aggregate = 0
    for e in array:
        aggregate += e
    return aggregate == pattern


def presentation_to_string(integer_to_present, presentation_array):  # presentation (1, 1) to string (2=1+1)
    result = str(integer_to_present) + '='
    for j in range(0, len(presentation_array)):
        if j == 0:
            result += str(presentation_array[j])
        else:
            result += '+' + str(presentation_array[j])
    return result


def print_representations(integer_to_present, components):
    for sequence in presentations_enum(integer_to_present, components):
        if check_sum(sequence, integer_to_present):
            print(presentation_to_string(integer_to_present, sequence))


def main():
    components = [2, 3, 5, 7]
    for integer_to_present in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        print()
        print("presentations of " + str(integer_to_present) + ' as a sum of ' + str(components) + ':')
        print_representations(integer_to_present, components)


main()
