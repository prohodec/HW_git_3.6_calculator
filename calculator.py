def plus(num_1, num_2):
    pass


def minus(num_1, num_2):
    print(f"{num_1} - {num_2} = {num_1 - num_2:.2f}")


def division(num_1, num_2):
    if num_2 == 0:
        print("cannot be divided by 0")
    else:
        print(f"{num_1} / {num_2} = {num_1 / num_2:.2f}")


def multiplication(num_1, num_2):
    if num_2 == 0:
        print("cannot be multiplied by 0")
    else:
        print(f"{num_1} * {num_2} = {num_1 * num_2:.2f}")


def exponentiation(num_1, num_2):
    if num_2 == 0:
        print("cannot be exponentiated")
    else:
        print(f"{num_1} ** {num_2} = {num_1 ** num_2:.2f}")


def square_root(num):
    if num == 0:
        print("cannot be square root")
    else:
        print(f"{num} ** 0.5 = {num ** 0.5}")


def cube_root(num):
    if num == 0:
        print("cannot be cube root")
    else:
        print(f"{num} ** (1/3) = {num ** (1/3)}")


while True:
    first = input("Enter first number(enter 'off' if you want to break): ")
    if first == "off":
        break
    else:
        first = int(first)

    sign = input("Choose the mathematical operation: \n 1 - +\n 2 - -\n 3 - /\n 4 - *\n 5 - **\n 6 - ** 0.5\n"
                 " 7 - ** (1/3)\n")
    if sign == "6":
        square_root(first)
        continue
    elif sign == "7":
        cube_root(first)
        continue

    second = float(input("Enter second number: "))

    if sign == "1":
        plus(first, second)
    elif sign == "2":
        minus(first, second)
    elif sign == "3":
        division(first, second)
    elif sign == "4":
        multiplication(first, second)
    elif sign == "5":
        exponentiation(first, second)
