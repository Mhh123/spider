import time
from multiprocessing import Process

count = 100

def change(name):
    global count
    count += 100
    print('进程%s修改后的值为%s' % (name, count))

def read(name):
    #  为了保证修改程序执行完毕，停顿一下
    time.sleep(2)
    print('进程%s修改后的值为%s' % (name, count))

def main():
    p_c = Process(target=change, args=('修改', ))
    p_r = Process(target=read, args=('读取', ))


    p_c.start()
    p_r.start()

    p_c.join()
    p_r.join()

    print('主进程，子进程全部运行结束')



if __name__ == '__main__':
    main()