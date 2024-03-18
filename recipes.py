def read_cook_book_from_file(filename):
    cook_book = {}
    with open(filename, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            cook_book[dish_name] = []
            ingredient_count = int(file.readline().strip())
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient = {'ingredient_name': ingredient_info[0], 'quantity': int(ingredient_info[1]), 'measure': ingredient_info[2]}
                cook_book[dish_name].append(ingredient)
    return cook_book

filename = 'recipes.txt'
cook_book = read_cook_book_from_file(filename)

print(cook_book)
