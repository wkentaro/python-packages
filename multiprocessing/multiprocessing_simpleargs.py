#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_simpleargs.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()