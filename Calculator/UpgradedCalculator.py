mode = input('Would you like addition, subtraction, division, or multiplication? ')
if mode == "Addition":
    first = float(input("First: "))
    second = float(input("Second: "))

    sum = first + second
    int(sum)

    test = str(sum)

    print('Sum: ' + test)
if mode == "Multiplication":
    first = float(input("First: "))
    second = float(input("Second: "))

    sum = first * second
    int(sum)

    test = str(sum)

    print('Sum: ' + test)
if mode == "Subtraction":
    first = float(input("First: "))
    second = float(input("Second: "))

    sum = first - second
    int(sum)

    test = str(sum)

    print('Sum: ' + test)
if mode == "Division":
    first = float(input("First: "))
    second = float(input("Second: "))

    sum = first // second
    int(sum)

    test = str(sum)

    print('Sum: ' + test)
