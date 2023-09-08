import logging
import os , sys
from datetime import datetime


LOG_FILE = "logs"
LOG_DIR = os.path.join(os.getcwd(),LOG_FILE)

os.makedirs(LOG_DIR,exist_ok=True)



CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"

LOG_FILE_PATH = os.path.join(LOG_DIR,FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
                    level=logging.INFO)
