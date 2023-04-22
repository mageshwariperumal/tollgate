c1=input("customer1 : TN 12 W 1706 : MICK : Make : Maruti") #press enter till the end of the customer
c2=input("customer2 : TN 13 W 1707 : JOHN : Make : Honda")
c3=input("customer3 : TN 14 W 1708 : PAVI : Make : Tesla")
c4=input("customer4 : TN 15 W 1709 : MAGGIE : Make : Lambrogane")
c5=input("customer5 : TN 16 W 1720 : YUVA : Make : BMW")
print("ide=11,c1")
print("ide=12,c2")
print("ide=13,c3")
print("ide=14,c4")
print("ide=15,c5")
w=int(input("Enter 1 to continue or 0 to exit :"))
while(w==1):
    ide=int(input("enter the id choice:"))
    a=input("enter the choice:")
    if(a=="c1"):
        print("******************************************************")
        amount=int(input("Enter the amount"))
        if(ide==11):
            print(amount)
            if(amount>550):
                amount=amount-30
                print(amount)
            elif(amount<550):
                print("insufficent balance")
                b=input("want to add amount to your account y/n:")
                if(b=="y"):
                    c=int(input("enter the amount you want to add:"))
                    amount=amount+c
                    print("updated amount=",amount)
                else:
                    print("insufficent balance")
            else:
                print("recharge as soon as possible")
    elif(a=="c2"):
        print("******************************************************")
        amount=int(input("Enter the amount"))
        if(ide==12):
            print(amount)
            if(amount>550):
                amount=amount-30
                print(amount)
            elif(amount<550):
                print("insufficent balance")
                b=input("want to add amount to your account y/n:")
                if(b=="y"):
                    c=int(input("enter the amount you want to add:"))
                    amount=amount+c
                    print("updated amount=",amount)
                else:
                    print("insufficent balance")
            else:
                print("recharge as soon as possible")
    elif(a=="c3"):
        print("******************************************************")
        amount=int(input("Enter the amount"))
        if(ide==13):
            print(amount)
            if(amount>550):
                amount=amount-30
                print(amount)
            elif(amount<550):
                print("insufficent balance")
                b=input("want to add amount to your account y/n:")
                if(b=="y"):
                    c=int(input("enter the amount you want to add:"))
                    amount=amount+c
                    print("updated amount=",amount)
                else:
                    print("insufficent balance")
            else:
                print("recharge as soon as possible")
    elif(a=="c4"):
        print("******************************************************")
        amount=int(input("Enter the amount"))
        if(ide==14):
            print(amount)
            if(amount>550):
                amount=amount-30
                print(amount)
            elif(amount<550):
                print("insufficent balance")
                b=input("want to add amount to your account y/n:")
                if(b=="y"):
                    c=int(input("enter the amount you want to add:"))
                    amount=amount+c
                    print("updated amount=",amount)
                else:
                    print("insufficent balance")
            else:
                print("recharge as soon as possible")
    else:
        print("******************************************************")
        amount=int(input("Enter the amount"))
        if(ide==15):
            print(amount)
            if(amount>550):
                amount=amount-30
                print(amount)
            elif(amount<550):
                print("insufficent balance")
                b=input("want to add amount to your account y/n:")
                if(b=="y"):
                    c=int(input("enter the amount you want to add:"))
                    amount=amount+c
                    print("updated amount=",amount)
                else:
                    print("insufficent balance")
            else:
                print("recharge as soon as possible")
    wb=int(input("enter 0 to exit 2 to tollgate 1 to continue:"))
    if(wb==1):
        continue
    elif(wb==2):
        if(a=="c1"):
            print("TN 12 W 1706 : MICK : Make : Maruti")
            print(amount)
        elif(a=="c2"):
            print("TN 13 W 1707 : JOHN : Make : Honda")
            print(amount)
        elif(a=="c3"):
            print("TN 14 W 1708 : PAVI : Make : Tesla")
            print(amount)
        elif(a=="c4"):
            print("TN 15 W 1709 : MAGGIE : Make : Lambrogane")
            print(amount)
        elif(a=="c5"):
            print("TN 16 W 1720 : YUVA : Make : BMW")
            print(amount)
        else:
            print(" invalid choice")
    else:
        break
