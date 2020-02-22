'''
    This is module
'''
#
# PyLint Tutorial
#

#pylint: disable=too-few-public-methods
class Car:
    '''
        This is class
    '''
    my_pizza = 5

    def __init__(self, color):
        self.color = color

        self.my_soup = 2

    def __str__(self):
        return self.color+" "+str(self.my_soup)

    def useless_method(self):
        '''
            This is useless method
        '''
        self.color = "black as hole"
        print("i won")


MY_CAR = Car("blue")


def crash(car1):
    '''
        This is method
    '''

    car1.color = "burnt"


crash(Car("red"))
