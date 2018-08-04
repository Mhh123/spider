import os
import threading
import time


def sing(*args):
    print('a'*80)

    print('-' * 30, '参数args:{}'.format(args))
    for i in range(5):
        print('i am sing', i)
        time.sleep(1)


def dance(args):
    print('-' * 30, '参数args:%s' % args)
    for i in range(5):
        print('iam dancing', i)
        time.sleep(1)


def main():
    name = '王力宏'
    age = 10
    # Thread(target,name,args)  中的name是给线程起名的，不是参数；args才是参数
    t_sing = threading.Thread(target=sing, name='唱歌', args=(name, age))
    t_dance = threading.Thread(target=dance, name='跳舞', args=(name,))

    t_sing.start()
    t_dance.start()

    t_sing.join()
    t_dance.join()

    print('主线程，子线程全部结束')


if __name__ == '__main__':
    main()
