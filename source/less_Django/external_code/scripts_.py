from django.core.wsgi import get_wsgi_application
from django.test.utils import setup_test_environment
from django.test import Client
import os
import sys

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        'mylogger': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}

def run_command_line(components):
    os.system(" ".join(components))


def emulate_manage_py_shell(path_to_project):
    sys.path.append(path_to_project)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    application = get_wsgi_application()


def get_pseudo_client(path_to_project):
    emulate_manage_py_shell(path_to_project)
    setup_test_environment()
    client = Client()
    return client

if __name__ == '__main__':
    python_path = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\venv\Scripts\python.exe"
    manage_py = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\less_Django\my_own_name\manage.py"



