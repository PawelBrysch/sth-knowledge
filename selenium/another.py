import subprocess

def startProgram():
    SW_MINIMIZE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_MINIMIZE
    # subprocess.Popen(r'C:\test.exe', startupinfo=info)
    subprocess.Popen(r"C:\Program Files\SANWA\PCLink7 Trial\PCLink7.exe", startupinfo=info)


startProgram()