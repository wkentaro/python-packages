#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_log_to_stderr.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing
import logging
import sys

def worker():
    print 'Doing some work'
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()