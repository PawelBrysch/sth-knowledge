from les_Jenkins.workspace_mock.target.some_module import suma

def test_good():
    assert suma(2, 2) == 4
    assert suma(3, 3) == 6

def test_bad():
    assert suma(2, 3) == 23

# python -m pytest C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\les_Jenkins\workspace_mock\tests\src\tc_01.py

C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\venv\Scripts\python.exe
"C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.5\helpers\pycharm\_jb_pytest_runner.py"
--path
C:/Users/Lenovo/Desktop/PROJECTS/django_top2/sth-knowledge/source/LESSON_pytest/tests/02_special_assertions_test.py