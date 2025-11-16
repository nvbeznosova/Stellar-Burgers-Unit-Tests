import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def ingredient_sauce():
    ing = Mock()
    ing.get_name.return_value = "ketchup"
    ing.get_price.return_value = 50
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ing

@pytest.fixture
def ingredient_filling():
    ing = Mock()
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 150
    ing.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ing

def test_set_buns(bun_mock):
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock

def test_add_and_remove_ingredient(bun_mock, ingredient_sauce, ingredient_filling):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    assert len(burger.ingredients) == 2
    burger.remove_ingredient(0)
    assert burger.ingredients == [ingredient_filling]

def test_move_ingredient(bun_mock, ingredient_sauce, ingredient_filling):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[1] == ingredient_sauce

@pytest.mark.parametrize("ingredients,expected_price", [
    ([], 200),  # только булка (100*2)
    ([50], 250),  # булка + соус
    ([150], 350),  # булка + начинка
    ([50, 150], 400),  # булка + соус + начинка
])
def test_get_price(bun_mock, ingredients, expected_price):
    burger = Burger()
    burger.set_buns(bun_mock)
    for price in ingredients:
        ing = Mock()
        ing.get_price.return_value = price
        ing.get_name.return_value = "mock"
        ing.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(ing)
    assert burger.get_price() == expected_price

def test_get_receipt(bun_mock, ingredient_sauce):
    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_sauce)
    receipt = burger.get_receipt()
    assert "test bun" in receipt
    assert "ketchup" in receipt
    assert "Price: 250" in receipt