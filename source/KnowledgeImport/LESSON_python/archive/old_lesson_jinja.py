'''####################################
Case to remove
####################################'''
# class Child:
#     def __init__(self, name_):
#         self.name = name_
#
# class Dictlike:
#     def __init__(self):
#         self.a = Child("ola")
#         self.b = Child("ela")
#
#     def items(self):
#         return self.__dict__.items()
#
#
# VAR = 3
# DICT_KTORY_BEDZIEMY_WIDZIEC = {
#     "KEY_KTOREMU_TRZEBA_DAC_VALUE_ROWNE_VAR"
# }
#
# data = {
#     'input': "\"JAKIS_INPUT_KTORY_MUSI_BYC_STRINGIEM_BY_SKOMPILOWALO\"",
#     'if_var1': 5,
#     'if_var2': 6,
#     # 'bad_path': "C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc",
#     'good_path': rf"C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc",
#     "list_": [4, 5, 6],
#     "dictlike": Dictlike()
# }
#
#
#
# template_string = """\
# byle_jaki_text = 0
# r\"\"\"
# Byle jaki text w komentarzu.
# \"\"\"
#
# wstaw_cos = {{input}} #<- tylko podwojna klamra dziala
#
# from PLAYGROUND.draft1 import DICT_KTORY_BEDZIEMY_WIDZIEC, VAR
# DICT_KTORY_BEDZIEMY_WIDZIEC["KEY_KTOREMU_TRZEBA_DAC_VALUE_ROWNE_VAR"] = VAR
#
#
# ### If
# # Ponizej bedzie przeklestwo, jesli context[if_var1] bedzie rowne 5, inaczej kucyk
# {%- if if_var1 == 5 %}
# _ = "Przeklenstwo"
# {% endif -%}
# {%- if if_var1 != 5 %}
# _ = "Kucyk"
# {% endif -%}
# # Ponizej bedzie przeklestwo, jesli context[if_var2] bedzie rowne 5, inaczej kucyk <- wersja z else
# {%- if if_var2 == 5 %}
# _ = "Przeklenstwo"
# {%- else %}
# _ = "Kucyk"
# {% endif -%}
#
#
# ### Sciezki
# try:
#     good_path = {{good_path}}
#     good_path_safe = {{good_path|safe}}
#     o_dziwo_trzeba_w_stringu = "{{good_path}}"
#     a_najlepiej_dodac_jeszcze_rf = rf"{{good_path}}"
# except:
#     pass
# # komentarz: sciezka bez rf nawet sie nie kompiluje (Python 3.7?)
#
#
# ### For
# {%- for elem in list_ %}
# "Kolejny element to {{elem}}."
# {% endfor -%}
#
#
# arg1 = "sth"
# arg2 = "sth"
# ### Makro
# {%- macro wypisz_trzy_razy(argument) -%}
# {%- for i in range(3) %}
# _ = "{{ argument }}"
# {% endfor -%}
# {%- endmacro %}
#
# # Pierwsze uzycie dla argument = arg1
# {{ wypisz_trzy_razy("arg1") }}
# # Drugie uzycie dla argument = arg1 <- argument przekazujemy w (" ") zamiast ( )
# {{ wypisz_trzy_razy('arg2') }}
#
# # dictlike.items()|map('last')|selectattr('name', 'equalto', 'ola')| list
# # -> {{ dictlike.items()|map('last')|selectattr('name', 'equalto', 'ola')| list }}
# # dictlike.items()|map('last')|selectattr('name', 'equalto', 'ela')| list
# # ->{{ dictlike.items()|map('last')|selectattr('name', 'equalto', 'ela')| list }}
# # dictlike.items()|map('last')|selectattr('name', 'equalto', 'maksio')| list
# # ->{{ dictlike.items()|map('last')|selectattr('name', 'equalto', 'maksio')| list }}
#
# # Wyjasnienie:
# # map(func, to_co_po_lewej_od_|) -> generator
# # def last(iterable) return iterable[-1]
# # selectattr('attrname', 'equalto', 'value', to_co_po_lewej) <=> filter(<zwraca true, jak atrybut elemtu jest rowny value>, to_co_po_lewej) -> generator
# # list(to_co_po_lewej) -> list
# # z listy potrzebna nam wartosc logiczna \
# """
#
#
#
# save_template_string_to_file(template_string)
# render_using_jinja(data, TEMPLATE_PATH, OUTPUT_PATH)
# open_with_notepadpp(OUTPUT_PATH)