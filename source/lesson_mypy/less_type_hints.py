

'''#############'''
''' Type hinting'''
'''#############'''

'''
Ponizsze dwie metody maja sens raczej tylko z uzyciem typing, gdyz gdy deklarujemy typy wbudowane (str, int, itd..) program
z reguly sam wie jaki typ w nich jest w danej chwili. Niejako pierwotna deklaracja to zgłasza. W sensie a = 2 => a: int, itd..
Moze w bardziej rozbudowanych przykladach bedzie mialo sens typowanie zmiennych o typie wbudowanym.
'''

''' 1) Special comments '''
# from typing import List
# a = []  # type: List[str]
# b=2
# a.append(b)
''' 2) Variable annotation '''
# from typing import List
# primes: List[int] = []
# string1 = "elo"
# primes.append(string1)



''' 3) Funtion annotations '''
''' w/o typing'''
# def annotated(x: int, y: str) -> bool:
#     return x < y
# print(annotated.__annotations__)
''' w/ typing'''
# from typing import List
# def func(x: List[int], y):
#     while y>0:
#         print(x[y])
#         y -= 1
# yy = 3
# xx = ["100", "200","300","400","500"]
# func(xx, yy)


''' Stub files'''
#
#
#
#


'''#############'''
''' Typing'''
'''#############'''



''' conteneir'''
# from typing import List, Dict, Tuple, Set
#
# MyList = List[int]
# MyDict = Dict[str, str]
# MyTuple = Tuple[str, int, float]
# MySet = Set[float]


''' iterable'''
# from typing import Iterable
#
# MyIterable = Iterable[int]

''' methods'''
''' simple'''
# from typing import Callable
# def simplefunc(arg1: float) -> str:
#     return "siema"
#
#
# def execute_simple_func(func: Callable[[int], str]):
#     print("nothing")
#
#
# execute_simple_func(simplefunc)

''' complex - ultra static'''
# from typing import Callable
# def complexfunc(arg1: int, arg2: float, arg3: float) -> str:
#     return "siema"
#
#
# def execute_complex_func(func: Callable[[int, float, str], str]):
#     print("nothing")
#
#
# execute_complex_func(complexfunc)

''' complex - ellipsis (arguments don't count)'''
# from typing import Callable
#
#
# def complexfunc(arg1: int, arg2: float, arg3: float) -> str:
#     return "siema"
#
# #IMPORTANT
# def execute_complex_func(func: Callable[..., str]):
#     print("nothing")
#
#
# execute_complex_func(complexfunc)


''' aka typedef '''
# from typing import NewType
#  #IMPORTANT
# UserId = NewType("(message): UserId", int)
# good_obj = UserId(524313)
# bad_obj = 624316
#
# def get_user_name(user_id: UserId):
#     print("elo")
#
#
# get_user_name(good_obj)
# get_user_name(bad_obj)

''' how to derive (typedef)'''
# from typing import NewType
# UserId = NewType('UserId', int)
# class AdminUserId(UserId):
#     pass
# #-> error

# from typing import NewType
# UserId = NewType('UserId', int)
# AdminUserId = NewType('AdminUserId', UserId)
# # #-> works
