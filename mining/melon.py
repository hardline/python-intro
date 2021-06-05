import requests
from bs4 import BeautifulSoup


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self, detail):
        self.result = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.result, 'lxml')
        ls1 = soup.find_all(name='div', attrs={"class": "ellipsis rank01"})
        for i, title in enumerate(ls1):
            print(f'{i + 1}등 {title.find("a").text}')

    @staticmethod
    def main():
        bugs = Melon()
        bugs.set_url('dayTime=2021060515')
        bugs.get_ranking()


if __name__ == '__main__':
    Melon.main()
