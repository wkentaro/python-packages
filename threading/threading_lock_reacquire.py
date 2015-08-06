#!/usr/bin/env python
# -*- coding: utf-8 -*-
# threading_lock_reacquire.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import threading

lock = threading.RLock()

print 'First try: ', lock.acquire()
print 'Second try: ', lock.acquire(0)