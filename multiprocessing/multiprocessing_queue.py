#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_queue.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import math
import random
import multiprocessing


class MyFancyClass(object):
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s!' % (proc_name, self.name)


def worker(q, n):
    obj = q.get()
    obj.do_something()
    print math.factorial(n)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    for i in range(3):
        rnd = random.randint(0, 100)
        p = multiprocessing.Process(target=worker, args=(queue, rnd))
        p.start()

        queue.put(MyFancyClass('FancyClass-{0}'.format(i)))

    # ワーカーが終了するまで待つ
    queue.close()
    queue.join_thread()
    p.join()
