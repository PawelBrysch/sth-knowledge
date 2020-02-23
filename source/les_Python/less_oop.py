'''#############################'''
''' why not my_obj._MyClass__atr'''
'''#############################'''
''' 
to samo ma miejsce w przypadku dokonywania tych assignemtow w ciele klasy (w sensie z uzyciem self.
wniosek->                                                                               self.__class__._MyClass__atr
'''
# class RLCN:
#     static_var = 5
#
#
# rlcn = RLCN()
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)
#
# RLCN.static_var =12
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)
#
# rlcn.static_var =40
# print(id(RLCN.static_var), id(rlcn.static_var))
# print(RLCN.static_var, rlcn.static_var)


