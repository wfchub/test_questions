# -*- coding: utf-8 -*-

import pandas as pd
data=pd.read_csv('fyx_chinamoney.csv',header=None)#读入数据
# print(data)

code_list=data.values.tolist()#将DataFrame型数据转化为列表
# print(code_list)

batch_size=80#设置批大小
for i in range(0,len(code_list),batch_size):
    batch_code_list=code_list[i:i+batch_size]#切片
    print(batch_code_list)