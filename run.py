# first project

print("\033c")

print('''
# CALCULATOR 📟
1.Add      【➕】
2.Subtract 【➖】
3.Multiply 【✖️ 】
4.Divide   【➗】

                           ✨ Created by Aayush Singh ✨
                                     from nepal



''')
x=int(input("Choose number 🔢 : "))
#Add script
if (x==1):
        num1=float(input("\n\nEnter first number : "))
        num2=float(input("Enter second number : "))
        print("Result : ",num1+num2)

#Subtract script
elif (x==2):
        num1=float(input("\n\nEnter first number : "))
        num2=float(input("Enter second number : "))
        print("Result : ",num1-num2)

#Multiply script
elif (x==3):
        num1=float(input("\n\nEnter first number : "))
        num2=float(input("Enter second number : "))
        print("Result : ",num1*num2)


#Divide script
elif (x==4):
        num1=float(input("\n\nEnter first number : "))
        num2=float(input("Enter second number : "))
        if (num2==0):
                print("⚠️ERROR⚠️ : cannot divide by zero !")
        else:
                print("Result : ",num1/num2)
else:
                print("⚠️ Invalid choice! Please select 1 to 4 only.")


