number1 = int(input("Tell me a number: "))
number2 = int(input("Tell me another number: "))


def number_compare():
    if number1 > number2:
        return "Number1 is greater"
    elif number2 > number1:
        return "Number2 is greater"
    else:
        return "Numbers are equal"


print(number_compare())
