import pytest
from unittest.mock import Mock
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