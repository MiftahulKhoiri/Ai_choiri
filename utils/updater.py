import subprocess
import sys
import os
import hashlib

HASH_FILE = ".requirements.hash"

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def install_requirements_if_needed():
    if not os.path.exists("requirements.txt"):
        print("[INFO] requirements.txt tidak ada, skip.")
        return

    current_hash = file_hash("requirements.txt")

    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            old_hash = f.read().strip()

        if current_hash == old_hash:
            print("[INFO] requirements.txt tidak berubah, skip install.")
            return

    print("[INFO] requirements.txt berubah, install dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )

        with open(HASH_FILE, "w") as f:
            f.write(current_hash)

        print("[INFO] Dependencies berhasil diupdate.")
    except Exception as e:
        print("[WARNING] Gagal install dependencies:", e)

def git_update():
    try:
        print("[INFO] Mengecek update dari GitHub...")
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("[INFO] Update selesai.")
            install_requirements_if_needed()
        else:
            print("[WARNING] Git gagal, lanjut tanpa update.")

    except Exception:
        print("[WARNING] Tidak bisa update (cek koneksi). Lanjutkan...")