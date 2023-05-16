from csv import DictReader, DictWriter
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Dict:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


def write_csv_inventory(data, inventory_file_path=BASE_INVENTORY):
    print(data)
    with open(inventory_file_path, "w", newline="") as file:
        header = ["ingredient", "initial_amount"]
        writer = DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerow({"ingredient": "a", "initial_amount": 2})


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)
        self._file_path = inventory_file_path

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe):
        for rec in recipe:
            if rec not in self.inventory:
                return False
            if recipe[rec] > self.inventory[rec]:
                return False
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        inventario = self.inventory

        if self.check_recipe_availability(recipe) is False:
            raise ValueError()

        for rec in recipe:
            inventario[rec] -= recipe[rec]

        write_csv_inventory(inventario, self._file_path)
        return None
