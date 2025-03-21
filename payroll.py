import classes

# Function to calculate pay of employee using insurances
def CalculatePay(employee, insuranceOne, insuranceTwo, insuranceThree):
    # Cast as floats because there was an error where object reference had issues when sourced from list
    employee_pay = (float(employee.getHoursOne()) * float(insuranceOne.getPay())) + (float(employee.getHoursTwo()) * \
        float(insuranceTwo.getPay())) + (float(employee.getHoursThree()) * float(insuranceThree.getPay()))
    return employee_pay

# Create empty list for employees
employees = []

# Read lines in employee file and instantiate a class with those values
with open('employees.txt', 'r') as file:
    for line in file:
        #print(line.strip()) <----debug
        currentEmployee = line.split()
        i = 0
        #print(currentEmployee) <----debug
        employee = classes.Employee(currentEmployee[0], currentEmployee[1], currentEmployee[2], \
            currentEmployee[3], currentEmployee[4], currentEmployee[5])
        employees.append(employee)

#Check that list has employees stored for debugging
# for obj in employees:
#     print(obj.getName())


# Hard-coded employees and insurances
Mike = employees[0]
Debra = employees[1]

# TO-DO************: Import insurance list from txt file like employees
InsureOne = classes.Insurance("One", 134.29)
InsureTwo = classes.Insurance("Two", 147.23)
InsureThree = classes.Insurance("Three", 75.34)

mike_pay = CalculatePay(Mike, InsureOne, InsureTwo, InsureThree)
debra_pay = CalculatePay(Debra, InsureOne, InsureTwo, InsureThree)

print("Mike's pay is: " + str(mike_pay))
print("Debra's pay is: " + str(debra_pay))