#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_import_main.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker)
        jobs.append(p)
        p.start()
