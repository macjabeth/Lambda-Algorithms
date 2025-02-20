#!/usr/bin/python

def recipe_batches(recipe, ingredients):
  batches = None
  for ingr in recipe:
    if not ingredients.get(ingr): return 0
    if not batches or (ingredients[ingr] // recipe[ingr]) < batches:
      batches = ingredients[ingr] // recipe[ingr]
  return batches or 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
