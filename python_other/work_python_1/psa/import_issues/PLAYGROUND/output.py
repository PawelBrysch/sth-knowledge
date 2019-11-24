byle_jaki_text = 0
r"""
Byle jaki text w komentarzu.
"""

wstaw_cos = "JAKIS_INPUT_KTORY_MUSI_BYC_STRINGIEM_BY_SKOMPILOWALO" #<- tylko podwojna klamra dziala

from PLAYGROUND.draft1 import DICT_KTORY_BEDZIEMY_WIDZIEC, VAR
DICT_KTORY_BEDZIEMY_WIDZIEC["KEY_KTOREMU_TRZEBA_DAC_VALUE_ROWNE_VAR"] = VAR


### If
# Ponizej bedzie przeklestwo, jesli context[if_var1] bedzie rowne 5, inaczej kucyk
_ = "Przeklenstwo"
# Ponizej bedzie przeklestwo, jesli context[if_var2] bedzie rowne 5, inaczej kucyk <- wersja z else
_ = "Kucyk"
### Sciezki
try:
    good_path = C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc
    good_path_safe = C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc
    o_dziwo_trzeba_w_stringu = "C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc"
    a_najlepiej_dodac_jeszcze_rf = rf"C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc"
except:
    pass
# komentarz: sciezka bez rf nawet sie nie kompiluje (Python 3.7?)


### For
"Kolejny element to 4."

"Kolejny element to 5."

"Kolejny element to 6."
arg1 = "sth"
arg2 = "sth"
### Makro

# Pierwsze uzycie dla argument = arg1

_ = "arg1"

_ = "arg1"

_ = "arg1"

# Drugie uzycie dla argument = arg1 <- argument przekazujemy w (" ") zamiast ( )

_ = "arg2"

_ = "arg2"

_ = "arg2"


# dictlike.items()|map('last')|selectattr('name', 'equalto', 'ola')| list
# -> [<PLAYGROUND.draft1.Child object at 0x00000202CAF616A0>]
# dictlike.items()|map('last')|selectattr('name', 'equalto', 'ela')| list
# ->[<PLAYGROUND.draft1.Child object at 0x00000202CAF615C0>]
# dictlike.items()|map('last')|selectattr('name', 'equalto', 'maksio')| list
# ->[]

# Wyjasnienie:
# map(func, to_co_po_lewej_od_|) -> generator
# def last(iterable) return iterable[-1]
# selectattr('attrname', 'equalto', 'value', to_co_po_lewej) <=> filter(<zwraca true, jak atrybut elemtu jest rowny value>, to_co_po_lewej) -> generator
# list(to_co_po_lewej) -> list
# z listy potrzebna nam wartosc logiczna 