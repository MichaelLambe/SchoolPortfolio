

class Employee:
    def __init__(self, fname:str,lname:str, id:int):
        self.fname = fname
        self.lname = lname
        self.id = id
    
    def __str__(self) -> str:
        return f'Employee: {self.fname} {self.lname} ({self.id})'

class WageEmployee(Employee):
    def __init__(self, fname:str, lname:str, id:int, hourly_wage:float, weekly_hours:float):
        super().__init__(fname, lname, id)
        self.hourly_wage = hourly_wage
        self.weekly_hours = weekly_hours
    
    def weekly_earnings(self):
        return '${:,.2f}'.format(self.weekly_hours * self.hourly_wage)
    
    def __str__(self) -> str:
        return f'WageEmployee: {self.fname} {self.lname} ({self.id}) WEEKLY EARNINGS: {self.weekly_earnings()}'

class SalaryEmployee(Employee):
    def __init__(self, fname:str, lname:str, id:int, yearly_salary:float):
        super().__init__(fname, lname, id)
        self.yearly_salary = yearly_salary
        
    
    def weekly_earnings(self):
        return '${:,.2f}'.format(self.yearly_salary / 52)
    
    def __str__(self) -> str:
        return f'SalaryEmployee: {self.fname} {self.lname} ({self.id}) WEEKLY EARNINGS: {self.weekly_earnings()}'


test1 = Employee('John', 'Smith', 2764723)
print(test1.__str__())

test2 = WageEmployee('Tim', 'Drake', 20474, 17.20, 40)
print(test2.__str__())

test3 = SalaryEmployee('Dan', 'Slaney', 6563, 67000)
print(test3.__str__())


