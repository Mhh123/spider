import json

import jsonpath

fp = open('book.json', 'r', encoding='utf-8')
string = fp.read()
fp.close()

obj = json.loads(string)
# print(obj)
ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
print('*'*80)
print(ret)
ret1 = jsonpath.jsonpath(obj, '$..author')
print('1'*80)
print(ret1)
ret2 = jsonpath.jsonpath(obj, '$.store.*')
print('2'*80)
print(ret2)

# 下标从0开始
ret3 = jsonpath.jsonpath(obj, '$..book[2]')
print('3'*80)
print(ret3)
# 获取最后一本书
# '$..book[@length-1]'
