"""
Utility Functions
"""

import os


def create_directories(paths):
    """
    Create directories if they don't exist.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)

    print("Project directories verified.")