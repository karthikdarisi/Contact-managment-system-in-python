
class ContactManagementSystem:
    def __init__(self,uemail,upassword,umobilenumber):
        self.uemail = uemail
        self.upassword = upassword
        self.umobilenumber = umobilenumber
        self.contacts=[]
    def loadcontacts(self):
        f = open("contact.txt", "r")
        txt = f.read()
        nl=txt.split("\n")
        for i in nl[:-1]:
            nnl=i.split(",")
            contact1=Contacts(nnl[0],nnl[1],int(nnl[2]))
            self.contacts.append(contact1)
        f.close()
    def savecontacts(self):
        f = open("contact.txt", "w")
        for i in self.contacts:
            f.write(f"{i.name},{i.email},{i.number}\n")
        f.close()
    def addcontact(self,contact):
        self.contacts.append(contact)
        self.savecontacts()


    def searchcontactbyname(self,name):
        for i in self.contacts:
            if i.name==name:
                print("Name found")
                print(f"Name:{i.name}")
                print(f"Email:{i.email}")
                print(f"Number:{i.number}")
                return i
        print("Contact not found")
        return None


    def searchcontactbymobilenumber(self,mobilenumber):
        for i in self.contacts:
            if i.number == mobilenumber:
                print("Mobile number found")
                print(f"Name:{i.name}")
                print(f"Email:{i.email}")
                print(f"Number:{i.number}")
                return i
        print("Contact not found")
        return None

    def deletecontact(self,res):
        self.contacts.remove(res)
        self.savecontacts()
class Contacts:
    def __init__(self,name,email,number):
        self.name = name
        self.email = email
        self.number = number
CMS = ContactManagementSystem(input("enter your mail:"),input("enter your password:"),input("enter your mobile number:"))
CMS.loadcontacts()
print("WELCOME TO CONTACT MANAGEMENT SYSTEM".center(150," "))
print("1. Create new contact")
print("2. Search contact by mobile number")
print("3. Search contact by Name")
print("4. Delete contact")
print("5. Update contact")
print("6. Exit")
choice = input("Enter your choice: ")
while choice != "6":
    if choice == "1":
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        number = int(input("Enter contact number: "))
        contact= Contacts(name, email, number)
        CMS.addcontact(contact)

    if choice == "2":
        number = int(input("Enter contact number: "))
        CMS.searchcontactbymobilenumber(number)
    if choice == "3":
        name = input("Enter contact name: ")
        CMS.searchcontactbyname(name)
    if choice == "4":
        name = input("Enter contact name: ")
        res=CMS.searchcontactbyname(name)
        if res==None:
            print("Contact not found")
        else:
            CMS.deletecontact(res)
            print("Contact deleted")

    if choice == "5":
        name = input("Enter contact name: ")
        res=CMS.searchcontactbyname(name)
        if res==None:
            print("Contact not found")
        else:
            name=input("Enter new contact name: ")
            number=int(input("Enter new contact number: "))
            email=input("Enter new contact email: ")
            resi=CMS.contacts.index(res)
            CMS.contacts[resi]=Contacts(name,email,number)
            CMS.savecontacts()
            print("Contact updated")
    choice = input("Enter your choice: ")







