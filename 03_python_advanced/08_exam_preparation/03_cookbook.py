def cookbook(*recipes):
    recipes_per_cuisine = {}
    cuisines = {}
    result = ""

    for current_recipe in recipes:
        recipe_name, cuisine, list_of_ingredients = current_recipe
        if cuisine not in recipes_per_cuisine:
            recipes_per_cuisine[cuisine] = []
            cuisines[cuisine] = 0
        recipes_per_cuisine[cuisine].append((recipe_name, list_of_ingredients))
        cuisines[cuisine] += 1

    cuisines_sorted = sorted(cuisines.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    for cuisine, count in cuisines_sorted:
        result += f"{cuisine} cuisine contains {count} recipes:\n"
        sorted_recipes = sorted(recipes_per_cuisine[cuisine], key=lambda kvp: kvp[0])
        for recipe_name, list_of_ingredients in sorted_recipes:
            list_of_ingredients_as_str = [str(ingredient) for ingredient in list_of_ingredients]
            result += f"  * {recipe_name} -> Ingredients: {', '.join(list_of_ingredients_as_str)}\n"

    return result
