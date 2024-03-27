def int_within_bounds(number, lower_bound, upper_bound):
    if type(number) != int:
        return False
    elif number < upper_bound and number >= lower_bound:
        return True
    else:
        return False
