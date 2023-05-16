from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, restriction_map
import pytest


# Req 2
def test_dish():
    names = ["aaa", "bbb", "ccc"]
    prices = [1.0, 2.0, 3.0]
    fake_prices = [-1.0, -2.0, -3.0]
    reverse_counter = len(names)
    bools_for_eq = [False, True, False]
    ingredient_names = ["carne", "frango", "farinha"]
    list_ingredient_dict = [
        {Ingredient("carne")},
        {Ingredient("frango")},
        {Ingredient("farinha")},
    ]
    index = 0
    for name, price, fake_price in zip(names, prices, fake_prices):
        dish = Dish(name, price)
        assert dish.name == name
        assert dish.price == price
        with pytest.raises(
            Exception, match="Dish price must be greater then zero."
        ):
            Dish(name, fake_price)
        assert dish.__hash__() == hash(f"Dish('{name}', R${price:.2f})")
        other = Dish(names[reverse_counter - 1], price)
        assert dish.__eq__(other) == bools_for_eq[reverse_counter - 1]
        reverse_counter -= 1
        ingredient = Ingredient(ingredient_names[index])
        dish.add_ingredient_dependency(ingredient, 1)
        assert dish.get_ingredients() == list_ingredient_dict[index]
        assert dish.get_restrictions() == restriction_map().get(
            ingredient_names[index], set()
        )
        index += 1
