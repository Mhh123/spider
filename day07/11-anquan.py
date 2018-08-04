import threading
import time

count = 100

#  创建一把锁
lock = threading.Lock()

def demo(n):
    global count
    for x in range(1, 1000000):
        lock.acquire()
        count += n
        count -= n
        lock.release()
    print('%s--线程，运行完之后count值为%s' % (threading.current_thread().name, count))


def main():
    t1 = threading.Thread(target=demo, name='haha', args=(5,))
    t2 = threading.Thread(target=demo, name='xixi', args=(3,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('主线程读取的值%s' % count)
    print('主线程，子线程全部运行结束')


if __name__ == '__main__':
    main()
