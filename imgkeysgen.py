input = int(input("number of keys? "))
if input > 0:
    result = ""
    for n in range(input + 1):
        if n == 0:
            result += "0,"
        elif n == input:
            result += str(input)
        else:
            result += str(n) + ","
    print(result)