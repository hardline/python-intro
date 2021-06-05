class Calculator(object):

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num

    def sub(self):
        return self.first_num - self.second_num

    def mul(self):
        return self.first_num * self.second_num

    def div(self):
        return self.first_num / self.second_num

    @staticmethod
    def main():
        while 1:
            menu = input("0-종료 1-계산기")
            if menu == '0':
                break
            elif menu == '1':
                first_num = int(input('첫번째 수'))
                second_num = int(input('두번째 수'))
                calc = Calculator(first_num, second_num)
                print('*' * 30)
                print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
                print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
                print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
                print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
                print('*' * 30)
            else:
                print('잘못된 메뉴입니다')


if __name__ == '__main__':
    Calculator.main()