# File: backend/shared.py (New File)
# This file holds shared instances to prevent circular imports.

from slowapi import Limiter
from slowapi.util import get_remote_address

# Initialize the rate limiter here
limiter = Limiter(key_func=get_remote_address)