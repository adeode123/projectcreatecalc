""" Test for Calculator class and child classes"""
import random
import pytest
from calculator.main import Calculator, Add, Subtract, Multiply, Divide
import pandas as pd


def divide_helper(*values):
    """ divide helper """
    result = 1
    for val in values:
        result = result / val
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


@pytest.fixture(name="random_values_add")
def fixture_random_values_add():
    """ Fixture to generate two random values """
    df = pd.read_csv('C:/Users/Abosede/PycharmProjects/calc_part2/tests/input_add.csv')
    number1, number2, operation = 0, 0, ""
    for index, row in df.iterrows():
        number1 = row[0]
        number2 = row[1]
        operation = row[2]
    return number1, number2, operation


@pytest.fixture(name="random_values_subtract")
def fixture_random_values_subtract():
    """ Fixture to generate two random values """
    df = pd.read_csv('C:/Users/Abosede/PycharmProjects/calc_part2/tests/input_subtract.csv')
    number1, number2, operation = 0, 0, ""
    for index, row in df.iterrows():
        number1 = row[0]
        number2 = row[1]
        operation = row[2]
    return number1, number2, operation


@pytest.fixture(name="random_values_multiply")
def fixture_random_values_multiply():
    """ Fixture to generate two random values """
    df = pd.read_csv('C:/Users/Abosede/PycharmProjects/calc_part2/tests/input_multiply.csv')
    number1, number2, operation = 0, 0, ""
    for index, row in df.iterrows():
        number1 = row[0]
        number2 = row[1]
        operation = row[2]
    return number1, number2, operation


@pytest.fixture(name="random_values_divide")
def fixture_random_values_divide():
    """ Fixture to generate two random values """
    df = pd.read_csv('C:/Users/Abosede/PycharmProjects/calc_part2/tests/input_divide.csv')
    number1, number2, operation = 0, 0, ""
    for index, row in df.iterrows():
        number1 = row[0]
        number2 = row[1]
        operation = row[2]
    return number1, number2, operation


def test_calculator_addition(random_values_add):
    """ Test calculator method addition """
    number1, number2, operation = random_values_add
    temp = (number1, number2)
    calculator_obj = Calculator.create(*temp)
    data = [[3, 2], [5, 6]]
    df = pd.DataFrame(data)
    df.to_csv('existing.csv', mode='a', index=False, header=False)
    assert calculator_obj.factory(operation) == sum(temp)


def test_calculator_subtraction(random_values_subtract):
    """ Test calculator method subtraction """
    number1, number2, operation = random_values_subtract
    temp = (number1, number2)
    calculator_obj = Calculator.create(*temp)
    assert calculator_obj.factory(operation) == subtract_helper(*temp)


def test_calculator_multiplication(random_values_multiply):
    """ Test calculator method multiplication """
    number1, number2, operation = random_values_multiply
    temp = (number1, number2)
    calculator_obj = Calculator.create(*temp)
    assert calculator_obj.factory(operation) == multiply_helper(*temp)


def test_calculator_division(random_values_divide):
    """ Test calculator method division """
    number1, number2, operation = random_values_divide
    temp = (number1, number2)
    calculator_obj = Calculator.create(*temp)
    assert calculator_obj.factory(operation) == divide_helper(*temp)


@pytest.fixture(name="two_random_values")
def fixture_two_random_values():
    """ Fixture to generate two random values """
    return random.randint(1, 10), random.randint(1, 20)


@pytest.fixture(name="calculator_object")
def fixture_calculator_object(two_random_values):
    """ Fixture to generate calculator object """
    num_1, num_2 = two_random_values
    return Calculator(num_1, num_2)


@pytest.fixture(name="add")
def fixture_add(two_random_values):
    """ Fixture to generate calculator object """
    num_1, num_2 = two_random_values
    return Add(num_1, num_2)


def test_get_history(calculator_object):
    """ Test get history method """
    assert calculator_object.get_history() == calculator_object.calculator_history


def test_get_last_calculation(calculator_object):
    """ Test get last calculations method """
    calculator_object.factory("add")
    assert calculator_object.get_last_calculation() == calculator_object.calculator_history[-1]


def test_get_first_calculation(calculator_object):
    """ Test get first calculations method """
    # first calculations - Add
    calculator_object.factory("add")
    # second calculations - Divide
    calculator_object.factory("divide")
    assert isinstance(calculator_object.get_first_calculation().get("object"), Add)


def test_add_calculation_to_history(add, calculator_object):
    """ Test add calculations to history """
    result = add.add()
    record = {
            "object": add,
            "result": result
        }
    calculator_object.add_calculation_to_history(record)
    assert record in calculator_object.calculator_history


def test_get_last_calculation_result(calculator_object):
    """ Test get last calculations result method """
    result = calculator_object.factory("add")
    assert calculator_object.get_last_calculation_result() == result


def test_get_last_calculation_object(add, calculator_object):
    """ Test get last calculations object method """
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


def test_calculator_addition(calculator_object, two_random_values):
    """ Test calculator static method addition """
    num_1, num_2 = two_random_values
    assert calculator_object.addition(num_1, num_2) == num_1 + num_2


def test_calculator_subtraction(calculator_object, two_random_values):
    """ Test calculator static method subtraction """
    num_1, num_2 = two_random_values
    assert calculator_object.subtraction(num_1, num_2) == num_1 - num_2


def test_calculator_multiplication(calculator_object, two_random_values):
    """ Test calculator static method multiplication """
    num_1, num_2 = two_random_values
    assert calculator_object.multiplication(num_1, num_2) == num_1 * num_2


def test_calculator_division(calculator_object, two_random_values):
    """ Test calculator static method division """
    num_1, num_2 = two_random_values
    assert calculator_object.division(num_1, num_2) == num_1 / num_2


def test_calculator_division_by_zero_not_allowed(calculator_object, two_random_values):
    """ Test calculator static method division by 0 returns None """
    num_1, _ = two_random_values
    assert calculator_object.division(num_1, 0) is None


def test_add_calculator_factory(two_random_values):
    """ Test calculator object factory for add operation """
    num_1, num_2 = two_random_values
    calculator = Calculator(num_1, num_2)
    assert calculator.factory("add") == num_1 + num_2


def test_subtract_calculator_factory(two_random_values):
    """ Test calculator object factory for subtract operation """
    num_1, num_2 = two_random_values
    calculator = Calculator(num_1, num_2)
    assert calculator.factory("subtract") == num_1 - num_2


def test_multiply_calculator_factory(two_random_values):
    """ Test calculator object factory for multiply operation """
    num_1, num_2 = two_random_values
    calculator = Calculator(num_1, num_2)
    assert calculator.factory("multiply") == num_1 * num_2


def test_divide_calculator_factory(two_random_values):
    """ Test calculator object factory for divide operation """
    num_1, num_2 = two_random_values
    calculator_obj = Calculator(num_1, num_2)
    assert calculator_obj.factory("divide") == num_1 / num_2


def test_calculator_factory_return_invalid_operation(two_random_values):
    """ Test calculator factory returns Invalid operation when the operation is not supported"""
    num_1, num_2 = two_random_values
    calculator_obj = Calculator(num_1, num_2)
    assert calculator_obj.factory("random operation") == "Invalid Operation"


def test_add_class(two_random_values):
    """ Test add class """
    num_1, num_2 = two_random_values
    add = Add(num_1, num_2)
    assert add.add() == num_1 + num_2


def test_subtract_class(two_random_values):
    """ Test subtract class """
    num_1, num_2 = two_random_values
    subtract = Subtract(num_1, num_2)
    assert subtract.subtract() == num_1 - num_2


def test_multiply_class(two_random_values):
    """ Test multiply class"""
    num_1, num_2 = two_random_values
    multiply = Multiply(num_1, num_2)
    assert multiply.multiply() == num_1 * num_2


def test_divide_class(two_random_values):
    """ Test divide class """
    num_1, num_2 = two_random_values
    divide = Divide(num_1, num_2)
    assert divide.divide() == num_1 / num_2


def test_divide_zero_class(two_random_values):
    """ Test Divide class when dividing by 0 """
    num_1, _ = two_random_values
    num_2 = 0
    divide = Divide(num_1, num_2)
    assert divide.divide() is None
