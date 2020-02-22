from jinja2 import Environment as _Environment
from jinja2 import FileSystemLoader as _FileSystemLoader

import os as _os

class Child:
    def __init__(self, name_):
        self.name = name_

class Dictlike:
    def __init__(self):
        self.a = Child("ola")
        self.b = Child("ela")

    def items(self):
        return self.__dict__.items()


VAR = 3
DICT_KTORY_BEDZIEMY_WIDZIEC = {
    "KEY_KTOREMU_TRZEBA_DAC_VALUE_ROWNE_VAR"
}

template = rf"C:\Users\BryschP\Desktop\testus_top\TESTUS-Automation_Framework\PLAYGROUND\my_template.jinja2"
output_file = rf"C:\Users\BryschP\Desktop\testus_top\TESTUS-Automation_Framework\PLAYGROUND\output.py"
context = {
    'input': "\"JAKIS_INPUT_KTORY_MUSI_BYC_STRINGIEM_BY_SKOMPILOWALO\"",
    'if_var1': 5,
    'if_var2': 6,
    # 'bad_path': "C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc",
    'good_path': rf"C:\Users\BryschP\Desktop\testus_test_data\tmp_dbc.dbc",
    "list_": [4, 5, 6],
    "dictlike": Dictlike()
}
tmpl_path, tmpl_file = _os.path.split(template)
env = _Environment(loader=_FileSystemLoader(tmpl_path or './'))
rendered_content = env.get_template(tmpl_file).render(context)
with open(output_file, 'w', encoding='utf-8') as fibex:
    fibex.writelines(rendered_content)

