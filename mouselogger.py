from pynput.mouse import Listener
from pynput import keyboard
import sys
import os
import logging

logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        logging.info('Mouse unclicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def on_press(key):
    logging.info('Keyboard press {0}'.format(key))
    if key is keyboard.Key.esc:
        os._exit(0)

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener, keyboard.Listener(on_press=on_press) as listener1:
    listener.join()
    listener1.join()