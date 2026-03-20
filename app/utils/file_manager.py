import os
import shutil


def safe_write(file_path, content):
    if not file_path.startswith("repo/"):
        raise Exception("Invalid path")

    if os.path.exists(file_path):
        shutil.copy(file_path, file_path + ".bak")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)