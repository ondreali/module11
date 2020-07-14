"""
program: hourly_employee
Author: Ondrea Li
Last date modfied: 07/5/20

The purpose of this program is to drive hourly_employee from Employee
"""
import datetime

from Inheritance_Assignment.employee import Employee

today = datetime.datetime.now()


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, date, hour):
        '''
        :param lname: represents last name derived from Employee Class
        :param fname: represents first name derived from Employee Class
        :param addy: represents address name derived from Employee Class
        :param phone: represents phone number derived from Employee Class
        :param date: represents start date
        :param hour: represents hourly pay
        '''
        super().__init__(lname, fname, addy, phone)
        self.start_date = date
        self.hourly_pay = hour

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
    def hourly_pay(self):
        return self._hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, value):
        if isinstance(value, float):
            self._hourly_pay = value
        else:
            raise AttributeError

    def give_raise(self, raise_pay):
        self._hourly_pay = self._hourly_pay + raise_pay

    def display(self):
        return super().display() + f'\nStart date: {self.start_date} \nHourly Pay: ${self.hourly_pay:2f}'

    def __str__(self):
        return super.display() + str(self.start_date.strftime('%m-%%d-%Y')) + str(self.hourly_pay)

    def __repr__(self):
        return super().display() + f'\nStart date: {self.start_date} \nHourly Pay: ${self.hourly_pay:.2f}'

if __name__ == '__main__':
    houremp = HourlyEmployee('Hello', 'kitty', '123 Conch Street', '515-345-2345', today, 10.00)
    houremp.give_raise(2.00)
    print(houremp.display())
    del houremp
