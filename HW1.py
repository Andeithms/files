cook_book = {}


def cooking_book():
    with open('recipes.txt') as f:
        for line in f:
            if '|' not in line and line != '':
                dish = line.strip()
                cook_book[dish] = []
            else:
                new_doc = dict(ingredient_name=line.split(' | ')[0],
                               quantity=line.split(' | ')[1],
                               measure=line.split(' | ')[2].strip())
                cook_book[dish].append(new_doc)
    print(cook_book)


def get_shop_list_by_dishes(dishes, person):
    for x in dishes:
        new_order(x, person)


def new_order(order, person):
    orders = {}
    for dish, ingredients in cook_book.items():
        if order == dish:
            orders[dish] = ingredients
            for i in ingredients:
                for quantity, count in i.items():
                    if 'quantity' == quantity:
                        i[quantity] = int(count) * person
    print(orders)


cooking_book()
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3)