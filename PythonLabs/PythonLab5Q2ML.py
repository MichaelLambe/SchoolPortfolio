class Person:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def fullName(self):
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
            print(f"{'Name:':10} {Person.fullName(object)}")
            print(f"{'Email:':10} {object.email}")
            print(f"{'Number:':10} {object.custNum}")
            print()
        else:
            print("EMPLOYEE")
            print(f"{'Name:':10} {Person.fullName(object)}")
            print(f"{'Email:':10} {object.email}")
            print(f"{'SSN:':10} {object.ssn}")
            print()
        again = input("Continue? (y/n): ")
        print()
        if again != "y":
            print("Bye!")
            break

           


            
if __name__ == "__main__":
    main()

            
