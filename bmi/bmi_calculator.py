import math


def calculate(height_cm, weight_kg):
    height_in_m = height_cm / 100
    return round(weight_kg / (math.pow(height_in_m, 2)), 1)


def get_message(bmi: float):
    if bmi < 18.5:
        return "LIGHT"
    if bmi < 24:
        return "GOOD"
    if bmi < 27:
        return "HEAVY"

    return "FAT"


if __name__ == '__main__':
    height = float(input("請輸入你的身高 (cm): "))
    weight = float(input("請輸入你的體重 (kg): "))

    bmi = calculate(height, weight)

    print("BMI:", bmi)

    print(
        {
            "LIGHT": "過輕",
            "GOOD": "適中",
            "HEAVY": "過重",
            "FAT": "肥胖",
        }[get_message(bmi)]
    )
