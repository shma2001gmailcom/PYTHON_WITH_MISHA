def sub_div(i, a):
    if i == 0:
        return 1
    answer = 0
    for offset in range(0, len(a)):
        if i - a[offset] >= 0:
            answer += sub_div(i - a[offset], a)
    return answer


def main():
    a = [1, 2, 3]
    print(sub_div(6, a))
    print("for 6-1:\n2+3, 3+2, 1+2+2, 2+1+2, 2+2+1, 1+1+3, 1+3+1, 3+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1,"
          "1+1+1+1+1 (add 1)")
    print(sub_div(6 - 1, a))
    print("for 6-2:\n2+2, 3+1, 1+3, 1+1+1+1, 1+1+2, 1+2+1, 2+1+1 (add 2)")
    print(sub_div(6 - 2, a))
    print("for 6-3:\n3, 2+1, 1+2, 1+1+1 (add 3)")
    print(sub_div(6 - 3, a))


main()
