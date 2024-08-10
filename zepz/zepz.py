import datetime
import operator
import re
import unittest
from typing import Any, Dict


class Spreadsheet:
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.format: Dict[str, str] = {}

    def get_formatted(self, index: str) -> str:
        value = self.evaluate_formula(index)
        if isinstance(value, (int, float)):
            format_spec = self.format.get(index, "%.2f")
            return format_spec % value
        elif isinstance(value, datetime.datetime):
            format_spec = self.format.get(index, "%Y-%m-%d")
            return value.strftime(format_spec)
        else:
            return str(value)

    def get_raw(self, index: str) -> str:
        return self.data.get(index, "")

    def set(self, index: str, raw: str) -> None:
        self.data[index] = raw

    def pythoset_format(self, index: str, type: str, spec: str) -> None:
        self.format[index] = spec

    def evaluate_formula(self, index: str) -> Any:
        formula = self.get_raw(index)
        if formula.startswith("="):
            formula = formula[1:]
            return self.evaluate_expression(formula)
        else:
            return formula

    def evaluate_expression(self, expression: str) -> Any:
        if "=" in expression:
            raise ValueError("Invalid expression")

        if expression.isdigit():
            return int(expression)
        elif re.match(r"\d+\.\d+", expression):
            return float(expression)
        elif re.match(r"\d{4}-\d{2}-\d{2}", expression):
            return datetime.datetime.strptime(expression, "%Y-%m-%d").date()

        if not expression.isdigit() and expression in self.data:
            return self.evaluate_formula(expression)

        tokens = expression.split()
        if len(tokens) == 3:
            left, operator_str, right = tokens
            operator_func = self.get_operator(operator_str)
            if operator_func:
                left_value_raw = self.evaluate_expression(left)
                right_value_raw = self.evaluate_expression(right)
                left_value = int(left_value_raw)
                right_value = int(right_value_raw)
                return operator_func(left_value, right_value)

        raise ValueError("Invalid expression")

    def get_operator(self, operator_str: str):
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        return operators.get(operator_str)


class SpreadsheetTests(unittest.TestCase):
    def setUp(self):
        self.spreadsheet = Spreadsheet()

    def test_get_formatted(self):
        self.spreadsheet.set("A1", "5")
        self.spreadsheet.set("A2", "10")
        self.spreadsheet.set("A3", "=A1 + A2")
        result = self.spreadsheet.get_formatted("A3")
        self.assertEqual(result, "15.00")

    def test_get_formatted_with_format_spec(self):
        self.spreadsheet.set("A1", "5")
        self.spreadsheet.set("A2", "10")
        self.spreadsheet.set("A3", "=A1 + A2")
        self.spreadsheet.set_format("A3", "number", "%.3f")
        result = self.spreadsheet.get_formatted("A3")
        self.assertEqual(result, "15.000")

    def test_get_raw(self):
        self.spreadsheet.set("A1", "5")
        result = self.spreadsheet.get_raw("A1")
        self.assertEqual(result, "5")

    def test_set(self):
        self.spreadsheet.set("A1", "5")
        result = self.spreadsheet.get_raw("A1")
        self.assertEqual(result, "5")


if __name__ == "__main__":
    unittest.main()
