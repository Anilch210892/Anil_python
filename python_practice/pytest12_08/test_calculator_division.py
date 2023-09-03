

from calculator import Caliculator

import pytest


def test_division_1():
    caliculator_division_1 = Caliculator("division", 12,3)
    assert caliculator_division_1.caliculate_result() == 4

def test_division_2():
    caliculator_division_2 = Caliculator("division", 25,5)
    assert caliculator_division_2.caliculate_result() == 5

def test_division_3():
    caliculator_division_3 = Caliculator("division", 25,10)
    assert not caliculator_division_3.caliculate_result() == 2.5

def test_division_4():
    caliculator_division_4 = Caliculator("division", 250,50)
    assert not caliculator_division_4.caliculate_result() == 5


