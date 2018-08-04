import json


lt = [
    {'name':'王静','age':'8','height':'120'},
    {'name':'闫晓红','age':'14','height':'165'},
    {'name':'刘慧芳','age':'17','height':'162'},
    {'name':'赵铁柱','age':'20','height':'180'}
]

string = json.dumps(lt, ensure_ascii=False)

print(string)
print(type(string))
obj = json.loads(string)

print(obj)
print(type(obj))