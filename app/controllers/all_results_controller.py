from app.controllers.controller import ControllerBase
from calculator.main import Calculation, Calculator
import pandas as pd
from flask import render_template, request, flash, redirect, url_for, session


class ResultsController(ControllerBase):
    @staticmethod
    def get():
        df = pd.read_csv(Calculator.history_log_file)
        all_results = df.values.tolist()
        headers = df.columns
        return render_template('all_results.html', all_results=all_results, headers=headers)