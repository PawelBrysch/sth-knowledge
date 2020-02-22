import logging
import os

logname = os.path.join(
    rf"E:\plauground_one\temp",
    "some_log.txt")

logging.basicConfig(
    filename=logname,
    filemode='w',
    level=logging.INFO
    )

logging.info("some info")



