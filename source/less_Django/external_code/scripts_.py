from django.core.wsgi import get_wsgi_application
from django.test.utils import setup_test_environment
from django.test import Client
import os
import sys
import json
import requests

METHOD_HTTP_NAME_to_PYTHON_NAME = {
    "GET": "get"
}

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


def get_printable_json(method, url_suffix):
    method_python_name = METHOD_HTTP_NAME_to_PYTHON_NAME[method]
    req = getattr(requests, method_python_name)(f'http://127.0.0.1:8000{url_suffix}')
    content = json.loads(req.content)
    pretty_string = json.dumps(content, indent=4, sort_keys=True)
    return pretty_string

if __name__ == '__main__':
    python_path = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\venv\Scripts\python.exe"
    manage_py = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\less_Django\my_own_name\manage.py"



