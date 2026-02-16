import os
import shutil

base_dir = r"c:\Users\Asylzhan\Desktop\MYSTARTAPP-VelorAI\IngiteAI.V2\IngiteAI\backend"
apps = ['users', 'bots', 'chats']

for app in apps:
    mig_dir = os.path.join(base_dir, app, "migrations")
    bak_dir = os.path.join(base_dir, app, "migrations_bak")
    
    if os.path.exists(mig_dir):
        # Rename if potential valuable content, or just delete? 
        # Rename to be safe, but if bak exists, delete bak first.
        if os.path.exists(bak_dir):
            try:
                shutil.rmtree(bak_dir)
            except:
                pass
        try:
            os.rename(mig_dir, bak_dir)
            print(f"Renamed {mig_dir} to {bak_dir}")
        except Exception as e:
            print(f"Failed to rename {mig_dir}: {e}")
            # Try 5 delete
            try:
                shutil.rmtree(mig_dir)
                print(f"Deleted {mig_dir}")
            except Exception as e2:
                print(f"Failed to delete {mig_dir}: {e2}")

    # Create fresh
    try:
        os.makedirs(mig_dir, exist_ok=True)
        with open(os.path.join(mig_dir, "__init__.py"), 'w') as f:
            pass
        print(f"Created fresh {mig_dir}")
    except Exception as e:
        print(f"Failed to create {mig_dir}: {e}")
