import logging
import time

logging.basicConfig(filename = r"C:\Users\Arun\Desktop\problems.log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_time(path):
    start_time = time.time()
    try:
        f = open(path,mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info('Time required for {file} = {time}'.format(file=path, time=dt))

data = read_file_time(r"C:\Users\Public\Videos\Sample Videos\Wildlife.wmv")
