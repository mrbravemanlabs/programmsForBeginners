# # hello world program
# print("Hello, World!")

# # person greeting 
# def greet_person(name):
#     print(f"Hello, {name}!") 

# greet_person("Pawan")

# #simple calculator
# def calculate(operations,firstNum,secondNum):
#     if(operations == 1):
#         return(firstNum + secondNum)
#     elif(operations == 2):
#         return(firstNum-secondNum)
#     elif(operations == 3):
#         return(firstNum * secondNum)
#     elif(operations == 4):
#         return(firstNum/secondNum)
#     else:
#         return

# def simpleCalculator():
#     operations=int(input(
#         '''
# please enter your operations:
# 1.addition           2.substraction
# 3.multiplication     4.division
# '''
#     ))
#     if(not operations):
#         print("Please Restart The Program And Select An Operation")
#         return
#     firstNum=int(input("Enter The First Number"))
#     secondNum = int(input("Enter The Second Number"))
#     if(not secondNum or not firstNum):
#          print("Restart The Program There Is No Any Operation")
#          return
#     result = calculate(operations,firstNum,secondNum)
#     print(result)

# simpleCalculator()

# temperature convertor
# def convert(to, temperature):
#     if(to == 1):
#         return(temperature * 1.8)+32
#     elif(to == 2):
#         return(temperature-32)/1.8
#     else:return

# def temperatureConvertor():
#     to = int(input('''
# enter 1 to convert to farhenheit
# enter 2 to convert to celsius
# '''))
#     temperature=int(input("enter your temperature"))
#     convertedTemperature=convert(to,temperature)
#     print(f"Your converted temperature is : {convertedTemperature}")

# temperatureConvertor()

def areaOfRectangle():
    length=int(input("Please Enter Length Of Rectangle : "))
    bredth=int(input("Please Enter Breadth Of Rectangle"))