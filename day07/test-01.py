import threading
from queue import Queue


class A(threading.Thread):
    def __init__(self, q, lis):
        super(A, self).__init__()
        self.q = q
        self.lis = lis

    def run(self):
        print('self.qsize is:{}'.format(self.q.qsize()))
        print('lis is : {}'.format(self.lis))
        self.q.put('a')
        self.lis.append('a')


class B(threading.Thread):
    def __init__(self, q, lis):
        super(B, self).__init__()
        self.q = q
        self.lis = lis

    def run(self):
        print(self.q.qsize())
        print(self.lis)


def main():
    lis = []
    q = Queue()
    a = A(q, lis)
    a.start()
    a.join()
    b = B(q, lis)
    b.start()
    b.join()
    print('主线程，子线程都结束')


if __name__ == '__main__':
    main()
