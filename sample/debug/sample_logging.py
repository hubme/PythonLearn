# https://docs.python.org/zh-cn/3/howto/logging.html#logging-basic-tutorial

import logging

# 默认级别为 WANNING，不会显示低于该级别的信息。
# logging.basicConfig(filename='example.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WANNING")
logging.error("ERROR")
logging.critical("CRITICAL")
