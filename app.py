#ARIEL AMERIGO JOE BANUA
#TP063209


def Userlogin():
    print ("BANK BANK".center(70,"="))
    trials = 3
    while trials <= 3:
        if trials == 0:
            return "null"
        user_id = input("enter your id :")
        user_pass = input("enter your password :")
        with open("users.txt","r") as fh:
            for rec in fh:
                rec_split = rec.strip().split(";")
                if user_id == rec_split[1] and user_pass == rec_split[2]:
                    return rec_split
        trials = trials - 1
        print ("wrong ID or password,", trials, "trials left")
            
def Datetime():
    import datetime as dt
    datetime_now = dt.datetime.now()
    time = datetime_now.strftime("%d/%m/%Y")
    return time

def GenerateID(acctype):
    with open ("ID.txt","r") as fh:
        IDscan = fh.readline()
        IDscan_list = IDscan.split(";")
        if (acctype == "admin"):
            oldid = IDscan_list[0]
            nextid = int(oldid[5:])+ 1
            if len (str(nextid))==1:
                newid = "ADMIN00"+str(nextid)
            elif len (str(nextid))==2:
                newid = "ADMIN0"+str(nextid)
            elif len (str(nextid))==3:
                newid = "ADMIN"+str(nextid)
            with open ("ID.txt","w") as fh:
                IDscan_list[0] = newid
                IDscan = ";".join(IDscan_list)
                fh.write(IDscan)
            return newid
        elif (acctype == "customer"):
            nextid = int(IDscan_list[1])+ 1
            if len (str(nextid))==1:
                newid = "0000000"+str(nextid)
            elif len (str(nextid))==2:
                newid = "000000"+str(nextid)
            elif len (str(nextid))==3:
                newid = "00000"+str(nextid)
            elif len (str(nextid))==4:
                newid = "0000"+str(nextid)
            elif len (str(nextid))==5:
                newid = "000"+str(nextid)
            elif len (str(nextid))==6:
                newid = "00"+str(nextid)
            elif len (str(nextid))==7:
                newid = "0"+str(nextid)
            elif len (str(nextid))==8:
                newid = str(nextid)
            with open ("ID.txt","w") as fh:
                IDscan_list[1] = newid
                IDscan = ";".join(IDscan_list)
                fh.write(IDscan)
            return newid

def Changepassword(userinfo):
    allrec = []
    newpass = input("enter the new password: ")
    while len(newpass)>8:
        print("a password can not exceed 8 characters")
        newpass = input("enter the new password: ")
    with open ("users.txt","r") as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            allrec.append(rec_split)
    ind = -1
    recnum = len(allrec)
    for cnt in range (0,recnum):
        if allrec[cnt][1] == userinfo[1]:
            ind = cnt
            break
    print("would you like to change your password to ", newpass,"?")
    confirm = input("(y/n) :")
    while confirm != "y" and confirm !="n":
        confirm = input("please enter (y/n) :") 
    if confirm == "n":
        ind = -1
    if ind >=0 :
        allrec[ind][2] = newpass
        with open ("users.txt","w") as fh:
            for rec in range(0,recnum):
                new = ";".join(allrec[rec])+"\n"
                fh.write(new)
        print("your password has been changed")
    else:
        print("failed changing password")

def Modifyacc(acctype):
    ID = input("enter the user's ID :")
    if acctype == "customer":
        while ID == "00000000" or ID[:5] == "ADMIN":
            print("admin account can change customer accounts only")
            ID = input("enter the user's ID :")
    elif acctype == "admin":
        while ID[:5] != "ADMIN":
            print("super account can change admin accounts only")
            ID = input("enter the user's ID :")
    allrec = []
    with open ("users.txt","r")as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            allrec.append(rec_split)
    ind = -1
    recnum = len(allrec)
    for cnt in range(0, recnum):
        if ID == allrec[cnt][1]:
            ind = cnt
            break
    if ind >= 0:
        print("1. address")
        print("2. phone number")
        option = input("which data would you like to modify? :")
        if option == "1":
            address = input("please enter the new address :")
            while len(address) > 40:
                print ("user's address can not exceed 40 characters. Please abbreviate")
                address = input ("please enter the new address :")
            print("would you like to change the address to ", address,"?")
            confirm = input("(y/n) :")
            while confirm != "y" and confirm !="n":
                confirm = input("please enter (y/n) :") 
            if confirm == "y":
                allrec[ind][4] = address
                with open ("users.txt","w") as fh:
                    for rec in range (0,recnum):
                        new = ";".join(allrec[rec])+"\n"
                        fh.write(new)
                    print("the data has been updated")
        elif option == "2":
            phonenum = input("please enter the new phone number :")
            while len(phonenum) < 12 or len(phonenum) > 15 or phonenum[:3] != "+60":
                print ("please enter in the right format")
                phonenum = input ("please enter the new phone number (+60**********) :")
            print("would you like to change the phone number to ", phonenum,"?")
            confirm = input("(y/n) :")
            while confirm != "y" and confirm !="n":
                confirm = input("please enter (y/n) :") 
            if confirm == "y":
                allrec[ind][5] = phonenum
                with open ("users.txt","w") as fh:
                    for rec in range (0,recnum):
                        new = ";".join(allrec[rec])+"\n"
                        fh.write(new)
                    print("the data has been updated")
    else:
        print("user not found")

def Transactions(userinfo,amount,action,person):
    import datetime as dt
    datetime_now = dt.datetime.now()
    time = datetime_now.strftime("%d/%m/%Y, %H:%M:%S")
    if action == "transfer to":
        with open ("transactions.txt","a") as fh:
            fh.write("\n"+time+";"+userinfo[0]+";"+userinfo[1]+";"+userinfo[3]+";"+"transfer to "+person+";"+str(amount)+";"+userinfo[4])
    elif action == "transfer from":
        with open ("transactions.txt","a") as fh:
            fh.write("\n"+time+";"+userinfo[0]+";"+userinfo[1]+";"+userinfo[3]+";"+"transfer from "+person+";"+str(amount)+";"+userinfo[4])
    else:
        with open ("transactions.txt","a") as fh:
            fh.write("\n"+time+";"+userinfo[0]+";"+userinfo[1]+";"+userinfo[3]+";"+action+";"+str(amount)+";"+userinfo[4])
        
def Reportstatement(userinfo):
    import datetime
    while True:
        try:
            startdate, startmonth, startyear = [int(x) for x in input("enter the start date(DD/MM/YYYY) :").split('/')]
            startperiod = datetime.datetime(startyear, startmonth, startdate)
            enddate, endmonth, endyear = [int(x) for x in input("enter the end date(DD/MM/YYYY) :").split('/')]
            endperiod = datetime.datetime(endyear, endmonth, enddate)
            break
        except:
            print("please enter in the right format (DD/MM/YYYY)")
    print ("\n")
    print ("STATEMENT OF ACCOUNT REPORT".center(158,"*"))
    print ("-"*158)
    print ("|","time".center(20), "|","name".center(30), "|","id".center(8), "|","customer type".center(15), "|","action".center(43),"|","amount".center(10),
           "|","total".center(10),"|")
    print ("-"*158)
    cnt = 0
    with open("transactions.txt","r") as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            rectime = datetime.datetime.strptime(rec_split[0][:10], "%d/%m/%Y")
            if userinfo[1] == (rec_split)[2] and rectime >= startperiod and rectime <= endperiod:
                print ("|",rec_split[0].ljust(20),"|", rec_split[1].ljust(30),"|",rec_split[2].center(8),
                       "|",rec_split[3].ljust(15),"|",rec_split[4].ljust(43),"|",rec_split[5].ljust(10),"|",rec_split[6].ljust(10),"|")
                print ("-"*158)
                cnt = cnt + 1
                if cnt %25 == 0:
                    confirm = input("press any other key to continue. press q to exit :")
                    if confirm == "q":
                        break
                    else:
                        print("\n")
        if cnt == 0:
            print("you have not done any transactions in this period")

def Viewbalance(userinfo):
    allrec = []
    with open ("customersavings.txt","r") as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            allrec.append(rec_split)
    ind = -1
    recnum = len(allrec)
    for cnt in range (0,recnum):
        if allrec[cnt][1] == userinfo[1]:
            ind = cnt
            break
    if ind >= 0:
        print ("-"*10,"your account type is",":".rjust(1), allrec[ind][3])
        print ("-"*10,"your balance is",": RM".rjust(9), allrec[ind][4])
            
def Depositmoney(userinfo):
    while True:
        try:
            deposit = int(input("enter the amount to deposit: "))
            break
        except:
            print("please enter in numbers")
    allrec = []
    with open ("customersavings.txt","r")as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            allrec.append(rec_split)
    ind = -1
    recnum = len(allrec)
    for cnt in range(0, recnum):
        if userinfo[1] == allrec[cnt][1]:
            ind = cnt
            break
    print("would you like to deposit RM", deposit,"?")
    confirm = input("y/n) :")
    while confirm != "y" and confirm !="n":
        confirm = input("please enter (y/n) :")
    if confirm == "n":
        ind = -1
    if ind >=0 :
        newbalance = int(allrec[ind][4])+deposit
        allrec[ind][4] = str(newbalance)
        Transactions(allrec[ind],deposit,"deposit","x")
        with open ("customersavings.txt","w") as fh:
            for rec in range(0,recnum):
                new = ";".join(allrec[rec])+"\n"
                fh.write(new)
        print("RM", deposit, "has been deposit")
    else :
        print("deposit failed")

def Withdrawmoney(userinfo):
    while True:
        try:
            withdraw = int(input("enter the amount to withdraw: "))
            break
        except:
            print("please enter in numbers")
    allrec = []
    with open ("customersavings.txt","r")as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            allrec.append(rec_split)
    ind = -1
    recnum = len(allrec)
    for cnt in range(0, recnum):
        if userinfo[1] == allrec[cnt][1]:
            ind = cnt
            break
    print("would you like to withdraw RM", withdraw,"?")
    confirm = input("y/n) :")
    while confirm != "y" and confirm !="n":
        confirm = input("please enter (y/n) :")
    if confirm == "n":
        ind = -1
    if ind >=0 :
        if allrec[ind][3] == "savings":
            if int(allrec[ind][4])- withdraw >= 100:
                newbalance = int(allrec[ind][4])-withdraw
                allrec[ind][4] = str(newbalance)
                Transactions(allrec[ind],withdraw,"withdraw","x")
                print("RM", withdraw, "has been withdrawn")
            else:
                print("your minimum balance is not RM 100")
                print ("your balance is: RM", allrec[ind][4])
        elif allrec[ind][3] == "current":
            if int(allrec[ind][4])- withdraw >= 500:
                newbalance = int(allrec[ind][4])-withdraw
                allrec[ind][4] = str(newbalance)
                Transactions(allrec[ind],withdraw,"withdraw","x")
                print("RM", withdraw, "has been withdrawn")
            else :
                print("your minimum balance is not RM 500")
                print ("your balance is: RM", allrec[ind][4])
        with open ("customersavings.txt","w") as fh:
            for rec in range(0,recnum):
                new = ";".join(allrec[rec])+"\n"
                fh.write(new)
    else:
        print ("withdraw failed")

def Transfermoney(userinfo):
    destination = input("enter the destination's ID: ")
    while destination == userinfo[1]:
        print("you can not enter your own ID")
        destination = input("enter the destination's ID: ")
    checker = False
    with open("customersavings.txt","r")as fh:
        for rec in fh:
            rec_split = rec.strip().split(";")
            if rec_split[1] == destination:
                checker = True
                break
        if checker == False:
            print("Destination ID not found")
    if checker == True:
        while True:
            try:
                transfer = int(input("enter the amount to transfer: "))
                break
            except:
                print("please enter in numbers")
        allrec = []
        with open ("customersavings.txt","r")as fh:
            for rec in fh:
                rec_split = rec.strip().split(";")
                allrec.append(rec_split)
        ind1 = -1
        ind2 = -1
        recnum = len(allrec)
        for cnt in range(0, recnum):
            if userinfo[1] == allrec[cnt][1]:
                ind1 = cnt
            elif destination == allrec[cnt][1]:
                ind2 = cnt
        print("would you like to transfer RM", transfer,"to", allrec[ind2][0],"?")
        confirm = input("y/n) :")
        while confirm != "y" and confirm !="n":
            confirm = input("please enter (y/n) :")
        if confirm == "n":
            ind1 = -1
        if ind1 >=0 :
            if allrec[ind1][3] == "savings":
                if int(allrec[ind1][4])- transfer >= 100:
                    newbalance = int(allrec[ind1][4])-transfer
                    allrec[ind1][4] = str(newbalance)
                    Transactions(allrec[ind1],transfer,"transfer to",allrec[ind2][0])
                    if ind2 >= 0:
                        newbalance = int(allrec[ind2][4])+transfer
                        allrec[ind2][4] = str(newbalance)
                        Transactions(allrec[ind2],transfer,"transfer from",allrec[ind1][0])
                        print("RM", transfer, "has been transferred to",allrec[ind2][0])
                else:
                    print("your minimum balance is not RM 100")
                    print ("your balance is: RM", allrec[ind1][4])
            elif allrec[ind1][3] == "current":
                if int(allrec[ind1][4])- transfer >= 500:
                    newbalance = int(allrec[ind1][4])-transfer
                    allrec[ind1][4] = str(newbalance)
                    Transactions(allrec[ind1],transfer,"transfer to",allrec[ind2][0])
                    if ind2 >= 0:
                        newbalance = int(allrec[ind2][4])+transfer
                        allrec[ind2][4] = str(newbalance)
                        Transactions(allrec[ind2],transfer,"transfer from",allrec[ind1][0])
                        print("RM", transfer, "has been transferred to",allrec[ind2][0])
                else :
                    print("your minimum balance is not RM 500")
                    print ("your balance is: RM", allrec[ind1][4])
            with open ("customersavings.txt","w") as fh:
                for rec in range(0,recnum):
                    new = ";".join(allrec[rec])+"\n"
                    fh.write(new)   
        else:
            print ("transfer failed")
def Createacc(acctype):
    if acctype == "admin":
        newID = GenerateID("admin")
        username = input("enter the user's name :")
        while len(username) > 30:
            print("user's name can not exceed 30 characters. Please abbreviate")
            username = input("enter the user's name:")
        defaultpass = newID
        address = input("enter the user's address :")
        while len(address) > 40:
            print ("user's address can not exceed 40 characters. Please abbreviate")
            address = input ("please enter the user's address :")
        phonenum = input ("enter user's phone number (+60**********) :")
        while len(phonenum) < 12 or len(phonenum) > 15 or phonenum[:3] != "+60":
            print ("please enter in the right format")
            phonenum = input ("enter the user's phone number (+60**********) :")
        with open ("users.txt","a")as fh:
           fh.write(username+";"+newID+";"+defaultpass+";"+"admin"+";"+address+";"+phonenum+"\n")
        print ("an admin account has been made")
    elif acctype == "customer":
        newID = GenerateID("customer")
        username = input("enter the user's name :")
        while len(username) > 30:
            print("user's name can not exceed 30 characters. Please abbreviate")
            username = input("enter the user's name:")
        defaultpass = newID
        address = input("enter the users's address :")
        while len(address) > 40:
            print ("user's address can not exceed 40 characters. Please abbreviate")
            address = input ("please enter the new address :")
        phonenum = input ("enter the user's phone number (+60**********) :")
        while len(phonenum) < 12 or len(phonenum) > 15 or phonenum[:3] != "+60":
            print ("please enter in the right format")
            phonenum = input ("enter the user's phone number (+60**********) :")
        custype = input("enter the type of account: ")
        if custype != "savings" and custype != "current":
            while custype  != "savings" and custype !=  "current":
                print("please enter either savings or current account")
                custype = input("enter the type of account: ")        
        while True:
            try:
                balance = int(input("enter the starting balance: "))
                break
            except:
                print ("please enter in numbers")
        if custype == "savings":
            while balance < 100:
                print("savings account must have a balance of at least 100 RM")
                while True:
                    try:
                        balance = int(input("enter the starting balance: "))
                        break
                    except:
                        print ("please enter in numbers")
        elif custype == "current":
            while balance < 500:
                print("current account must have a balance of at least 500 RM")
                while True:
                    try:
                        balance = int(input("enter the starting balance: "))
                        break
                    except:
                        print ("please enter in numbers")
        with open ("users.txt","a")as fh:
            fh.write(username+";"+newID+";"+defaultpass+";"+"customer"+";"+address+";"+phonenum+"\n")
        with open ("customersavings.txt","a") as fh:
            fh.write (username+";"+newID+";"+"customer"+";"+custype+";"+str(balance)+"\n")
        print("a",custype,"customer account has been made")
        
def Viewusers():
    with open ("users.txt","r") as fh:
        print ("\n")
        print ("USER LIST".center(128,"*"))
        print ("-"*128)
        print ("|","name".center(30), "|","id".center(8), "|","password".center(8), "|","type".center(8), "|","address".center(40), "|","phone number".center(15),"|")
        print ("-"*128)
        cnt = 0
        for rec in fh:
            rec_split = rec.strip().split(";")
            print ("|",rec_split[0].ljust(30),"|", rec_split[1].center(8),"|",rec_split[2].ljust(8),
                   "|",rec_split[3].ljust(8),"|",rec_split[4].ljust(40),"|",rec_split[5].ljust(15),"|")
            print ("-"*128)
            cnt = cnt + 1
            if cnt %25 == 0:
                confirm = input("press any other key to continue. press q to exit :")
                if confirm == "q":
                    break
                else:
                    print("\n")

def Viewcustomers():
    with open ("customersavings.txt","r") as fh:
        print ("\n")
        print ("CUSTOMER LIST".center(90,"*"))
        print ("-"*90)
        print ("|","name".center(30), "|","id".center(8), "|","type".center(8), "|","customer type".center(13), "|","balance".center(15), "|")
        print ("-"*90)
        cnt = 0
        for rec in fh:
            rec_split = rec.strip().split(";")
            print ("|",rec_split[0].ljust(30),"|", rec_split[1].center(8),"|",rec_split[2].center(8),
                   "|",rec_split[3].center(13),"|",rec_split[4].ljust(15),"|")
            print ("-"*90)
            cnt = cnt + 1
            if cnt %25 == 0:
                confirm = input("press any other key to continue. press q to exit :")
                if confirm == "q":
                    break
                else:
                    print("\n")

def Viewprofile(userinfo):
    print("-"*10,"Name ",":".rjust(11), userinfo[0])
    print("-"*10,"ID ",":".rjust(13), userinfo[1])
    print("-"*10,"Password ",":".rjust(7), userinfo[2])
    print("-"*10,"Occupation ",":".rjust(5), userinfo[3])
    print("-"*10,"Address ",":".rjust(8), userinfo[4])
    print("-"*10,"Phone number ",":".rjust(3), userinfo[5])

def Supermenu(userinfo):
    while True:
        time = Datetime()
        print("\n")
        print ("BANK BANK".center(70,"="))
        print("welcome", userinfo[0])
        print (time)
        print("1. create admin accounts")
        print("2. view users")
        print("3. modify admin account")
        print("4. log out")
        try:
            option=int(input("enter your option :"))
            if (option == 1):
                Createacc("admin")
            elif (option == 2):
                Viewusers()
            elif option == 3:
                Modifyacc("admin")
            elif (option == 4):
                break
            else:
                print("please enter from the above options")
        except:
            print("please enter an option in number")

def Adminmenu(userinfo):
    while (True):
        time = Datetime()
        print("\n")
        print ("BANK BANK".center(70,"="))
        print("welcome", userinfo[0])
        print (time)
        print("1. create customer accounts")
        print("2. view profile")
        print("3. view customers")
        print("4. change password")
        print("5. modify customer account")
        print("6. create account report")
        print("7. log out")
        try:
            option = int(input("please enter from the above option:"))
            if (option == 1):
                Createacc("customer")
            elif (option == 2):
                Viewprofile(userinfo)
            elif (option == 3):
                Viewcustomers()
            elif (option == 4):
                Changepassword(userinfo)
            elif option == 5:
                Modifyacc("customer")
            elif (option == 6):
                ID = input("enter the customeer's ID :")
                allrec = []
                with open ("customersavings.txt","r")as fh:
                    for rec in fh:
                        rec_split = rec.strip().split(";")
                        allrec.append(rec_split)
                ind = -1
                recnum = len(allrec)
                for cnt in range(0, recnum):
                    if ID == allrec[cnt][1]:
                        ind = cnt
                        break
                if ind >= 0:
                    Reportstatement(allrec[ind])
                else:
                    print("customer not found")
            elif (option == 7):
                break
            else:
                print("please enter from the above options")
        except:
            print("please enter in numbers")

def Customermenu(userinfo):
    while (True):
        time = Datetime()
        print("\n")
        print ("BANK BANK".center(70,"="))
        print("welcome", userinfo[0])
        print (time)
        print("1. deposit money")
        print("2. withdraw money")
        print("3. transfer money")
        print("4. view balance")
        print("5. view profile")
        print("6. change password")
        print("7. create account report")
        print("8. log out")
        try:
            option = int(input("enter your option:"))
            if (option == 1):
                Depositmoney(userinfo)
            elif (option == 2):
                Withdrawmoney(userinfo)
            elif (option == 3):
                Transfermoney(userinfo)
            elif (option == 4):
                Viewbalance(userinfo)
            elif (option == 5):
                Viewprofile(userinfo)
            elif (option == 6):
                Changepassword(userinfo)
            elif (option == 7):
                Reportstatement(userinfo)
            elif (option == 8):
                break
            else:
                print("please enter from the above options")
        except:
            print("please enter in numbers")      

#main logic
while True:
    checkval = Userlogin()
    if (checkval == "null"):
        print ("login failed")
        break
    elif (checkval[3] == "super"):
        Supermenu(checkval)
    elif (checkval[3] == "admin"):
        Adminmenu(checkval)
    elif (checkval[3] == "customer"):
        Customermenu(checkval)
    ans = input("press any other key to continue. press q to exit :")
    if (ans == "q"):
        break
