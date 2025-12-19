import subprocess

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
        else:
            print("[WARNING] Git gagal, lanjut tanpa update.")

    except Exception:
        print("[WARNING] Tidak bisa update (cek koneksi). Lanjutkan...")