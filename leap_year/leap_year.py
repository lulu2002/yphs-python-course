def is_leap_year(year: int):
    if special_case_not_leap(year):
        return False

    return year % 4 == 0


def special_case_not_leap(year):
    if year % 400 == 0:
        return False

    return year % 100 == 0
