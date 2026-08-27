from importlib.metadata import version, PackageNotFoundError
from platformdirs import user_data_dir
from pathlib import Path
import sys

APP_NAME = "FControl"
APP_AUTHOR = "fishija"

try:
    APP_VERSION = version(APP_NAME)
except PackageNotFoundError:
    APP_VERSION = "0.1.0"

# Detect environment
IS_FROZEN = getattr(sys, "frozen", False)

# Base paths
if IS_FROZEN:
    # PyInstaller bundle (temporary extraction dir)
    BASE_PATH = Path(getattr(sys, "_MEIPASS", Path(sys.executable).parent))
else:
    # Dev environment
    BASE_PATH = Path(__file__).resolve().parents[2]

# User data directory (ALWAYS external)
DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Database
DB_PATH = DATA_DIR / "fcontrol_dev.db"

# App constants
CURRENCIES = ["PLN", "EUR", "USD"]
