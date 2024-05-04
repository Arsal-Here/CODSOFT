maxrange=5
count = 0
name = [" " for i in range(maxrange)]
number = [" " for i in range(maxrange)]
email = [" " for i in range(maxrange)]
address = [" " for i in range(maxrange)]

ch = 'n'
while ch != 'Y' or ch != 'y':
    choice = int(input("1)Add Contact\n2)View Contact List\n3)Search Contact\n4)Update Contact\n5)Delete Contact\n"))
    if choice == 1:
        if (count != maxrange):
            name[count] = str(input("Enter name "))
            number[count] = str(input("Enter number "))
            email[count] = str(input("Enter email "))
            address[count] = str(input("Enter address "))
            count += 1
    elif (choice == 2):
            for i in range(count):
                print("Name: ", name[i])
                print("Number: ", number[i])
                print("Email: ", email[i])
                print("Address: ", address[i],"\n")
    elif (choice == 3):
            search = str(input("Search by Number or Search by Name? "))
            search = search.lower()
            if (search == "number"):
                num = int(input("Enter number "))
                for i in range(count):
                    if (number[i] == num):
                        print("Name: ", name[i])
                        print("Number: ", number[i])
                        print("Email: ", email[i])
                        print("Address: ", address[i])
                    else:
                        print("Not found ")
            elif (search == "name"):
                searchName = str(input("Enter name "))
                for i in range(count):
                    if (name[i] == searchName):
                        print("Name: ", name[i])
                        print("Number: ", number[i])
                        print("Email: ", email[i])
                        print("Address: ", address[i])
                        found=True
                if(found==False):
                    print("Not found ")
    elif (choice == 4):
            searchName = str(input("Enter name of contact to update "))
            for i in range(count):
                if (name[i] == searchName):
                    name[i] = str(input("Enter new name "))
                    number[i] = str(input("Enter new number "))
                    email[i] = str(input("Enter new email "))
                    address[i] = str(input("Enter new address "))
                    foundName=True
            if(foundName==False):
                print("Contact not found ")
            else:
                 print("\nContact updated\n")
    elif (choice == 5):
            foundContact=False
            searchName = str(input("Enter name of contact to delete "))
            for i in range(count):
                if (name[i] == searchName):  
                    name[i]= "Deleted Contact "
                    number[i] ="Deleted Contact "
                    email[i] = "Deleted Contact "
                    address[i]="Deleted Contact "
                    foundContact=True
                else:
                     foundContact=False
            if(foundContact==True):
                    print("Deleted contact")
            else:
                    print("Contact not found ")
    else:
        print("Invalid choice ")
    ch = str(input("Do wish to exit?[Y/N] "))
