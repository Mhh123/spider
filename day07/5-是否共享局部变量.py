import time
from multiprocessing import Process

def demo(name):
    count = 100
    #  通过name来区分是哪个进程
    if name == 'change':
        count += 100
        print('修改进程后的值为%s' % count)
    else:
        time.sleep(2)
        print('读取的值为%s' % count)


def main():
    pc = Process(target=demo, args=('change', ))
    pr = Process(target=demo, args=('read', ))


    pc.start()
    pr.start()

    pc.join()
    pr.join()

    print('主进程，子进程都结束')

if __name__ == '__main__':
    main()