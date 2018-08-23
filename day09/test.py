baby = 'angelababy'
'''
细思极恐
你的对手在看书
你的敌人在磨刀
你的闺蜜在减肥
隔壁老王在炼妖
'''

'''
a = eval('baby')
print(a)
'''

def demo():
    lt = []
    for i in range(1, 11):
        lt.append(i)
    return lt

# 生成器，保存了生成数据的方法，需要的时候再去生成即可
def lala():
    for i in range(1, 11):
        yield i
        yield '杨颖'
    yield '黄晓明'

g = lala()

print(next(g))
print(next(g))
print(next(g))
print(next(g))