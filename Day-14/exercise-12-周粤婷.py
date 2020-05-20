class Media(object):
    count = 0
    def __init__(self,name,url):
        Media.count += 1
        self.name = name
        self.url = url
    def name_(self):
        return self.name
    def url_(self):
        return self.url
class Update_media(Media):
    def __str__(self):
        return "媒体名为%s"% (self.name)
def main():
    media_list=[Update_media("澎湃新闻","https://m.thepaper.cn/"),Update_media("南方都市报","https://http://www.oeeee.com/")]
    for media in media_list:
        media.name_()
        media.url_()
        media.__str__()
    print("一共实例了%d个媒体"% Media.count)
if __name__ == '__main__':
    main()