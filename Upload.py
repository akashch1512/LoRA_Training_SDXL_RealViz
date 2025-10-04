import os
from huggingface_hub import HfApi, upload_folder

# === SETUP ===
# Set your token safely (replace with your token if you want, but ENV var is safer)
HF_TOKEN = "put_your_token_here"  # <-- replace with your Hugging Face token or set the HF_TOKEN env variable
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"   # Enable fast upload

# Repo details
REPO_ID = "akashch1512/Navya_LoRA_SDXL_RealViz"   # <-- change "username" to your Hugging Face username
LOCAL_DIR = "/workspace/LoRA/LoRA_Output/Navya/"

# === CREATE REPO IF NOT EXISTS ===
api = HfApi(token=HF_TOKEN)
try:
    api.create_repo(repo_id=REPO_ID, repo_type="model", exist_ok=True)
    print(f"✅ Repo ready at https://huggingface.co/{REPO_ID}")
except Exception as e:
    print(f"Repo creation failed: {e}")

# === UPLOAD FOLDER ===
upload_folder(
    repo_id=REPO_ID,
    folder_path=LOCAL_DIR,
    repo_type="model",
    token=HF_TOKEN,
    commit_message="Upload Navya LoRA trained model",
    ignore_patterns=["*.log", "*.tmp", "__pycache__/*"]
)

print("🚀 Upload complete!")
