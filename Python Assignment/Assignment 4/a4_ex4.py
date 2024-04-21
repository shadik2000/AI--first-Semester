def round_(number, ndigits: int | None = None) :
    if ndigits is None:
        ndigits = 0

    if ndigits == 0:
        return int(number)

    multiplier = 10**ndigits
    whole_part = int(number * multiplier)
    fractional_part = number * multiplier - whole_part

    if fractional_part < 0.5:
        rounded_number = whole_part
    elif fractional_part > 0.5:
        rounded_number = whole_part + 1
    else:
        # In case of a tie, round towards the even digit
        if whole_part % 2 == 0:
            rounded_number = whole_part
        else:
            rounded_number = whole_part + 1

    return rounded_number / multiplier


# print(round_(777.777,4))
# print(round_(777.77, 2))