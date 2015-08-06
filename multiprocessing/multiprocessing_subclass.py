#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_subclass.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing


class Worker(multiprocessing.Process):
    def run(self):
        print 'In %s' % self.name
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
