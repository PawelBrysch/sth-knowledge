from collections import namedtuple


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry)

'''
Minus ->                                                                                                       immutable
'''

perry = perry._asdict()
print(perry)

'''
Namedtuple lepsze od slownika, bo: (2)                                                                        1) szybsze
                                                                                           2) latwiejszy dostep do pola?
'''