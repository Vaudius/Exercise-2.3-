Enter_Hours=input("Enter Hours:")
Enter_Rate=input("Enter Rate:")
if float(Enter_Hours)<=40:
    Pay = float(Enter_Hours) * float(Enter_Rate)
else:
    Pay=40*float(Enter_Rate)+(float(Enter_Hours)-40)*1.5*float(Enter_Rate)
print("Pay:", Pay)