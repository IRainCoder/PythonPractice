"""
GIL探索
"""
import time
from threading import Thread


def CountDown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    n = 1000000000
    # 单线程
    start_time = time.perf_counter()
    CountDown(n)
    end_time = time.perf_counter()
    print('cost {} seconds'.format(end_time - start_time))
    
    # # 多线程
    # start_time_t = time.perf_counter()
    # t1 = Thread(target=CountDown, args=(n//2,))
    # t2 = Thread(target=CountDown, args=(n//2,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # end_time_t = time.perf_counter()
    # print('Thread cost {} seconds'.format(end_time_t - start_time_t))



