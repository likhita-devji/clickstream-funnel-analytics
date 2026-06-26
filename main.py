from src.config import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODEL_DIR,
    REPORT_DIR,
    DASHBOARD_DIR
)

from src.utils import create_directories

print("=" * 60)
print("Predictive Clickstream Pipeline")
print("=" * 60)

create_directories([
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODEL_DIR,
    REPORT_DIR,
    DASHBOARD_DIR
])

print("\nProject Initialized Successfully.")