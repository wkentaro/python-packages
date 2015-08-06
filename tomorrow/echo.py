#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from tomorrow import threads

@threads(5)
def echo():
    print('echo')
    time.sleep(1)

if __name__ == '__main__':
    start = time.time()
    for i in xrange(5):
        echo()
    end = time.time()
    print('Time: {} seconds'.format(end - start))