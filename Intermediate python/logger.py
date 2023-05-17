import logging

logging.basicConfig(level=logging.INFO)

logging.info("You have 5 unread messages")
logging.critical("All componets have failed")

logger = logging.getLogger("Rhina Logger")
logger.info("A new logger was created")
logger.critical("Are you sure you want to delete this logger?")
logger.log(logging.ERROR, "An error has occured!")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.debug("This is a debug message")
logger.info("This is an information message")
