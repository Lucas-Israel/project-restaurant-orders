import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def __stock_checker(self, data):
        for rec in data.recipe:
            self.inventory.consume_recipe({rec: data.recipe[rec]})

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        try:
            a = self.menu_data.dishes
            dish_name = []
            ingredients = []
            price = []
            restrictions = []
            for b in a:
                self.__stock_checker(b)
                if not b.get_restrictions().issuperset([restriction]):
                    dish_name.append(b.name)
                    ingredients.append(b.get_ingredients())
                    price.append(b.price)
                    restrictions.append(b.get_restrictions())
            new_dict = {
                "dish_name": dish_name,
                "ingredients": ingredients,
                "price": price,
                "restrictions": restrictions,
            }
            new_df = pd.DataFrame(new_dict)

        except ValueError:
            return pd.DataFrame({})
        return new_df
