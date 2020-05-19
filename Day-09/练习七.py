import json
path = 'E:\\json\\mangguo.json'
#路径
new = []
#新的存储位置，一会把提取内容放进去

with open(path,'r',encoding = 'utf-8',errors = 'ignore') as f:
    danmu_py = json.load(f)
    #转换为python对象
    data = danmu_py['data']
    for x in data:
        if x[0] == 'NM':
             new.append(x[3])

filename = 'E:\\json\\new.txt'
with open(filename,'w',errors='ignore')as f2:
    #写入
    for x in new:
        f2.write(x)
        f2.write('\n')

#finally
print('搞定')