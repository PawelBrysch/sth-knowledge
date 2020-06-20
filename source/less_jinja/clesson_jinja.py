#TODOG jak przeniesc ustawienia pycharma
#TODOG encoding utf-8

'''####################################
HOW TO USE JINJA?
####################################'''
import os
from less_jinja.utils import open_with_notepadpp, save_template_string_to_file, TEMPLATE_PATH, OUTPUT_PATH
from jinja2 import Environment, FileSystemLoader


def render_using_jinja(data, template_path, output_path):
    template_dirname, template_filename = os.path.split(template_path)
    env = Environment(loader=FileSystemLoader(template_dirname or './'))
    rendered_content = env.get_template(template_filename).render(data)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(rendered_content)


'''####################################
HOW TO WRITE RENDERED STRING TO A FILE?
####################################'''
# with open(path_to_file, 'w', encoding='utf-8') as file:
#     file.writelines(rendered_content)



'''####################################
SIMPLE INPUTS
####################################'''
# import os
#
# some_int = 234
# some_string = "Ala has a cat."
# some_path = os.getcwd()
#
# data = {
#     'name_key': "some_var",
#     'int_key': some_int,
#     'str_key': some_string,
#     'path_key': some_path
# }
#
# template_string = """\
# {{name_key}} = 2 * 5
# int_best_way = {{int_key}}
# some_str = "{{str_key}}"
# some_path = rf"{{path_key}}"\
# """
#
# save_template_string_to_file(template_string)
# render_using_jinja(data, TEMPLATE_PATH, OUTPUT_PATH)
# open_with_notepadpp(OUTPUT_PATH)
#

'''####################################
COMMENTS
# ####################################'''
# data = {
# }
#
# template_string = """\
# # inline comment\
# {# jinja comment - NOT VISIBLE!!!#}
# \"\"\"
# multiline comment
# \"\"\"\
# """
#
# save_template_string_to_file(template_string)
# render_using_jinja(data, TEMPLATE_PATH, OUTPUT_PATH)
# open_with_notepadpp(OUTPUT_PATH)
#

'''####################################
STATEMENTS (IF, FOR, MAKRO)
####################################'''
'''
why there are `-` signs within jinja instructions?->    they delete additional whitespaces (try: trial and error method)
'''
# data = {
#     'condition_1': 1,
#     'condition_2': 1,
#     'some_list': [4, 5, 6],
#     'list_of_classnames': ["Alpha", "Beta"]
# }
#
# template_string = """\
# # IF
# {% if condition_1 == 1 -%}
# print("visible")
# {% else %}
# print("not visible")
# {% endif %}
#
# # FOR
# {%- for elem in some_list %}
# "The next element is {{elem}}."
# {%- endfor %}
#
#
# # MAKRO
# from external_module import BaseClass
# {%- macro render_class(argument) -%}
# class {{argument}}(BaseClass):
#     pass
# {%- endmacro %}
#
# {{ render_class(list_of_classnames[0]) }}
#
#
# {{ render_class(list_of_classnames[1]) }}\
# """
#
# save_template_string_to_file(template_string)
# render_using_jinja(data, TEMPLATE_PATH, OUTPUT_PATH)
# open_with_notepadpp(OUTPUT_PATH)


'''####################################
DATA UNPACKING (JSON) && FILTER
####################################'''
'''
`func(arg)` - here he have another syntax - what?->                                                           `arg|func`

`some_dict.values() -> Typing.list` <==>                             `some_dict.items()|map("last") -> Typing.generator`
    so `last` must be equal to->                                                        `lambda iterable : iterable[-1]`
selectattr('attrname', 'equalto', 'value') is just a ...->                                                        filter
'''
# class CustomClass:
#     def __init__(self, name_):
#         self.name = name_
#
#     def __repr__(self):
#         return "Object with ID={}".format(self.name)
#
# some_dict = {
#     'first_key': CustomClass("2B"),
#     'second_key': CustomClass("9Z")
# }
#
# data = {
#     "some_dict": some_dict
# }
#
#
# template_string = """\
#
# # some_dict.items()
# # >>> {{ some_dict.items()}}
#
# # some_dict.items()|map('last')
# # >>> {{ some_dict.items()|map('last')}}
# # some_dict.items()|map('last')|list
# # >>> {{ some_dict.items()|map('last')|list}}
#
# # some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')
# # >>> {{ some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')}}
# # some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')|list
# # >>> {{ some_dict.items()|map('last')|selectattr('name', 'equalto', '2B')|list }}
#
# # some_dict.items()|map('last')|selectattr('name', 'equalto', 'MC2')|list
# # >>>{{ some_dict.items()|map('last')|selectattr('name', 'equalto', 'MC2')|list }}\
# """
#
#
# save_template_string_to_file(template_string)
# render_using_jinja(data, TEMPLATE_PATH, OUTPUT_PATH)
# open_with_notepadpp(OUTPUT_PATH)