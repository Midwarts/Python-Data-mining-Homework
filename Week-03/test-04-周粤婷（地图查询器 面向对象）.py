import json
data_json = open("中国地名表.json","r",encoding='gbk')
data_dict = json.load(data_json)

class Place():
    def __init__(self,place,up_name,down_name):
        self.place=place
        self.up_name= up_name
        self.down_name=down_name

    def is_province(self):
        if self.place in data_dict['root'].values():
            print("您查找的是国家")
            self.up_name.append('无上级地名')
            for i in range(len(data_dict['root']['province'])):
                self.down_name.append(data_dict['root']['province'][i]['name'])
            print("上级地名为：")
            print(self.up_name)
            print("下级地名为：")
            print(self.down_name)
        else:
            for i in range(len(data_dict['root']['province'])):
                if self.place in data_dict['root']['province'][i].values():
                    print("你要查找的是省")
                    self.up_name.append("中国")
                    if type(data_dict['root']['province'][i]['city'])==dict:
                        print("你要查找的是省直辖市")
                        for n in range(len(data_dict['root']['province'][i]['city']['area'])):
                            self.down_name.append(data_dict['root']['province'][i]['city']['area'][n]['name'])
                        print("上级地名为：")
                        print(self.up_name)
                        print("下级地名为：")
                        print(self.down_name)
                    else:
                        print("你要找的是非直辖市的省")
                        for n in range(len(data_dict['root']['province'][i]['city'])):
                            self.down_name.append(data_dict['root']['province'][i]['city'][n]['name'])
                        print("上级地名为：")
                        print(self.up_name)
                        print("下级地名为：")
                        print(self.down_name)
    def is_city(self):
        for i in range(len(data_dict['root']['province'])):
            if type(data_dict['root']['province'][i]['city']) == list:
                for j in range(len(data_dict['root']['province'][i]['city'])):
                    if self.place in data_dict['root']['province'][i]['city'][j].values():
                        print("你查询的是市")
                        self.up_name.append(data_dict['root']['province'][i]['name'])
                        for n in range(len(data_dict['root']['province'][i]['city'][j]['area'])):
                            self.down_name.append(data_dict['root']['province'][i]['city'][j]['area'][n]['name'])
                        print("上级地名为：")
                        print(self.up_name)
                        print("下级地名为：")
                        print(self.down_name)

    def is_area(self):
        # if is_province()==False and is_city()==False:
            for i in range(len(data_dict['root']['province'])):
                if type(data_dict['root']['province'][i]['city']) == list:
                    for j in range(len(data_dict['root']['province'][i]['city'])):
                        if type(data_dict['root']['province'][i]['city'][j].setdefault('area')) == list:
                            for k in range(len(data_dict['root']['province'][i]['city'][j]['area'])):
                                if self.place in data_dict['root']['province'][i]['city'][j]['area'][k].values():
                                    print('你查询的是区县')
                                    self.up_name.append(data_dict['root']['province'][i]['city'][j]['name'])
                                    self.down_name.append("无下级地名")
                                    print("上级地名为：")
                                    print(self.up_name)
                                    print("下级地名为：")
                                    print(self.down_name)
                if type(data_dict['root']['province'][i]['city']) ==dict:
                    for k in range(len(data_dict['root']['province'][i]['city']['area'])):
                        if self.place in data_dict['root']['province'][i]['city']['area'][k].values():
                            print('你查询的是区县')
                            self.up_name.append(data_dict['root']['province'][i]['city']['name'])
                            self.down_name.append("无下级地名")
                            print("上级地名为：")
                            print(self.up_name)
                            print("下级地名为：")
                            print(self.down_name)
def main():
    place_diy = Place(place=input("请输入想要查询的地名："),up_name = [],down_name = [])


    place_diy.is_province()
    place_diy.is_city()
    place_diy.is_area()




if __name__ == '__main__':
    main()
