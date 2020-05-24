import json
'''
想分为两类，一类是直辖市，一类是普通的城市。
如果识别出是直辖市则用第一类运行，识别出是普通城市则用第二类运行
可是写普通城市的时候一直有错误，思路还有点理不清
没有来得及用类来实现了
'''

#打开文件
f = open('D:\\xm\\huabang\\Python-Data-mining-Tutorial\\Week-03\\中国地名表.json', 'r', encoding='ANSI')  # 需更改文件路径
f.close
json_data = json.load(f)
province = json_data['root']['province']
location=input('请输入要查找的地名：')

for x in range(len(province)):
    a = province[x]['city']

#直辖市 Class zhixiashi
    if(type(a))==dict:
        zhixiashi=a
        for y in range(len(zhixiashi['area'])):

            if location==zhixiashi['name']:
                print('上级',zhixiashi['name'],zhixiashi['name'],'下级',zhixiashi['area'][y]['name'])
#普通城市 Class normal_city
    if (type(a)) == list:

        for z in range(len(a)):
            city=a[z]
            for m in range(len(city['area'])):
                if location == city['name']:
                    print('上级',province[m]['name'],city['name'],'下级',city.get('area')[m]['name'])

#if(type(location))==dict: city=Class zhixiashi[location]
#if(type(location))==dict: city=Class normal_city[location]

