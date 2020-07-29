#add date and time of trace
import logging

def add_log(exp):
    logging.basicConfig(filename = 'log.txt', filemode = 'a', level= logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
    #logging.error(str(exp))