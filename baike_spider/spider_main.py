# 总调度程序

from mooc.webSpiders.baike_spider import html_downloader, url_manager, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutpter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)

        # 若self.urls中还存在url则循环
        while self.urls.has_new_url():
            try:
                # 每次从self.urls中拿新的页面
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                # 下载新的页面的html
                html_count = self.downloader.download(new_url)
                # 进行页面的解析,得到新的urls和数据
                new_urls, new_data = self.parser.parse(new_url, html_count)
                # 将新得到的urls加入self.urls中
                self.urls.add_new_urls(new_urls)
                # 数据收集
                self.outputer.collect_data(new_data)

                count = count + 1

                if count == 1000:
                    break
            except:
                print("craw failed")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)