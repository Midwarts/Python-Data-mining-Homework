#改写成类的时候报错，调整不来，暂时交这个版本
import json
data_json = open("中国地名表.json","r",encoding='gbk')
data_dict = json.load(data_json)
place = input("请输入想要查询的地名：")
up_name=[]
down_name=[]
def is_province():
    if place in data_dict['root'].values():
        print("您查找的是国家")
        up_name.append('无上级地名')
        for i in range(len(data_dict['root']['province'])):
            down_name.append(data_dict['root']['province'][i]['name'])
        print("上级地名为：")
        print(up_name)
        print("下级地名为：")
        print(down_name)
    else:
        for i in range(len(data_dict['root']['province'])):
            if place in data_dict['root']['province'][i].values():
                print("你要查找的是省")
                up_name.append("中国")
                if type(data_dict['root']['province'][i]['city'])==dict:
                    print("你要查找的是省直辖市")
                    for n in range(len(data_dict['root']['province'][i]['city']['area'])):
                        down_name.append(data_dict['root']['province'][i]['city']['area'][n]['name'])
                    print("上级地名为：")
                    print(up_name)
                    print("下级地名为：")
                    print(down_name)
                else:
                    print("你要找的是非直辖市的省")
                    for n in range(len(data_dict['root']['province'][i]['city'])):
                        down_name.append(data_dict['root']['province'][i]['city'][n]['name'])
                    print("上级地名为：")
                    print(up_name)
                    print("下级地名为：")
                    print(down_name)
def is_city():
    for i in range(len(data_dict['root']['province'])):
        if type(data_dict['root']['province'][i]['city']) == list:
            for j in range(len(data_dict['root']['province'][i]['city'])):
                if place in data_dict['root']['province'][i]['city'][j].values():
                    print("你查询的是市")
                    up_name.append(data_dict['root']['province'][i]['name'])
                    for n in range(len(data_dict['root']['province'][i]['city'][j]['area'])):
                        down_name.append(data_dict['root']['province'][i]['city'][j]['area'][n]['name'])
                    print("上级地名为：")
                    print(up_name)
                    print("下级地名为：")
                    print(down_name)

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
                                print("上级地名为：")
                                print(up_name)
                                print("下级地名为：")
                                print(down_name)
            if type(data_dict['root']['province'][i]['city']) ==dict:
                for k in range(len(data_dict['root']['province'][i]['city']['area'])):
                    if place in data_dict['root']['province'][i]['city']['area'][k].values():
                        print('你查询的是区县')
                        up_name.append(data_dict['root']['province'][i]['city']['name'])
                        down_name.append("无下级地名")
                        print("上级地名为：")
                        print(up_name)
                        print("下级地名为：")
                        print(down_name)
def main():
    is_province()
    is_city()
    is_area()

if __name__ == '__main__':
    main()
