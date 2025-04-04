import pytest
from unittest.mock import mock_open, patch
from payroll import CalculatePay, FormatOutput
from classes import Employee, Insurance

@pytest.fixture
def set_data():
    employee1 = Employee("John", "Doe", "1", "100", "40", "0")
    employee2 = Employee("Jane", "Smith", "2", "120", "30", "10")
    insurance1 = Insurance("Insurance1", "5.0")
    insurance2 = Insurance("Insurance2", "4.0")
    insurance3 = Insurance("Insurance3", "3.0")

    return employee1, employee2, insurance1, insurance2, insurance3

def test_calculate_pay_employee1(set_data):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{6.60:.2f}"

def test_calculate_pay_employee2(set_data):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data
    result = CalculatePay(employee2, insurance1, insurance2, insurance3)
    assert result == f"{15:.2f}"

def test_calculate_pay_zero_hours(set_data):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data
    employee1.getHoursOne = lambda: 0
    employee1.getHoursTwo = lambda: 0
    employee1.getHoursThree = lambda: 0
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{0:.2f}"