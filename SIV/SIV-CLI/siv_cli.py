import subprocess

info = subprocess.run(["systeminfo"], capture_output=True, check=True, text=True)
output_lines = [line.strip() for line in info.stdout.splitlines()[1:3]]
output = '\n'.join(output_lines)
print(output)
