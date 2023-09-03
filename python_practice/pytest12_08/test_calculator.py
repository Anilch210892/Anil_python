from calculator import Caliculator
# module , Class
from calculator import *
# * will import all classes

import pytest

def test_add_1():
    caliculator_add_1 = Caliculator("add",1,2)
    assert caliculator_add_1.caliculate_result()==3

def test_add_2():
    caliculator_add_1 = Caliculator("add",-1,12)
    assert caliculator_add_1.caliculate_result()==8

def test_add_3():
    caliculator_add_1 = Caliculator("add",2,5)
    assert caliculator_add_1.caliculate_result()==3

def test_add_4():
    caliculator_add_1 = Caliculator("add",2,15)
    assert not caliculator_add_1.caliculate_result()==16

def test_add_5():
    caliculator_add_1 = Caliculator("add",6,-13)
    assert caliculator_add_1.caliculate_result()==-7


def test_subtraction_1():
    caliculator_subtraction_1 = Caliculator("subtraction",6,-13)
    assert caliculator_subtraction_1.caliculate_result()==19

def test_subtraction_2():
    caliculator_subtraction_2 = Caliculator("subtraction",-1,-6)
    assert caliculator_subtraction_2.caliculate_result()==-7

def test_subtraction_3():
    caliculator_subtraction_3 = Caliculator("subtraction",2,3)
    assert caliculator_subtraction_3.caliculate_result()==-1


def test_multiplication_3():
    caliculator_multiplication_3 = Caliculator("multiplication", 2, 5)
    assert caliculator_multiplication_3.caliculate_result() == 10

def test_multiplication_4():
    caliculator_multiplication_4 = Caliculator("multiplication", 3, -9)
    assert caliculator_multiplication_4.caliculate_result() == -27


def test_division_1():
    caliculator_division_1 = Caliculator("division", 2,3)
    assert caliculator_division_1.caliculate_result() == 0.66

def test_division_2():
    caliculator_division_2 = Caliculator("division", 15,5)
    assert caliculator_division_2.caliculate_result() == 3

def test_division_3():
    caliculator_division_3 = Caliculator("division", 2,0)
    assert caliculator_division_3.caliculate_result() = = "invalid division"

def test_modulus_1():
    caliculator_modulus__1 = Caliculator("modulus_", 2,0)
    assert caliculator_modulus__1.caliculate_result() == "invalid operation"



















