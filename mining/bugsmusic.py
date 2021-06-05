import requests
from bs4 import BeautifulSoup

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = []

    def set_url(self, detail):
        self.result = requests.get(f'{self.url}{detail}').text

    def get_ranking(self):
        soup = BeautifulSoup(self.result, 'lxml')
        ls1 = soup.find_all(name = 'p', attrs = {"class":"title"})
        for i in ls1:
            print(i.find("a").text)

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.set_url('chartdate=20210605&charthour=11')
        bugs.get_ranking()


if __name__ == '__main__':
    Bugsmusic.main()