"""
Void Staff - Configuration Settings
"""

# Application Info
APP_NAME = "Void Staff"
APP_VERSION = "1.0.0"
APP_AUTHOR = "HackerAI"

# General Settings
DEFAULT_THREADS = 50
DEFAULT_DELAY = 0.1
DEFAULT_RAT_PORT = 9999
DEFAULT_C2_PORT = 8888

# Iran Phone Number Pattern
IRAN_PHONE_PATTERN = r'^09[0-9]{9}$'

# Directory Paths (set in main.py)
BASE_DIR = None
DATA_DIR = None
LOGS_DIR = None
PAYLOADS_DIR = None

# Network Settings
PROXY = None
TIMEOUT = 10

# User-Agents for Rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
]

# CLI Colors
COLORS = {
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "green": "\033[92m",
    "red": "\033[91m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
}
