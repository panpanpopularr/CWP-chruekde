try:
    num = float(input("Give me a number: "))
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass
