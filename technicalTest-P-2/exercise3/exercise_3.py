
def is_valid_ISBN10(ISBN):
    if len(ISBN) != 10 or not ISBN[:-1].isdigit() or not ISBN[-1].isdigit() and ISBN[-1] != 'X':
        return False

    first_9_digits_sum = sum(int(digit) * (11 - i) for i, digit in enumerate(ISBN[:-1], start=1))

    control_digit = ISBN[-1]
    if control_digit == "X":
        control_digit = 10

    if (first_9_digits_sum + int(control_digit)) % 11 == 0:
        return True
    else:
        return False
