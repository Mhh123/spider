import os
import time
from multiprocessing import Process


def sing(*args):
    print('aaaaaaaaaaaaa', args)
    #aaaaaaaaaaaaa ('刘慧芳', 18)
    print('获取父进程pid', os.getppid())
    #获取父进程pid 5324
    for i in range(5):
        print('i am sing', i)
        time.sleep(1)


def dance(args):
    print('bbbbbb', args)
    # bbbbbb 刘慧芳
    for i in range(5):
        print('iam dancing', i)
        time.sleep(1)


def main():
    name = '刘慧芳'
    age = 18

    #主进程的id
    print(os.getpid())
    #  5324
    # 创建唱歌进程
    p_sing = Process(target=sing, args=(name, age))
    # 创建跳舞进程
    p_dance = Process(target=dance, args=(name,))

    # 启动进程
    p_sing.start()
    p_dance.start()

    #主进程里面有子进程的信息，
    #所以主进程要等待子进程结束,才能结束主进程
    p_sing.join()
    p_dance.join()

    # 结束语
    print('主进程，子进程全部结束')


if __name__ == '__main__':
    main()
