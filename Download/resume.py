import os
from Tools.unzip import unzip_file

def resume_setup():
    os.chdir("/workspace/")

    os.system('gdown "https://drive.google.com/uc?id=1yBrlyIYzGHVla3Oiw1-wIZMIw7-i72I_"')

    os.system("tar -xvf /workspace/Navya.tar -C /workspace/LoRA/LoRA_Output/")

    print("✅ Resume setup completed!")