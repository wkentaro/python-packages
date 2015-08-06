#!/usr/bin/env python
# -*- coding: utf-8 -*-
# threading_subclass.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')

for i in range(5):
    t = MyThread()
    t.start()
