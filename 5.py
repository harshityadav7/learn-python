"""You are given a string and your task is to swap cases. In other words, convert all
lowercase letters to uppercase
letters and vice versa."""


def swap_case(s):
    result = ""
    for i in s:
        if i.isupper():
            result = result + i.lower()
        else:
            result = result + i.upper()
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
