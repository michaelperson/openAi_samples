import subprocess
result = subprocess.run(    ['git', 'diff', '--staged'],    capture_output=True,    text=True)
diff_output = result.stdout
print(diff_output)




