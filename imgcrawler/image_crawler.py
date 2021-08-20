from icrawler.builtin import GoogleImageCrawler
import os


class ImageCrawler:
    def __init__(self, names):
        self.names = names

    def crawl(self):
        for name in self.names:
            os.mkdir(name)
            crawler = GoogleImageCrawler(storage={"root_dir": name})
            crawler.crawl(keyword=name, max_num=500)

    def split(self):
        if not os.path.exists("train"):
            os.mkdir("train")

        if not os.path.exists("validation"):
            os.mkdir("validation")




my_crawler = ImageCrawler(["gorilla", "orangutan", "chimpanzee"])
my_crawler.crawl()
my_crawler.split()
