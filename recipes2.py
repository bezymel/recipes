def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


# Пример использования функции
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)