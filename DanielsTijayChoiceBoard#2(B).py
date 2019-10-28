"""

Daniels Tijay
"""

#class definition for node

class Node:

    def __init__(self, name, pdate, pamount, q):
        self.name = name
        self.pdate = pdate
        self.pamount = pamount
        self.q = q
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, name, pdate, pamount, q):
        temp = Node(name, pdate, pamount, q)
        temp.link = self.head
        self.head = temp

    def update(self, name, q):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            found = False
            if current.name == name:  #is the first node what we're looking for?
                #print("Found")
                found = True
                current.q = q
            else:
                while current.link is not None and current.name != name:
                    current = current.link
                    if current.name == name:  
                        current.q = q
                    else:
                        found= False
                if found == False:
                    print("That item was not found.")
                else:
                    print("The Quantity for", name, "has been updated to", current.q)
        


    def inventory(self, pamount):
        total = 0
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                total += pamount
                current = current.link
        print("Total Value of ALL Inventory = ", total)

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            current = self.head
            while current is not None:
                print(current.name , " ", current.pdate, " ", current.pamount, " ", current.q, " ")
                current = current.link

def main():

    myList  = LinkedList()
    print("WELCOME!")
    print(" [1] - Add a New Piece of Equipment")
    print(" [2] - Update the Quantity on hand")
    print(" [3] - Finish & Calculate Total Value of all Inventory")
    print(" [4] - Quit")
    answer = input("WHAT WOULD YOU LIKE TO DO?")
    while answer != '4':
        if answer == '1':
            print("Add a New Piece of Equipment: ")
            name = input("What is the equipment name? ")
            pdate = input("What is the purchase date? ")
            pamount = float(input("What is the purchase amount? "))
            q = input("What is the quantity on hand? ")
            myList.insert_at_start(name, pdate, pamount, q)
        elif answer == '2':
            print("Updating the quantity on hand")
            name = input("What is the product Name? ")
            q = input("What is the new number of quantity ")
            myList.update(name, q)
        elif answer == '3':
            myList.inventory(pamount)
        else:
            print("Invalid Input")
        print(" [1] - Add a New Piece of Equipment")
        print(" [2] - Update the Quantity on hand")
        print(" [3] - Finish & Calculate Total Value of all Inventory")
        print(" [4] - Quit")
        answer = input("WHAT WOULD YOU LIKE TO DO?")
    print("Thank you for using this program!")
    myList.traverse_list()
main()




                


        
            
            

        
    
