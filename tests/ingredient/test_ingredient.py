from src.models.ingredient import (
    Ingredient,
    restriction_map,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    names = ["carne", "frango", "farinha"]
    bools = [False, True, False]
    reverse_counter = len(names)
    for index, name in enumerate(names):
        assert Ingredient(name).name == name
        assert Ingredient(name).__hash__() == hash(name)
        assert (
            Ingredient(name).__eq__(Ingredient(names[reverse_counter - 1]))
            == bools[index]
        )
        reverse_counter -= 1
        assert Ingredient(name).__repr__() == f"Ingredient('{name}')"
        assert Ingredient(name).restrictions == restriction_map().get(
            name, set()
        )
