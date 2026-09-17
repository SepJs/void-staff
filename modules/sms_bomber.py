"""
Void Staff - SMS Bombing Module
"""

import requests
import threading
import time
import random
import hashlib
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

from modules.utils import (
    print_info, print_success, print_error, print_warning,
    generate_random_device_id, get_random_user_agent
)
from config.settings import TIMEOUT, IRAN_PHONE_PATTERN


class SMSBomber:
    """SMS Bombing attack module."""
