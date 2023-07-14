import getpass
import string
import os


users=['user1','user2','user3']
pins=['4599','4554','9549']
amounts=['1000','2000','3000']
phone_numbers=['9784566723','9234567890','9876543210']
count=0

while True:
    user=input("Enter the User name:")
    user=user.lower()
    if user in users:
        if user==users[0]:
            n=0
        elif user==users[1]:
            n=1
        else:
            n=2
        break
    else:
        print("INVALID USER")
        
while count<3:

    pin=str(getpass.getpass("PLEASE ENTER THE PIN:"))
    if pin.isdigit():
        if user==users[0]:
            if pin==pins[0]:
                break
            else:
                count+=1
                print("INVALID PIN")
        if user==users[1]:
            if pin==pins[1]:
                break
            else:
                count+=1
                print("INVALID PIN")
        if user==users[2]:
            if pin==pins[2]:
                break
            else:
                count+=1
                print("INVALID PIN")
    else:
        print("PIN CONSISTS OF 4 DIGITS")

if count==3:
    print("3 UNSUCCESSFUL PIN ATTEMPTS,EXITING")
    print("!!! YOUR CARD HAS BEEN BLOCKED !!!")

    exit()
    
print("LOGIN SUCCESSFULLY, CONTINUE")            
print(str.capitalize(users[n]),"welcome to the ATM")
print("-----------ATM SYSTEM----------")

while True:
    
    response=input("\nSELECT FROM FOLLOWING OPTIONS: \nStatement__(s)\t Withdraw__(w)\n Lodgement__(l)\t Change PIN__(p)\n Balance Enquiry(b)\t Change Phone number(n)\n Quit__(q)\n:").lower()
    valid_response=['s','w','l','p','b','n','q']
    response=response.lower()
    if response=='s':
        print(str.capitalize(users[n]),"YOU HAVE",amounts[n],"EURO ON YOUR ACCOUNT\n************************")
    elif response=='w':
        cash_out=int(input("ENTER THE AMOUNT YOU WOULD LIKE TO WITHDRAW:"))

        if cash_out%10 !=0:
            print("\nAMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EURO NOTES")
        elif cash_out>int(amounts[n]):
            print("\nYOU HAVE INSUFFICIENT BALANCE")
        else:
            amounts[n]=amounts[n]-cash_out
            print("YOUR NEW BALANCE IS",amounts[n],"EURO")
    elif response=='l':
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        

        if cash_in%10!=0:
            print("\nAMOUNT YOU WANT TO LODGE MUST TO MATCH 10 EURO NOTES\n")
        else:
            amounts[n]=amounts[n]+cash_in
            print("\nYOUR NEW BALANCE IS",amounts[n],"EURO\n")
    elif response=='p':
        new_pin=str(getpass.getpass("ENTER A NEW PIN:"))
        if new_pin.isdigit() and new_pin!=pins[n] and len(new_pin)==4:
            new__pin=str(getpass.getpass("COFIRM NEW PIN:"))
            if new__pin!=new_pin:
                print("\nPIN MISMATCH\n")
            else:
                pins[n]=new_pin
                print("\nNEW PIN SAVED\n")
        else:
            print("\nPIN CONSISTS OF 4 DIGITS\n AND MUST BE DIFFERENT TO PREVIOUS PIN\n")
    elif response=='b':
        print("\nYOUR CURRENT BALANCE IS\n",amounts[n])
    
    elif response=='n':
        new_num=str(getpass.getpass("ENTER A NEW NUMBER:"))
        if new_num.isdigit() and new_num!=phone_numbers and len(new_num)==10:
            new_numm=str(getpass.getpass("CONFIRM NEW NUMBER:"))
            if new_numm!=new_num:
                print("\nPHONE NUMBER MISMATCH\n")
            else:
                phone_numbers[n]=new_num
                print("\nPHONE NUMBER IS CHANGED\n")
        else:
            print("\nPHONE NUMBER CONSISTS OF 10 digits\n")
    elif response=='q':
        print("------THANK YOU------")
        exit()
    else:
        print("RESPONSE IS INVALID")


                
    
            
                     
            
        
