import ast
import csv
import os
import re


def writeCsv(path, data):  # 把文件当做参数传进去
    """01写入数据"""
    global i
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # print(type(writer),writer,sep="\n")

        # 写入表的字段名
        key_list = []
        if len(key_list) == 0:
            for key in eval(data[0]).keys():
                key_list.append(key)
            writer.writerow(key_list)

        for rowdata in data:
            row_data_dic = eval(rowdata)
            row_data_lis = [row_data_dic[key] for key in key_list]
            writer.writerow(row_data_lis)
            i = i + 1
            print(i)
        # print("-->",type(writer))
        return writer


i = 0

dirname = 'source'
if not os.path.exists(dirname):
    os.mkdir(dirname)

fp = open('taobao.txt', 'r', encoding='utf-8')
data = fp.read()

string = data[1:-1]

pattern = re.compile(r'{.*?}')
data_ = pattern.findall(string)

file_path = os.path.join(dirname, 'taobao.csv')
writeCsv(file_path, data_)
fp.close()
