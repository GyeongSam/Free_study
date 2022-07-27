class Calculator:

    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2
    
    def substract(self):
        return self.num1 - self.num2
    
    def multuply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2 if self.num2!=0 else '0으로 나눌 수 없습니다.'

add_test=Calculator(1,2)
sub_test=Calculator(2,1)
mul_test=Calculator(3,4)
div_test=Calculator(4,0)
print(add_test.add())
print(sub_test.substract())
print(mul_test.multuply())
print(div_test.divide())