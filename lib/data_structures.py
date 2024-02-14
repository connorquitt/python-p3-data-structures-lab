spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = [n['name'] for n in spicy_foods]
    return names_list

def get_spiciest_foods(spicy_foods):
    hot_list = [n for n in spicy_foods if n['heat_level'] > 5]
    return hot_list

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
       food = f"{n['name']} ({n['cuisine']}) | Heat Level: {'🌶' * n['heat_level']}"
       print(food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food = [n for n in spicy_foods if n["cuisine"] == cuisine]
    return food[0]

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    number = 0
    index = len(spicy_foods)
    for n in spicy_foods:
        number = number + n['heat_level']
    return number/(index)


def create_spicy_food(spicy_foods, spicy_food):
    list = spicy_foods.append(spicy_food)
    return spicy_foods