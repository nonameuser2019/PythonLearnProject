def cakes(recipe: dict, available: dict):
    result = []
    for key, val in recipe.items():
        try:
            result.append(available[key] // val)
        except:
            return 0
    return min(result)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
assert cakes(recipe, available) == 2


# below is the best practice it isn't mine decision
def cakes_2(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)