import subprocess
import os
import time
# PowerShell
# run_pro = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
#                              '-ExecutionPolicy',
#                              'Unrestricted',
#                              './learn.ps1'], cwd=os.getcwd())
#
# result = run_pro.wait()


run_pro = subprocess.Popen([r'powershell.exe', '-ExecutionPolicy', 'Unrestricted', 'docker-compose', '-f', 'docker-compose.yml', 'up'], cwd=os.getcwd())
time.sleep(30)
# result = run_pro.wait()