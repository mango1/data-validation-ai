print("hello!")
print('hello'+' world'+'你好！')
print("hello \n\"let\'s go\"")
print("你好" + " 这里是一条代码")
#
import math
a = -1
b = -2
c = 3

x = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
x1 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
print(x)
print(x1)

# BMI = 体重 / (身高 ** 2)
user_weight = input("请输入您的体重(单位：kg) : ")
user_height = input("请输入您的身高(单位：米) : ")
user_BMI = float(user_weight) / float(user_height) ** 2
print("您的BMI是： " + str(user_BMI))