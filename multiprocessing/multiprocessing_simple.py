#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_simple.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing

def worker():
    """worker function"""
    print 'Worker'


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()