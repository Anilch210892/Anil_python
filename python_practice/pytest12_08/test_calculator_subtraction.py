
from calculator import Caliculator

import pytest


def test_subtraction_1():
    caliculator_subtraction_1 = Caliculator("subtraction",10,-13)
    assert caliculator_subtraction_1.caliculate_result()==23


def test_subtraction_2():
    caliculator_subtraction_2 = Caliculator("subtraction", 5,23)
    assert caliculator_subtraction_2.caliculate_result() == -18


def test_subtraction_3():
    caliculator_subtraction_3 = Caliculator("subtraction", 25, 36)
    assert caliculator_subtraction_3.caliculate_result() == -8


def test_subtraction_3():
    caliculator_subtraction_3 = Caliculator("subtraction", 25, 36)
    assert not caliculator_subtraction_3.caliculate_result() == -11


def test_subtraction_4():
    caliculator_subtraction_4 = Caliculator("subtraction", 5,-6)
    assert not caliculator_subtraction_4.caliculate_result() == 11



