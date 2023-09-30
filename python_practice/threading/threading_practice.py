import threading

import logging
import time

logging.basicConfig(filename ='app.log',
                        level = logging.DEBUG)

# create logger
logger = logging.getLogger('threading_practice')

formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
start = time.time()


def addition(a,b,c,d):
    logger.info(f'addition message_1 {a+b}')
    time.sleep(2)
    logger.info(f'addition message_2 {a+b+c}')
    time.sleep(2)
    logger.info(f'addition message_3 {a+b+c+d}')
    time.sleep(2)


def substraction(a,b,c,d):
    logger.info(f'subtraction message_1 {a-b}')
    time.sleep(2)
    logger.info(f'subtraction message_2 {a-b-c}')
    time.sleep(2)
    logger.info(f'subtraction message_3 {a-b-c-d}')
    time.sleep(2)


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=addition, args=(8,9,12,34))
    t2 = threading.Thread(target=substraction, args=(12,23,56,78))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    end = time.time()
    # both threads completely executed
    print(f"Done in seconds: {end-start}")

