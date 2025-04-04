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

def test_calculate_pay_basic(set_data):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == 220.0

def test_calculate_pay_zero_hours(set_data):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data
    employee1.getHoursOne = lambda: 0
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == 0.0

@pytest.fixture
def set_more_data():
    employees = [Employee("John", "Doe", "1", "100", "40", "0"), Employee("Jane", "Smith", "2", "120", "30", "10")]
    pay_list = [220.0, 150.0]
    return employees, pay_list

@patch("builtins.open", new_callable=mock_open)
def test_format_output(file, set_more_data):
    employees, pay_list = set_more_data
    FormatOutput(employees, pay_list)
    
    # Check that open was called to create the file
    file.assert_called_once_with("payReport.txt", 'w')
    
    # Check if content was written correctly to the file
    file().write.assert_any_call("Employee Name: John\n")
    file().write.assert_any_call("Employee ID: 1\n")
    file().write.assert_any_call("Earned this pay period: 220.00\n")