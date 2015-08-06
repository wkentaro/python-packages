#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing_producer_consumer.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import multiprocessing
import time

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill は終了を意味します
                print '%s: Exiting' % proc_name
                self.task_queue.task_done()
                break
            print '%s: %s' % (proc_name, next_task)
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return


class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1) # この処理に少し時間がかかることを意図しています
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)

    def __str__(self):
        return '%s * %s' % (self.a, self.b)


if __name__ == '__main__':
    # コミュニケーションキューを作成する
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    # consumers 処理を開始する
    num_consumers = multiprocessing.cpu_count() * 2
    print 'Creating %d consumers' % num_consumers
    consumers = [ Consumer(tasks, results)
            for i in xrange(num_consumers) ]
    for w in consumers:
        w.start()
    # ジョブをキューへ入れる
    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i, i))
    # 各 consumer へ poison pill を追加する
    for i in xrange(num_consumers):
        tasks.put(None)
    # 全てのタスクの終了を待つ
    tasks.join()
    # 結果を表示し始める
    while num_jobs:
        result = results.get()
        print 'Result:', result
        num_jobs -= 1