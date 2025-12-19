import os

def git_update():
    print("[INFO] Mengecek update dari GitHub...")
    os.system("git pull")