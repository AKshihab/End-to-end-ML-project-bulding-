import logging
import os
from datetime import datetime
from pathlib import Path
# Create a logger
LOG_FILE =f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_dir="logs"

LOG_directory_PATH=os.path.join(Path.cwd(),log_dir)
LOG_PATH=os.path.join(LOG_directory_PATH,LOG_FILE)
os.makedirs(LOG_directory_PATH,exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
