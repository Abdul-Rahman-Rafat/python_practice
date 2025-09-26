import os
import shutil

def os_file_manager():
    while True:
        dir_path = input("Enter a directory path: ").strip()

        if not os.path.isdir(dir_path):
            print("Invalid directory! Please try again.")
            continue  

        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        txt_files = [f for f in os.listdir(dir_path) if f.endswith(".txt")]

        copied_count = 0
        for file in txt_files:
            src = os.path.join(dir_path, file)
            dst = os.path.join(backup_path, file)
            shutil.copy2(src, dst)
            copied_count += 1

        print(f"Copied {copied_count} .txt file(s) into {backup_path}")
        break 

