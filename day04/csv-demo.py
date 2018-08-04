import ast
import csv
import os
import re

def writeCsv(path,data):    #把文件当做参数传进去
    """01写入数据"""
    global i
    with open(path,"w",newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # print(type(writer),writer,sep="\n")
        for rowdata in data:
            row_data_dic = eval(rowdata)
            row_data_lis = [row_data_dic['职位名称'],row_data_dic['公司名称'],row_data_dic['职位月薪'],row_data_dic['工作地点']]
            writer.writerow(row_data_lis)
            i=i+1
            print(i)
        # print("-->",type(writer))
        return writer


i=0

dirname = 'source'
if not os.path.exists(dirname):
    os.mkdir(dirname)


fp = open('work.txt', 'r', encoding='utf-8')
data = fp.read()

string = data[1:-1]
pattern = re.compile(r'{.*?}')
data_ = pattern.findall(string)
print(data_)
file_path = os.path.join(dirname,'work-txt.csv')
writeCsv(file_path,data_)
fp.close()
