def cakes(recipe, available):
    factores = list()
    for ingrediente in recipe.keys():
        if ingrediente in available.keys():
            factores.append(int(available[ingrediente])/int(recipe[ingrediente]))
        else:
            return 0
    return int(min(factores))