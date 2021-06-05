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
        calc = Calculator(6, 2)
        print('*' * 30)
        print(f'{calc.first_num} + {calc.second_num} = {calc.add()}')
        print(f'{calc.first_num} - {calc.second_num} = {calc.sub()}')
        print(f'{calc.first_num} * {calc.second_num} = {calc.mul()}')
        print(f'{calc.first_num} / {calc.second_num} = {calc.div()}')
        print('*' * 30)

if __name__ == '__main__':
    Calculator.main()