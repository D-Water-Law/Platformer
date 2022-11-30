def five(num=None):
    if num:
        if num[0] == "*":
            return int(num[1:])*5
    return 5


def seven(num=None):
    if num:
        if num[0] == "*":
            return int(num[1:])*7
    else:
        return 7

def times(num):
    return f"*{num}"

print(seven(times(five())))

