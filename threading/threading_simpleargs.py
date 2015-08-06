#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test2.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import threading

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
