media_dict ={"不会起名":"bu.huiqi.ming","编不出来":"bian.buchu.lai","我放弃了":"wo.fangqi.le"}


#编写媒体类
class Media(object):
    count = 0
    def __init__(self, name, url):
        Media.count += 1
        self.name = name
        self.url = url
        

    def get_info(self):
        print('媒体名是',self.name)
        print('媒体网址是',self.url)

    def __str__(self):
        return '媒体名是%s'%(self.name)

for media in media_dict:
    a = (Media(media,media_dict[media]))
    a.get_info()
print('共实例化了%d个媒体'%Media.count)

for i in media_dict:
    print(i)
