import os
import glob

base_dir = r"c:\Users\Asylzhan\Desktop\MYSTARTAPP-VelorAI\IngiteAI.V2\IngiteAI\backend"
files = [
    os.path.join(base_dir, "db.sqlite3"),
    os.path.join(base_dir, "users", "migrations", "0001_initial.py"),
    os.path.join(base_dir, "bots", "migrations", "0001_initial.py"),
    os.path.join(base_dir, "bots", "migrations", "0002_faq.py"),
    os.path.join(base_dir, "chats", "migrations", "0001_initial.py"),
    os.path.join(base_dir, "chats", "migrations", "0002_alter_chat_unique_together_alter_chat_lead_type.py"),
]

for f in files:
    try:
        if os.path.exists(f):
            os.remove(f)
            print(f"Deleted {f}")
        else:
            print(f"Not found {f}")
    except Exception as e:
        print(f"Failed to delete {f}: {e}")
