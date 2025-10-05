import os

def makedir(PROJECT_NAME="Navya", TRIGGER="Navya"):
    print("==== USER CONFIG ====")

    # Paths
    DATASET_DIR  = f"/workspace/LoRA/{PROJECT_NAME}/"
    REG_DIR   = f"/workspace/LoRA/{PROJECT_NAME}/1_women/" # Dataset Later Added
    OUTPUT_DIR   = f"/workspace/LoRA/LoRA_Output/"
    LOG_DIR      = f"/workspace/LoRA/LoRA_Logs/{PROJECT_NAME}"

    # Create folders if not exist
    import os
    for p in [DATASET_DIR, OUTPUT_DIR, LOG_DIR, REG_DIR]:
        os.makedirs(p, exist_ok=True)

    REG_DIR   = f"/workspace/LoRA/{PROJECT_NAME}/" # Dataset Later Added

    print("✅ Folders ready:")
    print("📂 Dataset Dir :", DATASET_DIR)
    print("📂 Images Dir  :", REG_DIR)
    print("📂 Output Dir  :", OUTPUT_DIR)
    print("📂 Log Dir     :", LOG_DIR)
    print("\n⚡ Place your training images inside:")

    return DATASET_DIR, REG_DIR, LOG_DIR