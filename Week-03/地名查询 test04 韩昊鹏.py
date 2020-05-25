import json
data_json = open("D:\hhp代码文件夹\week3大作业\中国地名表.json","r",encoding='gbk')     #encoding参数是gbk（国标）
data_dict = json.load(data_json)            #将json数据反序列化成python对象
place = input("请输入想要查询的地名：")
up_name=[]   #新建list
down_name=[]    #新建list
def is_province():
    if place == data_dict["root"]["name"]:
        print("您查找的是国家")
        up_name.append('无上级地名')
        for i in range(len(data_dict['root']['province'])):   #len函数，用于返还对象长度或项目个数，这里边就是返回有多少个prinvince
            down_name.append(data_dict['root']['province'][i]['name'])
        print("上级地名为："+str(up_name))
        print("下级地名为："+str(down_name))
    else:
        for i in range(len(data_dict['root']['province'])):
            #print('1',data_dict['root']['province'][i].values())   #打印出来就会发现，打印的是province结构下的所有子项，所以不能用简单的判断
            if place in data_dict['root']['province'][i].values():     #判断place是不是在province项、子项的值中，参看in函数案例
                print("你要查找的是省")
                up_name.append("中国")
                if type(data_dict['root']['province'][i]['city'])==dict:     #只有直辖市的['root']['province']['city']是字典形式
                    print("你要查找的是省直辖市")
                    for n in range(len(data_dict['root']['province'][i]['city']['area'])):
                        down_name.append(data_dict['root']['province'][i]['city']['area'][n]['name'])
                    print("上级地名为：" + str(up_name))
                    print("下级地名为："+str(down_name))
                else:
                    print("你要找的是非直辖市的省")
                    for n in range(len(data_dict['root']['province'][i]['city'])):
                        down_name.append(data_dict['root']['province'][i]['city'][n]['name'])
                    print("上级地名为：" + str(up_name))
                    print("下级地名为：" + str(down_name))
def is_city():
    for i in range(len(data_dict['root']['province'])):
        if type(data_dict['root']['province'][i]['city']) == list:      #非直辖市，就是市级单位而不是省级单位了
            for j in range(len(data_dict['root']['province'][i]['city'])):
                if place in data_dict['root']['province'][i]['city'][j].values():
                    print("你查询的是市")
                    up_name.append(data_dict['root']['province'][i]['name'])
                    for n in range(len(data_dict['root']['province'][i]['city'][j]['area'])):
                        down_name.append(data_dict['root']['province'][i]['city'][j]['area'][n]['name'])
                    print("上级地名为：" + str(up_name))
                    print("下级地名为：" + str(down_name))
def is_area():
    # if is_province()==False and is_city()==False:
        for i in range(len(data_dict['root']['province'])):
            if type(data_dict['root']['province'][i]['city']) == list:
                for j in range(len(data_dict['root']['province'][i]['city'])):
                    if type(data_dict['root']['province'][i]['city'][j].setdefault('area')) == list:
                        for k in range(len(data_dict['root']['province'][i]['city'][j]['area'])):
                            if place in data_dict['root']['province'][i]['city'][j]['area'][k].values():
                                print('你查询的是区县')
                                up_name.append(data_dict['root']['province'][i]['city'][j]['name'])
                                down_name.append("无下级地名")
                                print("上级地名为：" + str(up_name))
                                print("下级地名为：" + str(down_name))
            if type(data_dict['root']['province'][i]['city']) ==dict:
                for k in range(len(data_dict['root']['province'][i]['city']['area'])):
                    if place in data_dict['root']['province'][i]['city']['area'][k].values():
                        print('你查询的是区县')
                        up_name.append(data_dict['root']['province'][i]['city']['name'])
                        down_name.append("无下级地名")
                        print("上级地名为：" + str(up_name))
                        print("下级地名为：" + str(down_name))
def main():
    is_province()
    is_city()
    is_area()

if __name__ == '__main__':
    main()