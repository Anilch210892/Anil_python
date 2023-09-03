from calculator import Caliculator

import pytest


def test_add_1():
    caliculator_add_1 = Caliculator("add",13,2)
    assert caliculator_add_1.caliculate_result()==15

def test_add_2():
    caliculator_add_2 = Caliculator("add",7,2)
    assert caliculator_add_2.caliculate_result()==9

def test_add_3():
    caliculator_add_3 = Caliculator("add",10,-2)
    assert not caliculator_add_3.caliculate_result()==8

def test_add_4():
    caliculator_add_4 = Caliculator("add",-9,-10)
    assert not caliculator_add_4.caliculate_result()==-19






