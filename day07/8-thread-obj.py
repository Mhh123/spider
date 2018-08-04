import threading
import time


class SingThread(threading.Thread):
    def __init__(self, name):
        super(SingThread, self).__init__()
        self.name = name

    def run(self):
        print('唐诗:%s' % self.name)
        for i in range(5):
            print('i like sing %s' % i)
            time.sleep(1)


class DanceThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('i like dance %s' % i)
            time.sleep(1)


def main():
    name = '旧时王谢堂前燕，飞入寻常百姓家'
    t_sing = SingThread(name)
    t_dance = DanceThread()

    t_sing.start()
    t_dance.start()

    t_sing.join()
    t_dance.join()

    print('主线程，子线程都结束')


if __name__ == '__main__':
    main()
