baby = 'angelababy'

"""
荆轲刺秦
风萧萧兮易水寒，
壮士一去兮不复还

"""


# a = eval('baby')
# print(a)

def demo():
    lt = []
    for i in range(1, 11):
        lt.append(i)
    return lt


#  生成器，保存了生成数据的方法，需要的时候再去生成

def lala():
    for i in range(1, 11):
        yield i
        yield '杨颖'

g = lala()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
