#!c:\users\lenovo\desktop\projects\programming\top_proper\sth-knowledge\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pylatexenc==2.5','console_scripts','latexwalker'
__requires__ = 'pylatexenc==2.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pylatexenc==2.5', 'console_scripts', 'latexwalker')()
    )
