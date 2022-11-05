def make_change(item_price: int, gave: int, types: [int]):
    change_left = item_price - gave
    changes = []

    for type in types:
        amount = int(change_left // type)
        changes.append({
            "type": type,
            "amount": amount
        })

        change_left -= type * amount

    return changes


def get_unit_by_type(type):
    if type >= 100:
        return "張"
    return "個"


if __name__ == '__main__':
    price = int(input("請輸入商品價格"))
    gave = int(input("請輸入支付的金額"))
    money_types = [1000, 500, 100, 50, 10, 5, 1]
    changes = make_change(price, gave, money_types)

    for change in changes:
        if change["amount"] > 0:
            print(change["type"], "元:", change["amount"], get_unit_by_type(change["type"]))

    print("你給了老闆", gave, "元", "找零", price - gave, "元")
