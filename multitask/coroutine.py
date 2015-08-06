#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import (
    print_function,
    division,
    unicode_literals,
    )

import time

import multitask


def coroutine_1():
    for i in range(3):
        print('c1')
        yield i


def coroutine_2():
    for i in range(3):
        print('c2')
        yield i


def speed_test_1():
    t_start = time.time()
    multitask.add(coroutine_1())
    multitask.add(coroutine_2())
    multitask.run()
    print('sp1: {0} [ms]'.format((time.time() - t_start)*1000))


def speed_test_2():
    t_start = time.time()
    list(coroutine_1())
    list(coroutine_2())
    print('sp2: {0} [ms]'.format((time.time() - t_start)*1000))


if __name__ == '__main__':
    print("sp1-----")
    speed_test_1()
    print("sp2-----")
    speed_test_2()
