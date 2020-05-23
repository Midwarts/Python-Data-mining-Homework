import random
count = 0
class Media(object):
    """媒体类"""
    def __init__(self, media_name, media_web):
        self._media_name = media_name
        self._media_web = media_web
        global count
        count += 1#每调用一次就+1，以此来计算媒体名和网址数量

    @property
    def get_media_name(self):
        return self._media_name

    @property
    def get_media_web(self):
        return self._media_web

    def __str__(self):
        return '媒体名称是s%' % self._media_name

    def origin(self):#解决媒体来源
        a = random.randint(0,3)
        if a == 0:
            media_name = '澎湃新闻'
            media_web ='https://www.thepaper.cn/list_25635'
        elif a == 1:
            media_name = '新京报'
            media_web = 'http://www.bjnews.com.cn/'
        else:
            media_name = 'bilibili'
            media_web = 'https://www.bilibili.com/'
        # print('媒体名字是',media_name)
        # print('网址是',media_web)

def main():
    # 通过类方法创建对象并获取系统时间
    media = Media ('MEDIA','WEB')
    print(media.origin())


if __name__ == '__main__':
    main()