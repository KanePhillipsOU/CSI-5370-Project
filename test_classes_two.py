import pytest
from unittest.mock import mock_open, patch
from payroll import CalculatePay, FormatOutput
from classes import Employee, Insurance

# Fixture for basic test
@pytest.fixture
def set_data_one():
    employee1 = Employee("Daniel", "001", "1", "100", "40", "0")
    employee2 = Employee("Dakota", "002", "2", "120", "30", "10")
    insurance1 = Insurance("Insurance1", "5")
    insurance2 = Insurance("Insurance2", "4")
    insurance3 = Insurance("Insurance3", "3")

    return employee1, employee2, insurance1, insurance2, insurance3

# Fixture for 0 percentage
@pytest.fixture
def set_data_two():
    employee1 = Employee("Daniel", "001", "0", "100", "40", "0")
    employee2 = Employee("Dakota", "002", "0", "120", "30", "10")
    insurance1 = Insurance("Insurance1", "5")
    insurance2 = Insurance("Insurance2", "4")
    insurance3 = Insurance("Insurance3", "3")
    
    return employee1, employee2, insurance1, insurance2, insurance3

# Fixture for negative hours
@pytest.fixture
def set_data_three():
    employee1 = Employee("Daniel", "001", "1", "-10", "-40", "0")
    employee2 = Employee("Dakota", "002", "2", "-120", "-30", "-10")
    insurance1 = Insurance("Insurance1", "5")
    insurance2 = Insurance("Insurance2", "4")
    insurance3 = Insurance("Insurance3", "3")

    return employee1, employee2, insurance1, insurance2, insurance3

# Fixture for string instead of number
@pytest.fixture
def set_data_four():
    employee1 = Employee("Daniel", "001", "1", "ten", "-40", "0")
    employee2 = Employee("Dakota", "002", "2", "five", "-30", "-10")
    insurance1 = Insurance("Insurance1", "5")
    insurance2 = Insurance("Insurance2", "4")
    insurance3 = Insurance("Insurance3", "3")

    return employee1, employee2, insurance1, insurance2, insurance3

# Fixture for empty values
@pytest.fixture
def set_data_five():
    employee1 = Employee("Daniel", "001", "", "100", "40", "0")
    employee2 = Employee("Dakota", "002", "0", "120", "30", "")
    insurance1 = Insurance("Insurance1", "")
    insurance2 = Insurance("Insurance2", "4")
    insurance3 = Insurance("Insurance3", "3")

    return employee1, employee2, insurance1, insurance2, insurance3

# Test for basic functionality
def test_calculate_pay_employee1(set_data_one):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_one
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{6.60:.2f}"

# Test that employee 2 is working
def test_calculate_pay_employee2(set_data_one):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_one
    result = CalculatePay(employee2, insurance1, insurance2, insurance3)
    assert result == f"{15:.2f}"

# Test that no hours means 0 pay (verifies hours are being applied)
def test_calculate_pay_zero_hours(set_data_one):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_one
    employee1.getHoursOne = lambda: 0
    employee1.getHoursTwo = lambda: 0
    employee1.getHoursThree = lambda: 0
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{0:.2f}"

# Test that percent = 0 makes pay go to 0 (verifies percentage is being applied)
def test_zero_percent(set_data_two):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_two
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{0:.2f}"

# Test to verify that negative hours is replaced with 0 pay
def test_negative_hours(set_data_three):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_three
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    result2 = CalculatePay(employee2, insurance1, insurance2, insurance3)
    assert result == f"{0:.2f}"
    assert result2 == f"{0:.2f}"

# Test to verify strings entered as values still functions
def test_zero_percent(set_data_four):
    employee1, employee2, insurance1, insurance2, insurance3 = set_data_four
    result = CalculatePay(employee1, insurance1, insurance2, insurance3)
    assert result == f"{0:.2f}"
    # Currently fails