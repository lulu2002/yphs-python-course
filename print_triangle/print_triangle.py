def print_triangle(height: int):
    for i in range(0, height):
        print((height - i) * " " + ("*" * (2 * i + 1)))


if __name__ == '__main__':
    while True:
        try:
            height = int(input("請輸入三角形高度: "))
        except ValueError:
            continue

        if height == 0:
            break

        print_triangle(height)
