# Req 3
from models.dish import Dish, Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.df = pd.read_csv(source_path)
        self.dishes = set()
        self.__populate_data()

    def __len__(self):
        return len(self.dishes)

    def __dict_creator(self):
        ingredient_dict = dict()
        recipe_amount_dict = dict()
        for a in self.df.groupby(["dish", "price"])[
            ["ingredient", "recipe_amount"]
        ]:
            ingredient_dict[a[0]] = tuple(a[1]["ingredient"])
            recipe_amount_dict[a[0]] = tuple(a[1]["recipe_amount"])
        return (ingredient_dict, recipe_amount_dict)

    def __populate_data(self):
        ing_di, amo_di = self.__dict_creator()

        for ele in ing_di:
            new_dish = Dish(ele[0], ele[1])
            for ing, amount in zip(ing_di[ele], amo_di[ele]):
                new_dish.add_ingredient_dependency(Ingredient(ing), amount)
            self.dishes.add(new_dish)


if __name__ == "__main__":
    a = MenuData("tests/mocks/menu_base_data.csv")
    b = a.dishes
    for c in b:
        print(c.recipe)
