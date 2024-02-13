from src.item import Item
from config import ROOT_DIR

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(ROOT_DIR.joinpath('items.csv'))  # указали неверный путь
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ROOT_DIR.joinpath('src', 'items_filed.csv'))  # указали поврежденный файл
    # InstantiateCSVError: Файл item.csv поврежден
