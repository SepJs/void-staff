"""
Void Staff - Utility Functions
"""

import os
import sys
import re
import random
import hashlib
import platform
from colorama import init, Fore, Style

init(autoreset=True)


def get_system():
    """Return the current operating system name."""
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Darwin":
        return "macos"
    else:
        return "linux"


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if get_system() == "windows" else 'clear')


def print_banner():
    """Display the application banner."""
    banner = f"""
{Fore.CYAN}
   _____  _   _    ____  _     _     ____  _   _  _____  ____  _____  _   _  
  / ____|| | | |  / __ \| |   | |   / __ \| | | |/ ____|/ __ \|  __ \| | | | 
 | (___  | |_| | | |  | | |   | |  | |  | | | | | (___ | |  | | |  | | |_| | 
  \___ \ |  _  | | |  | | |   | |  | |  | | | | |\___ \| |  | | |  | |  _  | 
  ____) || | | | | |__| | |___| |  | |__| | | | |____) | |__| | |__| | | | | 
 |_____/ |_| |_|  \____/ \_____/_   \____/ \_| |_______\____/|_____/|_| |_| 
                                 _/                                        
                                |___|                                       
{Fore.YELLOW}Mobile Hacking Toolkit v1.0{Fore.CYAN}
{Fore.MAGENTA}Cross-Platform Edition - {get_system().upper()}{Fore.CYAN}
    """
    print(banner)


def validate_phone(phone):
    """Validate Iranian phone number format."""
    pattern = r'^09[0-9]{9}$'
    return bool(re.match(pattern, str(phone)))


def generate_random_device_id():
    """Generate a random device ID."""
    return hashlib.md5(str(random.random()).encode()).hexdigest()[:16]


def get_random_user_agent():
    """Return a random User-Agent string."""
    from config.settings import USER_AGENTS
    return random.choice(USER_AGENTS)


def print_success(msg):
    """Print a success message."""
    print(f"{Fore.GREEN}[✓] {msg}{Style.RESET_ALL}")


def print_error(msg):
    """Print an error message."""
    print(f"{Fore.RED}[✗] {msg}{Style.RESET_ALL}")


def print_info(msg):
    """Print an informational message."""
    print(f"{Fore.CYAN}[*] {msg}{Style.RESET_ALL}")


def print_warning(msg):
    """Print a warning message."""
    print(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")


def load_services(filepath):
    """Load SMS services from a JSON file."""
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        print_error(f"Invalid JSON: {filepath}")
        return []


def save_log(message, logs_dir="logs"):
    """Save a message to the log file."""
    import datetime
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(logs_dir, "void_staff.log")
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
