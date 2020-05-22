# coding=utf-8

"""
目的：读取数据表中的数据并写入到Excel中，要求包含表头，表头为各字段的名字
读取数据表中的数据并写为Json格式的数据，要求每条记录为list中的一个元素，每个字段为元素的一个属性
作者：徐昭
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import xlwt
import json

def export_excel(table_name):
    conn = pymysql.connect(user='huabang_learning', host='rm-m5e63zf8ii67j7uq1zo.mysql.rds.aliyuncs.com',
                           port=3306, passwd='huabang_201904', db='huabang_learning', charset='utf8')
    cur = conn.cursor()

    sql = 'select * from %s;' % table_name

    # 读取数据
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description] # 返回域，可从中得到变量名
    all_date = cur.fetchall()   #得到所有列的内容
    print("------以下为您的表格内容------")
    for result in all_date:
        print(result)  # 打印所得

    # 写excel
    book = xlwt.Workbook()
    sheet = book.add_sheet('result')  # 创建一个sheet表

    for column, filed in enumerate(fileds):
        sheet.write(0, column, filed)    # 写表头内容

    row = 1   #填之后的主要信息
    for data in all_date:
        for column, filed in enumerate(data):
            sheet.write(row, column, filed)
        row += 1

    book.save('%s.xls' % table_name)

    print("------以下为您的表格json格式------")
    li = []
    for i in all_date:
        di = {}
        for j in range(len(i)):
            di[fileds[j]] = i[j]  #构造字典
        j = json.dumps(di)
        li.append(j)  # 拼凑
    print(li)

if __name__ == '__main__':
    export_excel('xuzhao_xialan')