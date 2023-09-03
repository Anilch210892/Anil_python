
from calculator import Caliculator

import pytest




def test_modulus_1():
    caliculator_modulus__1 = Caliculator("modulus_", 12,6)
    assert caliculator_modulus__1.caliculate_result() == "invalid operation"


def test_modulus_2():
    caliculator_modulus__2 = Caliculator("modulus_", 9, 0)
    assert not caliculator_modulus__2.caliculate_result() == "invalid operation"

