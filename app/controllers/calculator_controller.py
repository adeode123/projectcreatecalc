from app.controllers.controller import ControllerBase
from calculator.main import Calculator
from flask import render_template, request, flash, redirect, url_for, session


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            Calculator.get_history_from_csv()
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            # my_tuple = (value1, value2)
            # this will call the correct operation
            #getattr(Calculator, operation)(my_tuple)
            calculator = Calculator.create(value1, value2)
            calculator.factory(operation)
            print("operation is " + operation)
            # print("result is " + result)
            result = str(Calculator.get_last_calculation_result())
            # print("result is " + result)
            # Hey if you copy this it will not work you need to think about it
            # data = {
            #     'value1': [value1],
            #     'value2': [value2],
            #     'operation': [operation]
            # }
            calculator.write_history_to_csv()
            return render_template('result.html', data=Calculator.get_history(), value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')