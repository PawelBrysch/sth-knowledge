'''######################
side_effect vs return_value
######################'''
'''
Jak to dziala?->                                                side_effect przeslania niezaleznie od kolejnosci dodania
czy mozna wstawic jako argument dla patch?->                                                                         TAK
'''


'''######################
Mock(spec=Class_or_func)
######################'''
'''
co nam to daje?->                      wywali AttributeError, jak wywolamy atrybut, ktorego nie ma dana klasa (regresja)
a sprawdza argumenty?->                                                                                              NIE
'''

from unittest.mock import Mock

mocek = Mock(details=lambda: "elo")
mocek.details()
mocek.details


