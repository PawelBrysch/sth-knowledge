import os

TEMPLATE_PATH = rf"E:\KnowledgeImport\LESSON_python\temp\my_template2.jinja2"
OUTPUT_PATH = rf"E:\KnowledgeImport\LESSON_python\temp\rendered_text.py"

def open_with_notepadpp(path_to_file):
    path_to_notepad = r"C:\Users\BryschP\Desktop\ProgramFiles2\Notepad++\notepad++.exe"
    osCommandString = " ".join([path_to_notepad, path_to_file])
    os.system(osCommandString)


def save_template_string_to_file(template_string):
    cwd = os.getcwd()
    path_to_template = os.path.join(cwd, "temp\my_template2.jinja2")
    with open(path_to_template, "w") as file:
        file.write(template_string)