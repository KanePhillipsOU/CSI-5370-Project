from classes import Employee, Insurance

def test_employee_getters():
    """
    Test that the Employee getter methods return the correct values.
    This checks the data flow from initialization through to the getter calls.
    """
    employee = Employee("Charlie", "004", "50", "10", "20", "30")
    assert employee.getName() == "Charlie"
    assert employee.getID() == "004"
    assert employee.getPercent() == "50"
    assert employee.getHoursOne() == "10"
    assert employee.getHoursTwo() == "20"
    assert employee.getHoursThree() == "30"

def test_insurance_getters():
    """
    Test that the Insurance getter methods return the correct values.
    """
    insurance = Insurance("TestInsurance", "25")
    assert insurance.getName() == "TestInsurance"
    assert insurance.getPay() == "25"
