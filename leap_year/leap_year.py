def is_leap_year(year: int):
    if special_case_not_leap(year):
        return False

    return year % 4 == 0


def special_case_not_leap(year):
    if year % 400 == 0:
        return False

    return year % 100 == 0


if __name__ == '__main__':
    while True:
        try:
            year = int(input("請輸入年份"))
        except ValueError:
            continue

        if year == 0:
            break

        print(year, "是閏年: ", is_leap_year(year))
