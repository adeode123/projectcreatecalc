from app.controllers.controller import ControllerBase
from calculator.main import Calculation, Calculator
import pandas as pd
from flask import render_template, request, flash, redirect, url_for, session


class TestController(ControllerBase):
    @staticmethod
    def get():
        return render_template('test.html')