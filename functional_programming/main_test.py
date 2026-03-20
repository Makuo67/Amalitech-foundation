# Understanding OOP

class Employee:
    num_of_emps = 0
    raise_amt = 1.6

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    raise_amt = 1.03

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employess = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emps(self):
        for emp in self.employees:
            print('----->', emp.fullname())


emp1 = Developer('Makuo', 'Okeke', 10000, 'Javascript')
emp2 = Employee('Marius', 'Ojemba', 45000)
emp3 = Developer('Hubert', 'Apana', 4000, 'Scala')
emp4 = Employee('Pierrine', 'Nshuti', 5000)


# print(emp1.prog_lang)

mgr1 = Manager('Sue', 'Synman', 40000, [emp1, emp3])
mgr2 = Manager('Roger', 'Uwimana', 40000, [emp2, emp4])
print("Manager 1", mgr1.email)
print("Manager 2", mgr2.email)

print(mgr1.show_emps())
print(mgr2.show_emps())

emp4_str = 'John-Doe-2000'
emp5_str = 'Amara-Okeke-3000'

first, last, pay = emp4_str.split('-')
emp4 = Employee(first, last, pay)

emp5 = Employee.from_string(emp5_str)

print(emp4.email)
print(emp5.email)
