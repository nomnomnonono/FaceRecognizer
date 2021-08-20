from icrawler.builtin import GoogleImageCrawler
import glob
import os
import shutil


class ImageCrawler:
    def __init__(self, names):
        self.names = names

    def crawl(self, num):
        self.num = num
        for name in self.names:
            os.mkdir(name)
            crawler = GoogleImageCrawler(storage={"root_dir": name})
            crawler.crawl(keyword=name, max_num=self.num)

    def split(self, val_rate):
        if not os.path.exists("train"):
            os.mkdir("train")

        if not os.path.exists("validation"):
            os.mkdir("validation")

        for name in self.names:
            files = glob.glob(os.path.join(name, "*.jpg"))
            for i in range(len(files)):
                if i < (1-val_rate)*len(files):
                    shutil.copy(files[i], f"train/{name}{i}.jpg")
                else:
                    shutil.copy(files[i], f"validation/{name}{i}.jpg")


my_crawler = ImageCrawler(["gorilla", "orangutan", "chimpanzee"])
my_crawler.crawl(100)
my_crawler.split(0.2)
