

from calculator import Caliculator

import pytest

def test_multiplication_1():
    caliculator_multiplication_1 = Caliculator("multiplication", 12,5)
    assert caliculator_multiplication_1.caliculate_result() == 60

def test_multiplication_2():
    caliculator_multiplication_2 = Caliculator("multiplication", 2,-9)
    assert caliculator_multiplication_2.caliculate_result() == -18


def test_multiplication_3():
    caliculator_multiplication_3 = Caliculator("multiplication", 2,-11)
    assert not caliculator_multiplication_3.caliculate_result() == -22


def test_multiplication_4():
    caliculator_multiplication_4 = Caliculator("multiplication", 3,4)
    assert not caliculator_multiplication_4.caliculate_result() == 12


