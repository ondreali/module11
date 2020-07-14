"""
program: Inheritance
Author: Ondrea Li
Last date modfied: 07/5/20

The purpose of this program is to write information about employee
"""

class Employee:
    def __init__(self, lname, fname, addy, phone):
        '''
        :param lname: represents last name
        :param fname: represents last name
        :param addy: represents address from the class address
        :param phone: represents phone numer
        '''
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone


    @property
    def last_name(self):
        '''
        :return: last name of customer
        '''
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        :param value: represents the last name
        :keyError: raises AttributeError
        """
        if isinstance(value, str):
            self._last_name = value
        else:
            raise AttributeError

    @property
    def first_name(self):
        '''
        :return: returns first name
        '''
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        '''
        :param value: this sets the first name
        :keyError: raises Attribute error if not str
        '''
        if isinstance(value, str):
            self._first_name = value
        else:
            raise AttributeError

    @property
    def address(self):
        '''
        :return: retursn the address of the customer
        '''
        return self._address

    @address.setter
    def address(self, value):
        '''
        :param value: sets the address
        :keyError: raise AttributeError if not a str
        '''
        if isinstance(value, str):
            self._address = value
        else:
            raise AttributeError

    @property
    def phone_number(self):
        '''
        :return: returns the phone number
        '''
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        '''
        :param value: this sets the phone number
        :keyError: raises AttributeError if not str
        '''
        if isinstance(value, str):
            self._phone_number = value
        else:
            raise AttributeError

    def display(self):
        return f'{self.last_name}, {self.first_name}, \n{self.address}, \n{self.phone_number}'

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name) +'\n' + str(self.address) + '\n'+ str(self.phone_number)

    def __repr__(self):
        return f'{self.last_name}, {self.first_name}, \n{self.address}, \n{self.phone_number}'

#driver
if __name__ == '__main__':
    emp = Employee('Hello', 'kitty', '123 Conch Street', '515-345-2345')
    print(emp.display())
    del emp
