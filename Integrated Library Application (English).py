listLibrary =[
    {   'ID':'1A',
        'Name': 'George',
        'Book': 'A Study in Scarlet',
        'Category': 'Mystery',
        'Borrowing Period':3
    },
    {   'ID':'2A',
        'Name': 'Brian',
        'Book': 'Harry  Potter',
        'Category': 'Fantasy',
        'Borrowing Period': 10
    },
    {   'ID':'1B',
        'Name': 'Stephanie',
        'Book': 'The Little Prince',
        'Category': 'Fantasy',
        'Borrowing Period': 7
    },
    {   'ID':'3A',
        'Name': 'Jackson',
        'Book': 'Atomic Habits',
        'Category': 'Psychology',
        'Borrowing Period': 5
    },
    {   'ID':'2B',
        'Name': 'Nicole',
        'Book': 'Me Before You',
        'Category': 'Romance',
        'Borrowing Period': 8
    }
]

def Library():
    while True :
        MenuOption = input('''
        =================================================================================================
                                        WELCOME TO THE LIBRARY
        =================================================================================================

            LIST MENU 
            1. Display Library Data
            2. Add Library Data
            3. Update Library Data
            4. Delete Library Data
            5. Exit Program

            Enter the Number of the Menu to Run : ''')

        if(MenuOption == '1') :
            displaylistLibrary()
        elif(MenuOption == '2') :
            addlistLibrary()
        elif(MenuOption == '3') :
            updatelistLibrary()
        elif(MenuOption == '4') :
            deletelistLibrary()
        elif(MenuOption == '5') :
            print('''
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
                                Thank You for Using the Library Application!
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            ''')
            break
        else:
            print("Sorry, the Menu Option You Entered Does Not Exist")

def alllistLibrary():
    if len(listLibrary)==0:
        print("Sorry, No Data Available")
    else: 
        print('''
        ++++++++++++++++++++++++++++++++ LIBRARY DATA  +++++++++++++++++++++++++++++++++
        ''')
        print("ID \t| NAME \t \t| BOOK \t \t \t| CATEGORY \t| BORROWING PERIOD")
        for i in range(len(listLibrary)) :
            print(f"{listLibrary[i]['ID']} \t| {listLibrary[i]['Name']} \t| {listLibrary[i]['Book']} \t| {listLibrary[i]['Category']} \t| {listLibrary[i]['Borrowing Period']}")

def displaylistLibrary():
    while True:
        print('''
        ==================================================================================== 
                                        LIBRARY DATA LIST
        ====================================================================================  

            1. Display All Library Data
            2. Display Specific Library Data
            3. Return to Main Menu
        ''')
        submenu = int(input("Please Select a Submenu for Library Data Display : "))
        if submenu==1:
            if len(listLibrary)==0:
                print("Sorry, No Data Available")
            else:
                alllistLibrary()
        elif submenu==2:
            if len(listLibrary)==0:
                print("Sorry, No Data Available")
            else:
                inputid = input("Enter the ID of the Data to Display : ")
                result=[]
                for i in range(len(listLibrary)):
                    result.append(listLibrary[i]['ID'])
                if inputid in result:
                    sameindex=result.index(inputid)
                    print("ID \t| NAME \t \t| BOOK \t \t \t| CATEGORY \t| BORROWING PERIOD")
                    print(f"{listLibrary[sameindex]['ID']} \t| {listLibrary[sameindex]['Name']} \t| {listLibrary[sameindex]['Book']} \t| {listLibrary[sameindex]['Category']} \t| {listLibrary[sameindex]['Borrowing Period']}")
                    result=[]
                else:
                    print("Sorry, No Data Matches the Entered ID")
        elif submenu==3:
            break
        else:
            print("Sorry, the Submenu Option You Entered Does Not Exist")

def addlistLibrary():
    while True: 
        print('''
        ============================================================================================ 
                                        ADD LIBRARY LIST
        ============================================================================================ 

            1. Add Library Data
            2. Return to Main Menu
        ''')
        submenu = int(input('Please Select a Submenu to Add Library Data :'))
        if submenu==1:
            newid = input("Enter the ID to be Added : ")
            result=[]
            for i in range(len(listLibrary)):
                result.append(listLibrary[i]['ID'])
            if newid in result:
                print("Sorry, the Data Already Exists")
                result=[]
            else:
                newname = input("Enter Name : ")
                newbook = input("Enter the Borrowed Book Title : ")
                newcategory = input("Enter the Borrowed Book Category : ")
                while True:
                    newperiod = int(input("Enter the Book Borrowing Period (Maximum 14 Days) : "))
                    if newperiod>=14:
                        print("Sorry, the Book Borrowing Period is a Maximum of 14 Days.")
                    else:
                        save=input("Do You Want To Save the Data? (yes/no)")
                        if save.lower()=='yes':
                            listLibrary.append({
                                'ID' : newid,
                                'Name': newname,
                                'Book': newbook,
                                'Category': newcategory,
                                'Borrowing Period': newperiod
                                })
                            print("Data Has Been Saved")
                            alllistLibrary()
                            break
                        elif save.lower()=='no':
                            break        
        elif submenu==2:
            break
        else:
            print("Sorry, the Submenu Option You Entered Does Not Exist")

def updatelistLibrary():
    while True: 
        print('''
        =================================================================================================
                                            UPDATE LIBRARY DATA
        =================================================================================================

            1. Update Library Data
            2. Return to Main Menu
        ''')
        submenu = int(input("Please Select a Submenu to Update Library Data : "))
        if submenu==1:
            inputid = input("Enter the ID of the Data to be Updated : ")
            result=[]
            for i in range(len(listLibrary)):
                result.append(listLibrary[i]['ID'])
            if inputid in result:
                indexupdate=result.index(inputid)
                print("ID \t| NAME \t \t| BOOK \t \t \t| CATEGORY \t| BORROWING PERIOD")
                print(f"{listLibrary[indexupdate]['ID']} \t| {listLibrary[indexupdate]['Name']} \t| {listLibrary[indexupdate]['Book']} \t| {listLibrary[indexupdate]['Category']} \t| {listLibrary[indexupdate]['Borrowing Period']}")
                result=[]
                next=input("Do You Want to Update the Data? (yes/no)")
                if next.lower()=='yes':
                    while True:
                        column=input("Enter the Column Name You Want to Update (Type 'End' to Go Back) : ")
                        if column.lower()=='name':
                            newname=input("Enter New Name : ")
                            other=input("Are You Sure You Want to Change the Data Column? (yes/no)")
                            if other.lower()=='no':
                                continue
                            elif other.lower()=='yes':
                                listLibrary[indexupdate]['Name']=newname
                                alllistLibrary()
                                print("Data Has Been Updated")
                                updatelistLibrary()
                                break
                        elif column.lower()=='book':
                            newbook=input("Enter New Book Title : ")
                            other=input("Are You Sure You Want to Change the Data Column? (yes/no)")
                            if other.lower()=='no':
                                continue
                            elif other.lower()=='yes':
                                listLibrary[indexupdate]['Book']=newbook
                                alllistLibrary()
                                print("Data Has Been Updated")
                                updatelistLibrary()
                                break
                        elif column.lower()=='category':
                            newcategory=input("Enter New Category : ")
                            other=input("Are You Sure You Want to Change the Data Column? (yes/no)")
                            if other.lower()=='no':
                                continue
                            elif other.lower()=='yes':
                                listLibrary[indexupdate]['Category']=newcategory
                                alllistLibrary()
                                print("Data Has Been Updated")
                                updatelistLibrary()
                                break
                        elif column.lower()=='period' or column.lower()=='borrowing period':
                            while True:  
                                newperiod=int(input("Enter the New Borrowing Period (Maximum 14 Days) : "))
                                if newperiod>=14:
                                    print("Sorry, the Book Borrowing Period is a Maximum of 14 Days")
                                    continue
                                else:
                                    listLibrary[indexupdate]['Borrowing Period']=newperiod
                                    other=input("Are You Sure You Want to Change the Data Column? (yes/no)")
                                    if other.lower()=='no':
                                        continue
                                    elif other.lower()=='yes':
                                        listLibrary[indexupdate]['Borrowing Period']=newperiod
                                        alllistLibrary()
                                        print("Data Has Been Updated")
                                        updatelistLibrary()
                                        break
                        elif column.lower() == 'end':
                            updatelistLibrary()
                            break
                        break 
                elif next.lower()=='no':
                    continue
            else:
                print("Sorry, the Data You Are Looking For Does Not Exist")
                result=[]
                continue
            break
        elif submenu==2:
            break
        else:
            print("Sorry, the Submenu Option You Entered Does Not Exist")

def deletelistLibrary():    
    while True:
        print('''
        ================================================================================================= 
                                            DELETE LIBRARY DATA
        ================================================================================================= 

            1. Delete Specific Library Data
            2. Delete All Library Data
            3. Return to Main Menu
        ''')
        submenu = int(input("Please Select a Submenu to Delete Library Data : "))
        if submenu==1:  
            alllistLibrary()
            result=[]
            for i in range(len(listLibrary)):
                result.append(listLibrary[i]['ID'])
            iddelete = input("Enter the ID of the Book Borrower to be Deleted : ")
            if iddelete in result: 
                indexdelete=result.index(iddelete)
                yesno=input(f"Are You Sure You Want to Delete the Data With ID {iddelete}? (yes/no)")
                if yesno.lower()=='yes':
                    del listLibrary[indexdelete]
                    alllistLibrary()
                    print("Data Has Been Deleted")
                elif yesno.lower()=='no':
                    continue
            else:
                print("Sorry, the Data You Are Looking For Does Not Exist")
                result=[]
        elif submenu==2:
            yesno=input("Are You Sure You Want to Delete All Library Data? (yes/no)")
            if yesno.lower()=='yes':
                listLibrary.clear()
                print("All Data Has Been Deleted")
                alllistLibrary()
            elif yesno.lower()=='no':
                continue
        elif submenu==3:
            break
        else:
            print("Sorry, the Submenu Option You Entered Does Not Exist")
     
Library()