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

# PowerShell run docker compose file
run_pro = subprocess.Popen([r'powershell.exe', '-ExecutionPolicy', 'Unrestricted', 'docker-compose', '-f', 'docker-compose.yml', 'up'], cwd=os.getcwd())
# sleep 20 second, need to correct run docker images
time.sleep(20)
# In need to log info uncommented string
# result = run_pro.wait()