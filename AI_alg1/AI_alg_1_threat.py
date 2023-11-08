import subprocess
from Variables import ai_git_downloaded
from Variables import dev_mode
#running commands in the terminal for streamlining start up
if ai_git_downloaded == False and dev_mode == True :
    commands = 
    [
        "cd AI_alg_1",
        "sudo apt-get update",
        "sudo apt-install git",
        "sudo git clone https://github.com/dusty-nv/jetson-inference.git"
        "cd  jetson-inference",
        "docker/run.sh",
        "cd python/",
        "cd training/",
        "cd detection/",
        "cd ssd/",
        "cd data",
        "sudo git clone https://github.com/Lfehr199/threat-dectection",
        "cd ..",
        "python train_ssd.py --data=data/threat --model-dir=model/threat --batch-size=2 --epoch=1 --label=data/threat/labels.txt"
    ]

    command = ";".join(commands)
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
print(result.stdout)
