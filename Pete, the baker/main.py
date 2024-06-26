def cakes(recipe: dict, available: dict) -> int:
    if len(recipe) > len(available):
        return 0
    ingrCheck = []
    availableIngr = available.keys()
    for key in recipe.keys():
        if key not in availableIngr:
            return 0
        ingrCheck.append(available[key]//recipe[key])
    return min(ingrCheck)

if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available))

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available))