def calculate(month, day):
    result = (month * 2 + day) % 3

    return {
        0: "普通",
        1: "吉",
        2: "大吉"
    }[result]


if __name__ == '__main__':
    month = int(input("請輸入月份: "))
    day = int(input("請輸入日: "))

    print(calculate(month, day))
