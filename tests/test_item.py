from src.item import Item
item1 = Item('Смартфон', 10000, 20)
item2 = Item('Ноутбук', 20000, 5)
item1.pay_rate = 0.8
item2.pay_rate = 0.5


def test_item():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item2.name == 'Ноутбук'
    assert item2.price == 20000
    assert item2.quantity == 5


def test_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 10000.0
