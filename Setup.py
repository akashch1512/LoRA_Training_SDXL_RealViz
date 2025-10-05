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

unzip_file()

os.system('gdown "https://drive.google.com/uc?id=1xbqKVXBAatUNVfSJDqB3WIc_WdDw6Grf"')

unzip_file(location="/workspace/1_women.zip", dest="/workspace/LoRA/Navya/1_women")

sleep(2)

os.system("mv /workspace/LoRA/Navya/1_women/content/1_women/* /workspace/LoRA/Navya/1_women")

os.system("rm -r /workspace/LoRA/Navya/1_women/content")

sleep(2)

resume_setup()

Install_Realviz()



print("===============================")
print("Setup Completed Successfully!")
print("===============================")