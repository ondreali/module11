"""
program: SalariedEmployee
Author: Ondrea Li
Last date modfied: 07/5/20

The purpose of this program is to derive SalariedEmployee from employee
"""
import datetime

from Inheritance_Assignment.employee import Employee
today = datetime.datetime.now()

class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, date, salary):
        '''
        :param lname: represents last name derived from Employee Class
        :param fname: represents first name derived from Employee Class
        :param addy: represents address name derived from Employee Class
        :param phone: represents phone number derived from Employee Class
        :param date: represents start date
        :param salary: represents salary
        '''
        super().__init__(lname, fname, addy, phone)
        self.start_date = date
        self.salary = salary

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, datetime.datetime):
            self._start_date = value
        else:
            raise AttributeError


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, float):
            self._salary = value
        else:
            raise AttributeError


    def give_raise(self, raise_pay):
        self._salary = self._salary+ raise_pay

    def display(self):
        return super().display() + f'\nStart date: {self.start_date} \nSalary: ${self.salary:2f}'

    def __str__(self):
        return super.display() + str(self.start_date.strftime('%m-%%d-%Y')) + str(self.salary)

    def __repr__(self):
        return super().display() + f'\nStart date: {self.start_date} \nSalary: ${self.salary:.2f}'

    @salary.setter
    def salary(self, value):
        self._salary = value


if __name__ == '__main__':
    salemp = SalariedEmployee('Hello', 'kitty', '123 Conch Street', '515-345-2345', today, 40000.00)
    salemp.give_raise(5000.00)
    print(salemp.display())
    del salemp
