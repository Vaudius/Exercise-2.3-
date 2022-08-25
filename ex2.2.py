#在3.0以上python中，input()函数，通过键盘输入返回值的类型是字符串，要用int、float等进行强制类型转换。
# 因为，input()函数是默认输入字符串，不管你输入的数字还是其他什么。。。
#2.75是浮点数，不能用int(),而要用float（）
Enter_Hours= input("Enter Hours:")
Enter_Rate=input("Enter Rate:")
print(f"Pay: {float(Enter_Hours)*float(Enter_Rate)}")
print ("Pay:", float(Enter_Hours)*float(Enter_Rate))

#Better:
Pay = float(Enter_Hours)*float(Enter_Rate)
print ("Pay:", Pay)