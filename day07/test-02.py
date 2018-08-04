import threading
from queue import Queue


class A(object):
    def __init__(self, q, lis):
        print('添加前 lis :', lis)
        super(A, self).__init__()
        self.q = q
        self.lis = lis
        print('添加前 self.lis:', self.lis)
        self.lis.append('a')
        print('添加后 lis:', lis)
        print('添加后 self.lis:', self.lis)



class B(object):
    def __init__(self, q, lis):
        print('-----', lis)
        super(B, self).__init__()
        self.q = q
        self.lis = lis



def main():
    lis = []
    q = Queue()
    a = A(q, lis)
    print('最后 self.lis :', getattr(a, 'lis'))
    print('最后  lis:', lis)

    # b = B(q, lis)
    # print(getattr(b, 'lis'))
    #
    # print('主线程，子线程都结束')
    # print(getattr(a, 'lis'))


if __name__ == '__main__':
    main()
