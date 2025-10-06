from huggingface_hub import snapshot_download
import os
from Tools.unzip import unzip_file

def resume_setup():
    # Ensure output directory exists
    output_dir = "/workspace/LoRA/LoRA_Output/Navya"
    os.makedirs(output_dir, exist_ok=True)

    # Enable high-speed transfer
    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

    # Repo ID
    repo_id = "akashch1512/Navya_LoRA_SDXL_RealViz"

    print(f"🚀 Downloading {repo_id} directly into {output_dir}...")

    snapshot_download(
        repo_id=repo_id,
        repo_type="model",
        local_dir=output_dir,
        local_dir_use_symlinks=False,  # ensures actual file copies
        resume_download=True,          # resume if interrupted
    )

    print("✅ Resume Download complete!")
