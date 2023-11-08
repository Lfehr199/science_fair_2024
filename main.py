import subprocess

command ="code run.py"

result =subprocess.run(command,shell=True, text=True, capture_output=True)
print(result.stdout)
