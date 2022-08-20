import itertools

class Employee():
    newid = itertools.count()
    def __init__ (self, first_name, last_name, position):
        self._id = str(next(Employee.newid))
        self._first_name = self._valid_first_name(first_name)
        self._last_name = self._valid_last_name(last_name)
        self._position = self._valid_postion(position)
     
    def _valid_first_name(self, first_name):
        if isinstance(first_name, str):
            if len(first_name) > 0:
                return first_name
            else:
                raise ValueError("Lenght of first name must be greater than 0")
        else:
            raise TypeError("First name must be an str type")

    def _valid_last_name(self, last_name):
        if isinstance(last_name, str):
            if len(last_name) > 0:
                return last_name
            else:
                raise ValueError("Lenght of last name must be greater than 0")
        else:
            raise TypeError("Last name must be an str type")

    def _valid_postion(self, position):
        if isinstance(position, str):
            if len(position) > 0:
                return position
            else:
                raise ValueError("Lenght of postion must be greater than 0")
        else:
            raise TypeError("Position must be an str type")
    
    def _set_first_name(self, value):
        if isinstance(value, str):
            if len(value) > 0:
                self._first_name = value
            else:
                raise ValueError("Lenght of first name must be greater than 0")
        else:
            raise TypeError("First name must be an str type")

    def _set_last_name(self, value):
        if isinstance(value, str):
            if len(value) > 0:
                self._last_name = value
            else:
                raise ValueError("Lenght of last name must be greater than 0")
        else:
            raise TypeError("Last name must be an str type")

    def _set_position(self, value):
        if isinstance(value, str):
            if len(value) > 0:
                self._position = value
            else:
                raise ValueError("Lenght of postion must be greater than 0")
        else:
            raise TypeError("Position must be an str type")
    
    def get_id(self):
        return self._id
    
    def details(self):
        return f"{self._id} | {self._first_name} | {self._last_name} | {self._position}"
    
    def __str__(self):
        return f'\nId: {self._id} \nFirst name: {self._first_name} \nLast name: {self._last_name} \nPosition: {self._position}'

class Manager(Employee):
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)
    
    def __str__(self):
        return super(Manager, self).__str__()

def enter_employee():
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    position = str(input("Enter position: "))
    return Manager(first_name, last_name, position)

def write_employees(employees):
    with open(r'C:\Users\TheKi\Desktop\projekt\plik.txt', 'w') as file:
        for employee in employees:
            file.write(f"{str(employee)}\n")

def check_employee(employees):
    found = False
    id = input("Enter Employee's ID: ")
    for employee in employees:
        if id in employee.get_id():
            print(employee)
            print()
            found = True
    if not found:
        print("There is no employee with this id")

def show_employees(employees):
    for employee in employees:
        print(employee)
    print()

def clean_file():
    with open(r'C:\Users\TheKi\Desktop\projekt\plik.txt', 'w'):
        pass

def delete_employee(employee):
    id = input("Enter id: ")
    for i in employee:
        if id in i._id:
            employee.remove(i)
            break     
    
def menu():
    print("1) New Employee")
    print("2) Check Employee")
    print("3) Show all Employees")
    print("4) Delete Employee")
    print("5) Save to txt file")
    print("6) Clean file")
    print("7) Exit.")

def main():
    option = 0
    employees = []
    run = True
    while run == True:
        menu()
        option = input('-> ')
        if option == '1':
            employees.append(enter_employee())
        elif option == '2':
            check_employee(employees)
        elif option == '3':
            show_employees(employees)
        elif option == '4':
            delete_employee(employees)
        elif option == '5':
            write_employees(employees)
        elif option == '6':
            clean_file()
        elif option == '7':
            run = False
        else:
            print('xd')

main()

