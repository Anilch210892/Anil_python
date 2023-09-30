

from calculator import Caliculator

import pytest

@pytest.mark.int_add
def test_add():
    calculator_add = Caliculator("add",1,2)
    assert calculator_add.caliculate_result() == 3



@pytest.mark.float_add
def test_add():
    caliculator_add = Caliculator("add",1,3.5)
    assert caliculator_add.caliculate_result() == 4.5


@pytest.mark.float_add
def test_add():
    caliculator_add = Caliculator("add", 3,8)
    assert caliculator_add.caliculate_result() == 11


@pytest.mark.float_add
def test_add():
    caliculator_add = Caliculator("add", 3.7,5.6)
    assert caliculator_add.caliculate_result() == 9.3




