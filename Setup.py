import os
from Tools.unzip import unzip_file
from Download.Realviz import Install_Realviz
from time import sleep
from Tools.makedir import makedir
from Download.resume import resume_setup

print("================================")
print("Starting Setup...")
print("================================")

os.chdir("/workspace/")

makedir()

os.system("git clone https://github.com/bmaltais/kohya_ss")

os.chdir("/workspace/kohya_ss/sd-scripts")

os.system("git submodule init")

os.system("git submodule update")

os.chdir("/workspace/")

os.system('gdown "https://drive.google.com/uc?id=1ybTkd0d_XOazmk9B1VFxCRJHZXzLUDpp"')

sleep(2)

unzip_file()

resume_setup()

Install_Realviz()



print("===============================")
print("Setup Completed Successfully!")
print("===============================")