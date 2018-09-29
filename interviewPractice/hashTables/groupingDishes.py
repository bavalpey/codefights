"""
You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it. You want to group the dishes by
ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list with the first element equal to the name of the ingredient and all of the other elements
equal to the names of dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically. The result
array should be sorted lexicographically by the names of the ingredients in its elements.

Example
For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
For
  dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Chicken", "Chicken Curry", "Quesadilla"],
                            ["Nuts", "Fried Rice", "Salad"],
                            ["Onions", "Fried Rice", "Pasta"]]
"""

def groupingDishes(d):
  recipeDict = dict()
  for recipe in d:
    for ingredient in recipe[1:]:
      if ingredient in recipeDict:
        recipeDict[ingredient].append(recipe[0])
      else:
        recipeDict[ingredient] = [recipe[0]]
  to_Return = []
  
  for item in recipeDict:
    if len(recipeDict[item]) >= 2:
      x = sorted(recipeDict[item])
      y = [item]
      y.extend(x)
      to_Return.append(y)
  return sorted(to_Return)1
