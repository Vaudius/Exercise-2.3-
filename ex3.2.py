# Wrong example
# Enter_Hours=input("Enter Hours:")
# Enter_Rate=input("Enter Rate:")
# try:
#     FEH=float(Enter_Hours)
# except:
#     FEH=-1
#
#
# try:
#     FER=float(Enter_Hours)
# except:
#     FER=-1
# if float(Enter_Hours)<=40:
#     Pay = float(Enter_Hours) * float(Enter_Rate)
#     print("Pay:", Pay)
# elif:
#     Pay=40*float(Enter_Rate)+(float(Enter_Hours)-40)*1.5*float(Enter_Rate)
#     print("Pay:", Pay)
# else:
#     print("Error,please enter numeric input")

Enter_Hours=input("Enter Hours:")
Enter_Rate=input("Enter Rate:")
try:
    FEH=float(Enter_Hours)
    FER = float(Enter_Hours)
except:
    print("Error,please enter numeric input")

if float(Enter_Hours)<=40:
    Pay = float(Enter_Hours) * float(Enter_Rate)
    print("Pay:", Pay)
else:
    Pay=40*float(Enter_Rate)+(float(Enter_Hours)-40)*1.5*float(Enter_Rate)
    print("Pay:", Pay)
