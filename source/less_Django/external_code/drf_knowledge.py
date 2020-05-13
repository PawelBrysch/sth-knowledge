import subprocess
# from subprocess import check_output
import os

# TODO zbudowac narzedzia do wysylania requestow
http = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\venv\Scripts\http.exe"

# command = f"{http} http://127.0.0.1:8000/snippets.json"
command = f"http://127.0.0.1:8000/snippets.json"

# sub_output = subprocess.Popen([http, command], stdout=subprocess.PIPE)
# sub_output = subprocess.run([http, command], stdout=subprocess.PIPE)
#
# text = sub_output.communicate()[0]

# out = subprocess.check_output([http, command])

res = os.popen(f'{http} {command}').read()