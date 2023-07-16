# Users data +
# Password checking +
# Maximum 3 attempts

# View Current Balance +
# View Steps +
# Cash In +
# Cash Out +
# Give Check +


mArr1 = 0
mArr2 = 0
mArr3 = 0



notificationArr1 = 0
notificationArr2 = 0
notificationArr3 = 0
IdNotification = 0



User1CheckPoint = 0
User2CheckPoint = 0
User3CheckPoint = 0

User1Arr = ["579170524", "52301", 569, "+1467224674"]
User1View = "Bay` car Honda Pilot 36300 $, Jins 50$, laptop` MSI Computer GF63 600$ "
User1IndexArr = 2

User2Arr = ["089345679", "09168", 1000, "+15468753678"]
User2View = "Bay` Yacht 2295000 $, La Ferrari 2.000.000 $, airplane T7A $6,395.00"
User2IndexArr = 2


User3Arr = ["1845682159", "753951", 843, "+1235689057"]
User3View = "Bay : Business PC  - 50.000.000$"
User3IndexArr = 2

i = 0

from datetime import datetime

current_datetime = datetime.now()



def DefnotificationArr1():
    print("                                                ATM")
    print(f"                       You received money from - id : {IdNotification[0]} and {IdMoney}$ ")
    print()


def DefnotificationArr2():
    print("                                                ATM")
    print(f"                       You received money from - id : {IdNotification[0]} and {IdMoney}$ ")
    print()


def DefnotificationArr3():
    print("                                                ATM")
    print(f"                       You received money from - id : {IdNotification[0]} and {IdMoney}$ ")
    print()






def GiveCheckCashOut(user_arr):
    print("                                 ATM Check ")
    print(f"                        Time {current_datetime}")
    print("                       You took money from this card")
    print(f"                     We will send a message {user_arr[3]}")
    print("                           Thanks for understanding")
    print()
    print()

def GiveChackCashIn(user_arr):
    print("                                         Check ATM")
    print(f"                        Time {current_datetime}")
    print(f"                      you took the amount {user_arr[2]} from the bank")
    print("                          I will send a message to your phone")
    print("                                thanks for understanding")
    print()
    print()




IdMoney = 0
def CashOut(user_arr):
    while True:
        CashOut = input("Your Number: ")

        CashOutPinus = int(user_arr[2]) - int(CashOut)
        if CashOutPinus >= 0:
            user_arr[2] = CashOutPinus
            print(user_arr[2])
            break
        else:
            print("You can't withdraw that amount. Insufficient funds.")
            print("^-^-" * 20)
            YesNoCashOut = input("Do you want to continue? (Yes/No): ")
            if YesNoCashOut.lower() == "no":
                print("Operation canceled.")
                break

z = 0
while i <= 3:
    if z == 0:
        z += 1
        User1CheckPoint += 1

    User = input("Enter Your User: ")
    Password = input("Enter Your Password: ")

    if User == User1Arr[0] and Password == User1Arr[1]:
        print("You are logged in")
        print(f"Your balance: {User1Arr[2]} $")



        while True:

            if(notificationArr1 == 1 and mArr1 == 0):
                mArr1+=1
                DefnotificationArr1()
            i = 0
            help = input("How can I help you? (Type 'help' for assistance): ")

            #------------------------------------------------------------------------------GIVE MONEY #1
            if(help. lower() == "give money"):
                IdMoney = int(input("Money you want to send to a friend or man : "))
                User1ArrIdMoneyMinus  = User1Arr[2] - IdMoney
                if(User1ArrIdMoneyMinus >= 0):
                    Id = input("Id : ")
                    if(Id == User2Arr[0]):
                        User1Arr[2] = User1Arr[2] - IdMoney
                        User2Arr[2] =  User2Arr[2] + IdMoney
                        print(f"Everyone sent your balance  - {User1Arr[2]} $")
                        notificationArr2 += 1
                        IdNotification = User2Arr

                    if (Id == User3Arr[0]):
                        IdMoney = int(input("Money you want to send to a friend or man : "))
                        User1Arr[2] = User1Arr[2] - IdMoney
                        User3Arr[2] = User3Arr[2] + IdMoney
                        print(f"Everyone sent your balance  - {User1Arr[2]} $")
                        notificationArr3 += 1
                        IdNotification = User3Arr




                if(User1ArrIdMoneyMinus < 0):
                    print("_____"*20)
                    print("insufficient funds")
                    print("_____"*20)


            #------------------------------------------------------------------------------GIVE MONEY

            if help.lower() == "help":
                print("Want to see your transactions? - Steps")
                print("Do you want to increase your balance? - Cash In")
                print("Give money to the bank - Cash Out")
                print("Exit - To exit the application")

            elif help.lower() == "steps":
                print(User1View)

            elif help.lower() == "cash in":
                CashPlus = input("Enter the amount to deposit: ")
                User1Arr[2] = str(int(User1Arr[2]) + int(CashPlus))

                CheckYesNoCashIn = input("give me a check? Yes/No: ")
                if CheckYesNoCashIn.lower() in ["yes", "y"]:
                    GiveChackCashIn(User1Arr)

            elif help.lower() == "cash out":
                CashOut(User1Arr)
                CheckYesNoCashOut = input("give me a check? Yes/No: ")
                if CheckYesNoCashOut.lower() in ["yes", "y"]:
                    GiveCheckCashOut(User1Arr)
                    User1CheckPoint += 1

            elif help.lower() == "exit":
                break

            elif help.lower() == "ball":
                print(f"Your balance: {User1Arr[2]} $")

    elif User == User2Arr[0] and Password == User2Arr[1]:


        while True:
            if (notificationArr2 == 1 and mArr2 == 0):
                mArr2+=1
                DefnotificationArr2()
            i = 0
            help = input("How can I help you? (Type 'help' for assistance): ")

            # ------------------------------------------------------------------------------GIVE MONEY #2
            if (help.lower() == "give money"):
                User2ArrIdMoneyMinus =  User1Arr[2] - IdMoney
                if (User2ArrIdMoneyMinus >= 0):
                    Id = input("Id : ")
                    if (Id == User1Arr[0]):
                        IdMoney = int(input("Money you want to send to a friend or man : "))
                        User2Arr[2] = User2Arr[2] - IdMoney
                        User1Arr[2] = User1Arr[2] + IdMoney
                        print(f"Everyone sent your balance  - {User1Arr[2]} $")
                        notificationArr1 +=1
                        IdNotification = User1Arr

                    if (Id == User3Arr[0]):
                        IdMoney = int(input("Money you want to send to a friend or man : "))

                        User2Arr[2] = User2Arr[2] - IdMoney
                        User3Arr[2] = User3Arr[2] + IdMoney
                        print(f"Everyone sent your balance  - {User1Arr[2]} $")
                        notificationArr2 +=1
                        IdNotification = User3Arr


                if(User2ArrIdMoneyMinus < 0):
                    print("_____" * 20)
                    print("insufficient funds")
                    print("_____" * 20)
                    # ------------------------------------------------------------------------------GIVE MONEY



            if help.lower() == "help":
                print("Want to see your transactions? - Steps")
                print("Do you want to increase your balance? - Cash In")
                print("Give money to the bank - Cash Out")
                print("Exit - To exit the application")

            elif help.lower() == "steps":
                print(User2View)

            elif help.lower() == "cash in":
                CashPlus = input("Enter the amount to deposit: ")
                User2Arr[2] = str(int(User2Arr[2]) + int(CashPlus))

                CheckYesNoCashIn = input("give me a check? Yes/No: ")
                if CheckYesNoCashIn.lower() in ["yes", "y"]:
                    GiveChackCashIn(User2Arr)

            elif help.lower() == "cash out":
                CashOut(User2Arr)
                CheckYesNoCashOut = input("give me a check? Yes/No: ")
                if CheckYesNoCashOut.lower() in ["yes", "y"]:
                    GiveCheckCashOut(User2Arr)
                    User2CheckPoint += 1

            elif help.lower() == "exit":
                break

            elif help.lower() == "ball":
                print(f"Your balance: {User2Arr[2]} $")

    elif User == User3Arr[0] and Password == User3Arr[1]:




        while True:
            if (notificationArr3 == 1 and mArr3 == 0):
                mArr3+=1
                DefnotificationArr3()
            i = 0
            help = input("How can I help you? (Type 'help' for assistance): ")

            # ------------------------------------------------------------------------------GIVE MONEY #3
            IdMoney = int(input("Money you want to send to a friend or man : "))
            User3ArrIdMoneyMinus = User3Arr[2] - IdMoney

            if (help.lower() == "give money"):
                if(User3ArrIdMoneyMinus >= 0):
                    Id = input("Id : ")
                    if (Id == User2Arr[0]):
                        User3Arr[2] = User3Arr[2] - IdMoney
                        User2Arr[2] = User2Arr[2] + IdMoney
                        notificationArr2 += 1
                        IdNotification = User2Arr
                        print(f"Everyone sent your balance  - {User3Arr[2]} $")
                    if (Id == User1Arr[0]):
                        IdMoney = int(input("Money you want to send to a friend or man : "))
                        User3Arr[2] = User3Arr[2] - IdMoney
                        User1Arr[2] = User1Arr[2] + IdMoney
                        print(f"Everyone sent your balance  - {User3Arr[2]} $")
                        IdNotification = User2Arr
                        notificationArr1+=1

                if(User3ArrIdMoneyMinus < 0):
                    print("_____" * 20)
                    print("insufficient funds")
                    print("_____" * 20)
                # ------------------------------------------------------------------------------GIVE MONEY
            if help.lower() == "help":
                print("Want to see your transactions? - Steps")
                print("Do you want to increase your balance? - Cash In")
                print("Give money to the bank - Cash Out")
                print("Exit - To exit the application")

            elif help.lower() == "steps":
                print(User3View)

            elif help.lower() == "cash in":
                CashPlus = input("Enter the amount to deposit: ")
                User3Arr[2] = str(int(User3Arr[2]) + int(CashPlus))

                CheckYesNoCashIn = input("give me a check? Yes/No: ")
                if CheckYesNoCashIn.lower() in ["yes", "y"]:
                    GiveChackCashIn(User3Arr)

            elif help.lower() == "cash out":
                CashOut(User3Arr)
                CheckYesNoCashOut = input("give me a check? Yes/No: ")
                if CheckYesNoCashOut.lower() in ["yes", "y"]:
                    GiveCheckCashOut(User3Arr)
                    User3CheckPoint += 1

            elif help.lower() == "exit":
                break

            elif help.lower() == "ball":
                print(f"Your balance: {User3Arr[2]} $")

    else:
        i += 1
        print(f"Your Points: {i}")

        if i >= 3:
            print("Maximum attempts reached. Exiting the application.")
            break
