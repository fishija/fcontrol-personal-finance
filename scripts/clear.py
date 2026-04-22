import shutil
import os

from fcontrol.config import DB_PATH


def clear_cache():
    # clear all __pycache__ directories
    for root, dirs, files in os.walk("."):
        for dir in dirs:
            if dir == "__pycache__":
                cache_path = os.path.join(root, dir)
                shutil.rmtree(cache_path)
                print(f"Removed cache directory: {cache_path}")


def clear_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed database file at {DB_PATH}.")
    else:
        print(f"Database file at {DB_PATH} does not exist.")


if __name__ == "__main__":
    clear_cache()
    clear_db()
