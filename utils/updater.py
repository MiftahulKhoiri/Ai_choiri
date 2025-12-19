import subprocess
import sys
import os

def install_requirements():
    if not os.path.exists("requirements.txt"):
        print("[INFO] requirements.txt tidak ditemukan, skip instalasi.")
        return

    try:
        print("[INFO] Menginstal dependencies dari requirements.txt...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )
        print("[INFO] Dependencies berhasil diinstal.")
    except Exception:
        print("[WARNING] Gagal install dependencies, lanjutkan program.")

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
            install_requirements()
        else:
            print("[WARNING] Git gagal, lanjut tanpa update.")

    except Exception:
        print("[WARNING] Tidak bisa update (cek koneksi). Lanjutkan...")