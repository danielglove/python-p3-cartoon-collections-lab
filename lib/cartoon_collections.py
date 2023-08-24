def roll_call_dwarves(list):
    names = [f"{index + 1}. {name}" for index, name in enumerate(list)]
    for name in names:
        print(f"{name}")


def summon_captain_planet(planeteer_calls):
    planeteer_calls = [f"{call.capitalize()}!" for call in planeteer_calls]
    return planeteer_calls


def long_planeteer_calls(calls):
    for call in calls:
        if (len(call) > 4):
            return True

    return False


def find_the_cheese(strings):
    types_of_cheese = ("cheddar", "gouda", "camebert")
    for element in strings:
        if (element in types_of_cheese):
            return element

    return None


print(roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"]))
print(summon_captain_planet(["earth", "wind", "fire", "water", "heart"]))
print(long_planeteer_calls(
    ["puff", "go", "two", "four", "five", "industrious"]))

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup))
