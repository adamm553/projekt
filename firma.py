import csv
import random
    
class Employee():
    
    def __init__ (self, first_name, last_name, position):
        newid = random.randint(99999, 999999)
        self._id = (str(newid))
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
        
    def __str__(self):
        return f"{self._id},{self._first_name},{self._last_name},{self._position}"

class Manager(Employee):
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)
    
    def __str__(self):
        return f"{self._id},{self._first_name},{self._last_name},{self._position}"

def enter_employee():
    first_name = str(input("Enter first name: "))
    last_name = str(input("Enter last name: "))
    position = str(input("Enter position: "))
    m = Manager(first_name, last_name, position)
    return f"[{m}]"

def write_employees(employees):
    with open('plik.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        for employee in employees:
            writer.writerow([str(employee).replace('[', '').replace(']','')])

def check_employee(employees):
    id = input("Enter ID: ")
    for x in employees:
        for y in x.split(','):
            if id in y:
                print(x)
                print()
            else:
                print("There is no employee with this ID!")

def show_employees(employees):
    for employee in employees:
        print(f"{employee}")
    print()

def read_file(emp):
    with open('plik.csv', 'rt') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            emp.append(str(line).replace("'", ""))


def edit_employee(emp):
    id = str(input("Enter ID of Employee: "))
    element = str(input("Enter an element that you want to change(type: firstname, lastname, position): "))
    if element == 'firstname':
        i = 1
    elif element == 'lastname':
        i = 2
    elif element == 'position':
        i = 3
    else:
        print("Wrong input!!!")
    value = input("Write a change: ")
    r = csv.reader(open('plik.csv', 'r')) # Here your csv file
    lines = list(r)
    for x in lines:
        for y in x:
            if id in y:
                idx = x.index(y)
                result = y.split(',')
    result[i] = value
    result = [','.join(result)]
    lines[idx] = result

    writer = csv.writer(open('plik.csv', 'w', newline=""))
    writer.writerows(lines)
        

def clean_file():
    with open('plik.csv', 'w') as file:
        file.truncate()

def delete_employee(employees):
    id = str(input("Enter employee's id to be deleted: "))
    for employee in employees:
        if id in employee:
            employees.remove(employee)
        else:
            print("Employee does not exist")

    
def menu():
    print("Please remember to save the file!!")
    print("1) New Employee")
    print("2) Check Employee")
    print("3) Show all Employees")
    print("4) Edit employee")
    print("5) Delete Employee")
    print("6) Read CSV file")
    print("7) Save to CSV file")
    print("8) Clean file")
    print("9) Exit.")

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
            edit_employee(employees)
        elif option == '5':
            delete_employee(employees)
        elif option == '6':
            read_file(employees)
        elif option == '7':
            write_employees(employees)
        elif option == '8':
            clean_file()
        elif option == '9':
            run = False
        else:
            print('xd')

main()
