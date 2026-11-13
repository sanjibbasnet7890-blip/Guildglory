import subprocess
import time

setup = """
mkdir -p ~/Guildglory
cp -r /storage/emulated/0/Guildglory/* ~/Guildglory/
cd ~/Guildglory
"""

subprocess.run(setup, shell=True, check=True)

process = subprocess.Popen(
    ["python", "run.py"],
    cwd=subprocess.run(
        "echo $HOME/test",
        shell=True,
        capture_output=True,
        text=True
    ).stdout.strip(),
    stdin=subprocess.PIPE,
    text=True
)

for command in ["3", "7", "0"]:
    time.sleep(2)
    process.stdin.write(command + "\n")
    process.stdin.flush()

process.wait()