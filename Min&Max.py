def minimum(a, b):
    result = 0
    if a > b:
        result = b
    elif a < b:
        result = a
    else:
        result = -1
        print("The numbers are equal")

    return result


def maximum(a, b):
    result = 0
    if a > b:
        result = a
    elif b > a:
        result = b
    else:
        result = -1
        print("The numbers are equal")
    return result


print("The minimum is: " + str(minimum(15, 20)))
print("The maximum is: " + str(maximum(25.0, 35.2)))
