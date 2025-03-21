class Employee:
    def __init__(self, name, id, pay_percent, hoursOne, hoursTwo, hoursThree):
        self.name = name
        self.id = id
        self.pay_percent = pay_percent
        self.insuranceOneHours = hoursOne
        self.insuranceTwoHours = hoursTwo
        self.insuranceThreeHours = hoursThree
    
    def addHoursOne(newHours):
        insuranceOneHours += newHours
    
    def addHoursTwo(newHours):
        insuranceTwoHours += newHours
    
    def addHoursThree(newHours):
        insuranceThreeHours += newHours

    def getHoursOne(self):
        return self.insuranceOneHours
    
    def getHoursTwo(self):
        return self.insuranceTwoHours
    
    def getHoursThree(self):
        return self.insuranceThreeHours
    
    def getPercent(self):
        return self.pay_percent
    
    def getName(self):
        return self.name

class Insurance:
    def __init__(self, name, payAmount):
        self.name = name
        self.payAmount = payAmount

    def getName(self):
        return self.name

    def getPay(self):
        return self.payAmount