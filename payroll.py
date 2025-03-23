import classes

# Function to calculate pay of employee using insurances
def CalculatePay(employee, insuranceOne, insuranceTwo, insuranceThree):
    # Cast as floats because there was an error where object reference had issues when sourced from list
    employee_pay = (float(employee.getHoursOne()) * float(insuranceOne.getPay())) + (float(employee.getHoursTwo()) * \
        float(insuranceTwo.getPay())) + (float(employee.getHoursThree()) * float(insuranceThree.getPay()))
    return employee_pay

# Function to format output
def FormatOutput(employeeList, payList):
    with open("payReport.txt", 'w') as f:
        f.write("--- Pay Report for all employees this period ---\n\n")
        totalPay = 0
        k = 0
        for obj in employeeList:
            f.write("Employee Name: " + obj.getName() + "\n")
            f.write("Employee ID: " + obj.getID() + "\n")
            f.write("Pay Percentage: " + obj.getPercent() + "%" + "\n")
            f.write("Earned this pay period: " + f"{payList[k]:.2f}" + "\n\n")
            totalPay += payList[k]
            k += 1
        f.write("Total amount paid to employees this period: " + f"{totalPay:.2f}" + "\n\n")
        f.write("--- End of report. ---")
    return

# Create empty list for employees
employees = []
insurances = []

# Read lines in employee file and instantiate a class with those values
with open('employees.txt', 'r') as file:
    for line in file:
        #print(line.strip()) <----debug
        currentEmployee = line.split()
        #print(currentEmployee) <----debug
        employee = classes.Employee(currentEmployee[0], currentEmployee[1], currentEmployee[2], \
            currentEmployee[3], currentEmployee[4], currentEmployee[5])
        employees.append(employee)

# Read lines in insurance file and instantiate a class with those values
with open('insurances.txt', 'r') as file:
    for line in file:
        currentInsurance = line.split()
        insurance = classes.Insurance(currentInsurance[0], currentInsurance[1])
        insurances.append(insurance)

# Assign objects in lists to variables
Mike = employees[0]
Debra = employees[1]
InsureOne = insurances[0]
InsureTwo = insurances[1]
InsureThree = insurances[2]

# Calculate pay for employees
payList = []
for obj in employees:
    payList.append(CalculatePay(obj, InsureOne, InsureTwo, InsureThree))

print("Generating pay report for employees...")
FormatOutput(employees, payList)
 
print("Report generates please see 'payReport.txt'.")