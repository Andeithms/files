
def cooking_book(file_name):
    with open(file_name) as file_work:

        for line in file_work:
            dish_name = line.strip()
            # print(line.strip())
            counter = int(file_work.readline().strip())
            list_of_ingridient = []

            for i in range(counter):
                string = file_work.readline().strip().split(sep=' | ')
                # print(string)
                temp_dict = dict(ingredient_name=string[0], quantity=string[1], measure=string[2])
                list_of_ingridient.append(temp_dict)
                cook_book[dish_name] = list_of_ingridient

            file_work.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person):
    shop_list = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            if shop_list.get(ingridient['ingredient_name']) is None:
                shop_list[ingridient['ingredient_name']] = {'measure': ingridient['measure'],
                                                            'quantity': int(ingridient['quantity']) * person}
            else:
                shop_list[ingridient['ingredient_name']]['quantity'] += int(ingridient['quantity']) * person

    return shop_list


cook_book = {}
print(cooking_book('recipes.txt'))
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))