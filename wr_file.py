import pprint as pp


def my_cook_book():
    with (open('recept.txt', encoding='utf-8') as file):
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(
                    lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity,
                     'measure': measure})
            cook_book[name] = tmp
    return cook_book


pp.pprint(my_cook_book(), indent=2, width=4)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = my_cook_book()
    shop_lists = {}
    for dish in dishes:
        ing = cook_book[dish]
        for i in ing:
            if i['ingredient_name'] not in shop_lists:
                shop_lists[i['ingredient_name']] = i['quantity'] * person_count
            else:
                shop_lists[i['ingredient_name']] *= person_count

    print(shop_lists)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'],
                        2)
