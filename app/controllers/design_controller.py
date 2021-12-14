from app.controllers.controller import ControllerBase
from calculator.main import Calculation, Calculator
import pandas as pd
from flask import render_template, request, flash, redirect, url_for, session


class DesignController(ControllerBase):
    @staticmethod
    def get():
        return render_template('design.html')