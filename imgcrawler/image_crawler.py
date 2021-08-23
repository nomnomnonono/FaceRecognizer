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
            if os.path.exists(name[1]):
                shutil.rmtree(name[1])

            os.mkdir(name[1])
            crawler = GoogleImageCrawler(storage={"root_dir": name[1]})
            crawler.crawl(keyword=name, max_num=self.num)

    def split(self, val_rate):
        if not os.path.exists("train"):
            os.mkdir("train")

        if not os.path.exists("validation"):
            os.mkdir("validation")

        for i in range(3):
            if not os.path.exists(f"train/{str(i)}"):
                os.mkdir(f"train/{str(i)}")

            if not os.path.exists(f"validation/{str(i)}"):
                os.mkdir(f"validation/{str(i)}")

        for name in self.names:
            files = glob.glob(os.path.join(str(name[1]), "*.jpg"))
            for i in range(len(files)):
                if i < (1-val_rate)*len(files):
                    shutil.copy(files[i], f"train/{str(name[0])}/{name[1]}{i}.jpg")
                else:
                    shutil.copy(files[i], f"validation/{str(name[0])}/{name[1]}{i}.jpg")
            shutil.rmtree(name[1])


my_crawler1 = ImageCrawler([(0, "gorilla"), (1, "orangutan"), (2, "chimpanzee")])
my_crawler1.crawl(100)
my_crawler1.split(0.2)
my_crawler2 = ImageCrawler([(0, "ゴリラ"), (1, "オラウータン"), (2, "チンパンジー")])
my_crawler2.crawl(100)
my_crawler2.split(0.2)
