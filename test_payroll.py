

import os
import pytest
from payroll import CalculatePay, FormatOutput
from classes import Employee, Insurance

# -----------------------
# Data Flow & Control Flow Testing for CalculatePay
# -----------------------

def test_calculate_pay_normal():
    """
    Test CalculatePay with typical (nonzero) hours and pay values.
    This test ensures that the values defined in Employee and Insurance objects
    are correctly used (data flow) to produce the expected result.
    """
    # Create an employee with specified hours.
    # Note: Hours and pay are provided as strings (as per your code)
    employee = Employee("John", "001", "10", "8", "5", "2")
    # Create dummy insurances with known pay rates.
    insurance1 = Insurance("Insure1", "20")  # $20 per hour
    insurance2 = Insurance("Insure2", "15")  # $15 per hour
    insurance3 = Insurance("Insure3", "10")  # $10 per hour

    # Expected: (8 * 20) + (5 * 15) + (2 * 10)
    expected = 8 * 20 + 5 * 15 + 2 * 10
    result = CalculatePay(employee, insurance1, insurance2, insurance3)
    assert result == expected

def test_calculate_pay_edge_case():
    """
    Data Flow test for CalculatePay with zero hours and zero pay.
    This test checks that even edge (zero) values propagate correctly.
    """
    employee = Employee("Zero", "000", "0", "0", "0", "0")
    insurance = Insurance("None", "0")
    expected = 0.0
    result = CalculatePay(employee, insurance, insurance, insurance)
    assert result == expected

# -----------------------
# Testing FormatOutput (Control Flow in loops and file output)
# -----------------------

def test_format_output(tmp_path):
    """
    Test FormatOutput to ensure that:
      - The file 'payReport.txt' is created.
      - The content includes the employee details and correctly computed totals.
    This test uses a temporary directory to avoid interfering with real files.
    """
    # Change to temporary directory using tmp_path fixture.
    old_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        # Create dummy employees.
        employee1 = Employee("Alice", "002", "100", "4", "6", "3")
        employee2 = Employee("Bob", "003", "80", "5", "5", "2")
        employees = [employee1, employee2]
        # Provide a pay list (these numbers are what FormatOutput writes)
        pay_list = [100.0, 200.0]
        
        # Call the function that writes the report.
        FormatOutput(employees, pay_list)
        
        # Verify the file was created.
        report_file = tmp_path / "payReport.txt"
        assert report_file.exists()
        
        # Read and check the content.
        content = report_file.read_text()
        # Check header, employee details, and total pay.
        assert "--- Pay Report for all employees this period ---" in content
        assert "Employee Name: Alice" in content
        assert "Employee ID: 002" in content
        assert "Pay Percentage: 100%" in content
        assert "Earned this pay period: 100.00" in content
        assert "Employee Name: Bob" in content
        assert "Employee ID: 003" in content
        assert "Pay Percentage: 80%" in content
        assert "Earned this pay period: 200.00" in content
        assert "Total amount paid to employees this period: 300.00" in content
    finally:
        os.chdir(old_dir)

def test_format_output_empty_lists(tmp_path):
    """
    Control Flow test: When provided with empty employee and pay lists,
    FormatOutput should still create a file that includes the header and shows a total of 0.00.
    """
    old_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        FormatOutput([], [])
        report_file = tmp_path / "payReport.txt"
        assert report_file.exists()
        content = report_file.read_text()
        assert "--- Pay Report for all employees this period ---" in content
        assert "Total amount paid to employees this period: 0.00" in content
    finally:
        os.chdir(old_dir)
