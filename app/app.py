"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.all_results_controller import ResultsController
from app.controllers.pylint_controller import PylintController
from app.controllers.design_controller import DesignController
from app.controllers.oop_controller import OOPController
from app.controllers.test_controller import TestController
from werkzeug.debug import DebuggedApplication


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/results", methods=['GET'])
def get_calculator_results():
    return ResultsController.get()

@app.route("/test-route", methods=['GET'])
def get_test_route():
    return TestController.get()

@app.route("/pylint", methods=['GET'])
def get_pylint_route():
    return PylintController.get()

@app.route("/oop", methods=['GET'])
def get_oop_route():
    return OOPController.get()

@app.route("/design", methods=['GET'])
def get_design_route():
    return DesignController.get()
