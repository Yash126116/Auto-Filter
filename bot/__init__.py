
import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID", "20089140"))

API_HASH = os.environ.get("API_HASH", "ced029e2c26de221aa2284d483dd7945")

BOT_TOKEN = "7087774258:AAHkxkjCf2AcH14w4-tZ9I36ZxjmIQjI0rs"

DB_URI = "mongodb+srv://yash14:Yash25@cluster0.qhyz4vx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

USER_SESSION = "BQEyiTQALhM4HcH-F6bP02-eIkejv6osG7Y-uhpJ0HmhpOVGYUQERjRQ5bjLuY2crR0FKV3NJan-e-oydfe_SYgOt7cPWotMf9S7wcVXCZoxNIGOxhZwzv-af0vNFaZezCQfQRKLXsuu4s5RRqCB-pHtCfClOoFnCUyQPFU4fMuKMKEYg4SkmjgSl_bhH71F1Zr7sjicD31KbRX_du0gOoPmvizTiGgR9U4qqXVretnP5rTjg1LtbUoNCW2qNNU2A5G25fhm5lZzj0LVULHLRabqJScwli5u-8nqs30DlYMhGyVptWTg066a0u_iid5jc6eTc8DvY1W_BB2o_Cl81KKhbcR7bQAAAABR6IgHAA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
