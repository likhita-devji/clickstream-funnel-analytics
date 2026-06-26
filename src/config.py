"""
Project Configuration File
"""

from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Directories
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Models Directory
MODEL_DIR = BASE_DIR / "models"

# Reports Directory
REPORT_DIR = BASE_DIR / "reports"

# Dashboard Directory
DASHBOARD_DIR = BASE_DIR / "dashboard"