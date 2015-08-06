#!/usr/bin/env python
# -*- coding: utf-8 -*-
# threading_names_log.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
