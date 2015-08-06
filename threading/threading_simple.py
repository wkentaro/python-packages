#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test1.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import threading

def worker():
    """thread worker function"""
    print 'Worker'

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()