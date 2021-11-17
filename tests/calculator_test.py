""" Test for Calculator class and child classes"""
import random
import pytest
from calculator.main import Calculator, Add, Subtract, Multiply, Divide


def divide_helper(*values):
    """ divide helper """
    result = 1
    for val in values:
        result = val / result
    return result


def multiply_helper(*values):
    """ Multiply helper """
    print(f"Multiply helper values are {list(values)}")
    result = 1
    for val in values:
        result = val * result
    return result


def subtract_helper(*values):
    """ Subtract helper """
    result = 0
    for val in values:
        result = val - result
    return result


@pytest.fixture(name="random_values")
def fixture_random_values():
    """ Fixture to generate two random values """
    num_values = random.randint(1, 10)
    return (random.randint(1, 20) for _ in range(num_values))


@pytest.fixture(name="random_values_with_zero")
def fixture_random_values():
    """ Fixture to generate two random values """
    num_values = random.randint(1, 10)
    return (0 for _ in range(num_values))


@pytest.fixture(name="calculator_object")
def fixture_calculator_object(random_values):
    """ Fixture to generate calculator object """
    return Calculator.create(*random_values)


@pytest.fixture(name="add")
def fixture_add(random_values):
    """ Fixture to generate calculator object """
    return Add(random_values)


def test_get_history(calculator_object):
    """ Test get history method """
    assert calculator_object.get_history() == calculator_object.calculator_history


def test_get_last_calculation(calculator_object):
    """ Test get last calculation method """
    calculator_object.factory("add")
    assert calculator_object.get_last_calculation() == calculator_object.calculator_history[-1]


def test_get_first_calculation(calculator_object):
    """ Test get first calculation method """
    # first calculation - Add
    calculator_object.factory("add")
    # second calculation - Divide
    calculator_object.factory("divide")
    assert isinstance(calculator_object.get_first_calculation().get("object"), Add)


def test_add_calculation_to_history(add, calculator_object):
    """ Test add calculation to history """
    result = add.add()
    record = {
            "object": add,
            "result": result
        }
    calculator_object.add_calculation_to_history(record)
    assert record in calculator_object.calculator_history


def test_get_last_calculation_result(calculator_object):
    """ Test get last calculation result method """
    result = calculator_object.factory("add")
    assert calculator_object.get_last_calculation_result() == result


def test_get_last_calculation_object(add, calculator_object):
    """ Test get last calculation object method """
    result = add.add()
    record = {
        "object": add,
        "result": result
    }
    calculator_object.add_calculation_to_history(record)
    assert calculator_object.get_last_calculation_object() == add


def test_clear_history(calculator_object):
    """ Test clear history of calculator """
    calculator_object.factory("add")
    calculator_object.factory("multiply")
    calculator_object.clear_history()
    assert len(calculator_object.get_history()) == 0


def test_count_history(calculator_object):
    """ Test count history of calculator """
    calculator_object.factory("add")
    calculator_object.factory("multiply")
    assert calculator_object.count_history() == 2


def test_calculator_addition(calculator_object, random_values):
    """ Test calculator static method addition """
    assert calculator_object.addition(*random_values) == sum(random_values)


def test_calculator_subtraction(calculator_object, random_values):
    """ Test calculator static method subtraction """
    assert calculator_object.subtraction(*random_values) == subtract_helper(*random_values)


def test_calculator_multiplication(calculator_object, random_values):
    """ Test calculator static method multiplication """
    assert calculator_object.multiplication(*random_values) == multiply_helper(*random_values)


def test_calculator_division(calculator_object, random_values):
    """ Test calculator static method division """
    assert calculator_object.division(*random_values) == divide_helper(*random_values)


def test_calculator_division_by_zero_not_allowed(calculator_object, random_values_with_zero):
    """ Test calculator static method division by 0 returns None """
    assert calculator_object.division(*random_values_with_zero) is None


def test_add_calculator_factory(random_values):
    """ Test calculator object factory for add operation """
    res = tuple(random_values)
    calculator = Calculator.create(*res)
    assert calculator.factory("add") == sum(res)


def test_subtract_calculator_factory(random_values):
    """ Test calculator object factory for subtract operation """
    res = tuple(random_values)
    calculator = Calculator.create(*res)
    assert calculator.factory("subtract") == subtract_helper(*res)


def test_multiply_calculator_factory(random_values):
    """ Test calculator object factory for multiply operation """
    res = tuple(random_values)
    calculator = Calculator.create(*res)
    assert calculator.factory("multiply") == multiply_helper(*res)


def test_divide_calculator_factory(random_values):
    """ Test calculator object factory for divide operation """
    res = tuple(random_values)
    calculator = Calculator.create(*res)
    assert calculator.factory("divide") == divide_helper(*res)


def test_calculator_factory_return_invalid_operation(random_values):
    """ Test calculator factory returns Invalid operation when the operation is not supported"""
    calculator_obj = Calculator.create(*random_values)
    assert calculator_obj.factory("random operation") == "Invalid Operation"


def test_add_class(random_values):
    """ Test add class """
    temp = tuple(random_values)
    add = Add.create(*temp)
    assert add.add() == sum(temp)


def test_subtract_class(random_values):
    """ Test subtract class """
    temp = tuple(random_values)
    subtract = Subtract.create(*temp)
    assert subtract.subtract() == subtract_helper(*temp)


def test_multiply_class(random_values):
    """ Test multiply class"""
    temp = tuple(random_values)
    multiply = Multiply.create(*temp)
    assert multiply.multiply() == multiply_helper(*temp)


def test_divide_class(random_values):
    """ Test divide class """
    temp = tuple(random_values)
    divide = Divide.create(*temp)
    assert divide.divide() == divide_helper(*temp)


def test_divide_class_with_zero(random_values_with_zero):
    """ Test divide class """
    temp = tuple(random_values_with_zero)
    divide = Divide.create(*temp)
    assert divide.divide() is None
