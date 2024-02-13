import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard
from config import ROOT_DIR
from src.exception import InstantiateCSVError

item1 = Item('Смартфон', 10000, 20)
item2 = Item('Ноутбук', 20000, 5)
item1.pay_rate = 0.8
item2.pay_rate = 0.5
phone1 = Phone('Samsung s24', 120000, 5, 2)
keyboard1 = Keyboard('Thor', 10000, 7)


def test_item():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item2.name == 'Ноутбук'
    assert item2.price == 20000
    assert item2.quantity == 5
    assert phone1.name == 'Samsung s24'
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    assert keyboard1.name == 'Thor'
    assert keyboard1.price == 10000
    assert keyboard1.quantity == 7
    assert keyboard1.language == 'EN'


def test_rename_item():
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 10000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ROOT_DIR.joinpath('electronics-shop-project', 'src', 'items.csv'))
    assert len(Item.all) == 4
    assert Item.all[-1].name == 'Клавиатура'


def test_instantiate_from_csv_error():
    try:
        Item.instantiate_from_csv(ROOT_DIR.joinpath('electronics-shop-project', 'src', 'items_filed.csv'))
    except Exception as ex:
        assert ex == Exception('InstantiateCSVError: Файл item.csv поврежден')


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5') == 5


def test_repr():
    item2 = Item('Ноутбук', 20000, 5)
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"
    assert repr(phone1) == "Phone('Samsung s24', 120000, 5, 2)"
    assert repr(keyboard1) == "Keyboard('Thor', 10000, 7)"


def test_str():
    assert str(item2) == 'Ноутбук'
    assert str(phone1) == 'Samsung s24'
    assert str(keyboard1) == 'Thor'


def test_add_quantity():
    assert item2.quantity + phone1.quantity == 10


def test_set_number_of_sim():
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_change_language():
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'
