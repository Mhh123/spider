import os
import time
from multiprocessing import Pool


def test(name):
    print('%s--任务的进程id号为%s' % (name, os.getpid()))
    time.sleep(2)


def main():
    #  创建一个进程池，3代表池里面的进程数
    pol = Pool(3)
    #  所有的任务写到一个列表中
    lt = ['关羽', '张飞', '赵云', '马超', '黄忠', '许褚', '典韦', '张郃', '张辽']

    for name in lt:
        #  向池子中添加任务
        pol.apply_async(func=test, args=(name,))

    #  提那家玩任务后，将池子关闭
    pol.close()
    #  主进程等待进程池中所有的进程结束
    pol.join()
    print('主进程，子进程全部运行结束')


if __name__ == '__main__':
    main()
