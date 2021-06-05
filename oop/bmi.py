class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        index = self.weight / self.height ** 2 * 10000
        if index >= 35:
            bmi = '고도 비만'
        elif index >= 30:
            bmi = '중도 비만'
        elif index >= 25:
            bmi = '경도 비만'
        elif index >= 23:
            bmi = '과체중'
        elif index >= 18.5:
            bmi = '정상'
        else:
            bmi = '저체중'

        return bmi

    @staticmethod
    def main():
        while 1:
            menu = input("0-종료 1-BMI")
            if menu == '0':
                break
            elif menu == '1':
                height = int(input('키'))
                weight = int(input('몸무게'))
                bmi = Bmi(height, weight)
                print('*' * 30)
                print(f'키 : {bmi.height}, 몸무게 : {bmi.weight} -> {bmi.get_bmi()}')
                print('*' * 30)
            else:
                print('잘못된 메뉴입니다')


if __name__ == '__main__':
    Bmi.main()