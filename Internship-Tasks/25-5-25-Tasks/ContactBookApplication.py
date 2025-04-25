class ContactBook:
    contact_book={}
    def __init__(self):
        while True:
            print("\n\tContact Book Menu \t\t")
            print("\t1. Add Contact")
            print("\t2. Search Contact")
            print("\t3. Delete Contact")
            print("\t4.Exit")
            try:
                ch=int(input("Enter Your Choice:"))
                match(ch):
                    case 1:
                        self.add()
                    case 2:
                        self.search()
                    case 3:
                        self.delete()
                    case 4:
                        print("ThankYou")
                        break
                    case _:
                        print("Invalid Input,please choose numbers within 1-3")
            except ValueError:
                print("Enter only Numerical numbers(1-4)")
            
    def add(self):
        self.name=input("Enter contact name:").lower()
        phno=int(input("Enter Phone Number:"))
        if self.name.lower() not in self.contact_book:
            self.contact_book[self.name.lower()]=phno
            print("Added Successfully")
        else:
            print("Contact Name Already Exists..")

    def search(self):
        self.name=input("Enter contact Name to search:").lower()
        if self.name.lower() in self.contact_book:
            print(self.contact_book[self.name.lower()])
        else:
            print("NOT FOUND")
        
    def delete(self):
        self.name=input("Enter contact Name to delete:").lower()
        if self.name.lower() in self.contact_book:
            self.contact_book.pop(self.name)
            print("Deleted Successfully")
        else:
            print("There is no specified contact name to delete")
        
obj1=ContactBook()
        
    