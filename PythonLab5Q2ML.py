class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Customer(Person):
    def __init__(self, fname, lname, email, custNum):
        super().__init__(fname, lname, email)
        self.custNum = custNum


class Employee(Person):
    def __init__(self, fname, lname, email, ssn):
        super().__init__(fname, lname, email)
        self.ssn = ssn

def checkC(cus):
    return isinstance(cus, Customer)

#def checkE(emp):
    return isinstance(emp, Employee)



def main():
    print("Customer/Employee Data Entry")
    print()
    while True:
        object = None
        choice = input("Customer or Employee? (c/e): ")
        print()
        print("DATA ENTRY")
        if choice == "c":
            firstName = input("First name: ")
            lastName = input("Last name: ")
            eMail = input("Email: ")
            cNum = input("Number: ")
            print()
            object = Customer(firstName, lastName, eMail, cNum)
        elif choice == "e":
            firstName = input("First name: ")
            lastName = input("Last name: ")
            eMail = input("Email: ")
            ssn = input("SSN: ")
            print()
            object = Employee(firstName,lastName, eMail, ssn)
        else:
            print("Error Please Try Again")
        
        if checkC(object) == True:
            print("CUSTOMER")
            print(f"Name: {Person.__str__}")
            print(f"Email: {object.email}")
            print(f"Number: {object.custNum}")
            print()
        else:
            print("EMPLOYEE")
            print(f"Name: {object.__str__}")
            print(f"Email: {object.email}")
            print(f"SSN: {object.ssn}")
            print()

           


            
if __name__ == "__main__":
    main()

            
