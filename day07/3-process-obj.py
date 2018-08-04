from multiprocessing import Process
import time

class SingProcess(Process):
    def __init__(self, name):
        #  手动调用父类的构造方法
        super().__init__()
        self.name = name
    def run(self):
        # 启动的时候自动运行这个run方法
        print('xxx is %s' % self.name)
        for x in range(5):
            print('-'*70, 'sing', x)
            time.sleep(1)


class DanceProcess(Process):
    def run(self):
        # 启动的时候自动运行这个run方法
        for x in range(5):
            print('-'*70, 'dance', x)
            time.sleep(1)



def main():
    name = '陈独秀'
    p_sing = SingProcess(name)
    p_dance = DanceProcess()

    p_sing.start()
    p_dance.start()

    p_sing.join()
    p_dance.join()

    print('主进程和子进程都结束')


if __name__ == '__main__':
    main()
