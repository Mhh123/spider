def func1(lis):
    print('*'*50, lis)
    lis.append('a')
    print('*'*50, lis)


def func2(lis):
    print('-'*50, lis)


def main():
    lis = []
    func1(lis)
    func2(lis)
    print('最后:{}'.format(lis))


if __name__ == '__main__':
    main()