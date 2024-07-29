import pandas as pd

def get_unique_ingredients(dataset):
    """This function returns the count os unique ingredients for each pizza type."""

    # Transform ingredients list into one-hot encoded matrix.
    ingredients_dummies = (pd.concat([dataset['pizza_type_id'], 
                                      pd.get_dummies(dataset['ingredients'].str.split(", ").explode(), 
                                                     dtype=int
                                                     )
                                      ],
                                     axis=1
                                     )
                           .groupby('pizza_type_id')
                           .sum()
                           )
    
    # Calculate number of pizzas that uses each ingredient.
    ingredients_counts = ingredients_dummies.sum(axis=0)
    # Get a list of ingredient only used in one pizza type.
    unique_ingredients_list = (ingredients_counts[ingredients_counts==1]
                               .index
                               .to_list()
                               )
    # Count the number of unique ingredients for each pizza type.
    num_unique_ingredients = ingredients_dummies[unique_ingredients_list].sum(axis=1).values

    return num_unique_ingredients