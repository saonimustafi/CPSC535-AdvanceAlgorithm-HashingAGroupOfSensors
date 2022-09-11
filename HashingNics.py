# Both 'in1.txt' and 'in2.txt' files get executed at the same time

import sys

# Class Item
class Item:
    def __init__(self) -> None:
        self.item= {}
        
    # Method to insert the keys and values into the 'item' dict and return the keys
    def itemKeys(self,data):
        self.item[data[-6:]] = data[0:-7]
        keys = []
        if len(keys) != 0:
            keys.pop()
        for i in self.item.keys():
            keys.append(i)
        return keys

# Class ItemCollection having all the Hash Tables and the member functions for all the networks
class ItemCollection:
    # Initialize all the 6 hash tables for the networks
    def __init__(self) -> None:
        self.HashTable1 = [[] for _ in range(16)]
        self.HashTable2 = [[] for _ in range(16)]
        self.HashTable3 = [[] for _ in range(16)]
        self.HashTable4 = [[] for _ in range(16)]
        self.HashTable5 = [[] for _ in range(16)]
        self.HashTable6 = [[] for _ in range(16)]
 
    # Method addItem() to add keys and values to the six HashTables -

    # 1. The items are being inserted into the hash tables of a network by first computing the keys using the 
    # itemKeys() of 'Item' class and then finding out their correct position in the hash tables using the six hashfct methods
    # 2. An object of the 'Item' class is first created and then the six hashfct() methods are called by passing this key as the
    # argument and then insert the item in its correct position in the hash tables using the result returned by the hashfct() methods.
    
    def addItem(self, data):                    # Add item for Network 1
        i = Item()                              # Create an object of the Item class 
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])              # Call hashfct1() 
        self.HashTable1[k1].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable11 for Network 1
        k2 = self.hashfct2(key[0])              # Call hashfct2() 
        self.HashTable2[k2].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable21 for Network 1
        k3 = self.hashfct3(key[0])              # Call hashfct3() 
        self.HashTable3[k3].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable31 for Network 1
        k4 = self.hashfct4(key[0])              # Call hashfct4() 
        self.HashTable4[k4].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable41 for Network 1
        k5 = self.hashfct5(key[0])              # Call hashfct5()
        self.HashTable5[k5].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable51 for Network 1
        k6 = self.hashfct6(key[0])              # Call hashfct6()
        self.HashTable6[k6].append(i.item)      # Insert the item (key, value) in its correct position in the HashTable61 for Network 1
    
    
    # Method removeItem() to remove items from the six Hash Tables of Network 3
    def removeItem(self, remlist):

        # Removes item from the HashTable1 based on first digit by calling hashfct1() method
        for nic in remlist:             
            key1 = self.hashfct1(nic)  
            for i in self.HashTable1[key1]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable1[key1].remove({})

            # Removes item from the HashTable2 based on second digit by calling hashfct2() method
            key2 = self.hashfct2(nic)
            for i in self.HashTable2[key2]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable2[key2].remove({})

            # Removes item from the HashTable3 based on third digit by calling hashfct3() method    
            key3 = self.hashfct3(nic)
            for i in self.HashTable3[key3]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable3[key3].remove({})

            # Removes item from the HashTable4 based on fourth digit by calling hashfct4() method     
            key4 = self.hashfct4(nic)
            for i in self.HashTable4[key4]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable4[key4].remove({})

            # Removes item from the HashTable5 based on fifth digit by calling hashfct5() method 
            key5 = self.hashfct5(nic)
            for i in self.HashTable5[key5]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable5[key5].remove({})
            
            ## Removes item from the HashTable6 based on six digit by calling hashfct6() method 
            key6 = self.hashfct6(nic)
            for i in self.HashTable6[key6]:
                if nic in i.keys():
                    #i.pop(nic)
                    del i[nic]
                    break
            self.HashTable6[key6].remove({})

        # Calculate the size of one of the HashTables after removing the nics and print the size
        sum = 0
        for i in range(len(self.HashTable1)):
            sum = sum + len(self.HashTable1[i])
        
        print(f'Then remove NICs : {" and ".join(remlist)}. Size becomes {sum}')

    # hashfct1() method returns the first digit of the nic key 
    def hashfct1(self, nic):
        k = int(nic[0],16)
        return k

    # hashfct2() method returns the second digit of the nic key
    def hashfct2(self, nic):
        k = int(nic[1],16) 
        return k

    # hashfct3() method returns the third digit of the nic key
    def hashfct3(self, nic):
        k = int(nic[2],16)
        return k

    # hashfct4() method returns the fourth digit of the nic key
    def hashfct4(self, nic):
        k = int(nic[3],16)
        return k

    # hashfct5() method returns the fifth digit of the nic key
    def hashfct5(self, nic):
        k = int(nic[4],16)
        return k

    # hashfct6() method returns the sixth digit of the nic key
    def hashfct6(self, nic):
        k = int(nic[5],16)
        return k

    # bestHashing() method to calculate the best Hashing Table among the six HashTables and
    # return the digit based on which outputs the Hash Table with uniform load distribution.
    def bestHashing(self):     
        dict = {}
        j=1
        for table in [self.HashTable1,self.HashTable2,self.HashTable3,self.HashTable4,self.HashTable5,self.HashTable6]:
            maxcount = 0
            mincount = sys.maxsize
            for i in table:
                count = len(i)
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
                diff = maxcount - mincount
            dict[j] = diff 
            j= j+1
        key = min(dict, key = dict.get)

        return key

       
    # readText() method that takes file name as the input and calls the respective addItem()
    # methods for every item in the file and adds them to the six HasTables.
    def readText(self, flname):
        list = []
        list1 = []
        if(flname == "in1.txt"):
            list.clear()
            fl = open(flname, "r")
            print(f'Successfully opened file {flname}')
            datainput = fl.read()
            datainput = datainput.split('\n')
            fl.close()
            for val in datainput:
                list.append(val)
            for l in list:
                self.addItem(l)
            size = 0
            for i in range(len(self.HashTable1)):
                size = size + len(self.HashTable1[i])
            print(f'New network. Size is {size} after reading {flname}.')
        elif(flname == "in2.txt"):
            list1.clear()
            fl1 = open(flname, "r")
            print(f'Successfully opened file {flname}')
            datainput1 = fl1.read()
            datainput1 = datainput1.split('\n')
            fl1.close()
            for val in datainput1:
                list1.append(val)
            for l in list1:
                self.addItem(l)
            
            size = 0
            for i in range(len(self.HashTable1)):
                size = size + len(self.HashTable1[i])
            print(f'New network. Size is {size} after reading {flname}.')
        return flname,size

    # def displayHash(self,HashTable):
    #     for i in range(len(HashTable)):
    #         print(i, end = " ")

    #         for j in HashTable[i]:
    #             print("-->", end = " ")
    #             print(j, end = " ")

    #         print()


    # def printHash(self):
    #     print("HashTable1")
    #     self.displayHash(self.HashTable1)
    #     print("HashTable2")
    #     self.displayHash(self.HashTable2)
    #     print("HashTable3")
    #     self.displayHash(self.HashTable3)
    #     print("HashTable4")
    #     self.displayHash(self.HashTable4)
    #     print("HashTable5")
    #     self.displayHash(self.HashTable5)
    #     print("HashTable6")
    #     self.displayHash(self.HashTable6)

if __name__ == '__main__':
    
    item1 = ItemCollection()
    item2 = ItemCollection()
    item3 = ItemCollection()
    item4 = ItemCollection()

    
    itemsfind =[]
    num1 = input("Enter number of items to find what the six hash function returns: ")
    for i in range(0, int(num1)):
        item = input("Enter the 6-digit NIC number - ")         # Enter a 6-digit NIC number 
        itemsfind.append(item)
    for nic in itemsfind:   
        k1 = item1.hashfct1(nic)                                # Call hashfct1()
        print(f'hash function 1 on item {nic} returns {k1}')    # Print the hash value returned
        k2 = item1.hashfct2(nic)                                # Call hashfct2()
        print(f'hash function 2 on item {nic} returns {k2}')    # Print the hash value returned
        k3 = item1.hashfct3(nic)                                # Call hashfct3()
        print(f'hash function 3 on item {nic} returns {k3}')    # Print the hash value returned
        k4 = item1.hashfct4(nic)                                # Call hashfct4()
        print(f'hash function 4 on item {nic} returns {k4}')    # Print the hash value returned
        k5 = item1.hashfct5(nic)                                # Call hashfct5()
        print(f'hash function 5 on item {nic} returns {k5}')    # Print the hash value returned
        k6 = item1.hashfct6(nic)                                # Call hashfct6()
        print(f'hash function 6 on item {nic} returns {k6}')    # Print the hash value returned

    print()
    
    print('Network 1')
    itemsadd = []
    num2 = input("Enter number of items to add to network 1 : ")        # Enter the number of records to add to form Network 1
    for i in range(0, int(num2)):
        item = input("Enter the full name of the sensor - ")            # Enter the full names of the sensor to add
        itemsadd.append(item)
    for item in itemsadd:
        item1.addItem(item)                                                     # Call the addItem() to add the items individually to the network
    print(f'Size is {len(itemsadd)} after adding {" and ".join(itemsadd)}')     # Print the size
    besthash1 = item1.bestHashing()                                             # Call the bestHashing() method for Network 1
    print(f'BestHashing() for Network 1 {itemsadd} returns {besthash1}')        # Print the best hashed table among the six tables for Network1
    print()
    

    print('Network 2')
    flname = item2.readText("in1.txt")                                 # Call the readText function to read the sensors in file "in1.txt" and form Network 2
    besthash2 = item2.bestHashing()                                    # Call the bestHashing() method for Network 2
    print(f'BestHashing() for {flname[0]} returns {besthash2}')        # Print the best hashed table among the six tables for Network 2
    print()

    print('Network 3')
    flname = item3.readText("in2.txt")                                 # Call the readText function to read the sensors in file "in2.txt" and form Network 3
    besthash3 = item3.bestHashing()                                    # Call the bestHashing() method for Network 3 and 
    print(f'BestHashing() for {flname[0]} returns {besthash3}')        # Print the best hashed table among the six tables for Network 3
    print()


    print('Network 4')
    itemsremove = []
    fname = item4.readText("in2.txt") 
    num4 = input("Enter number of items to remove from network 3 and create a new network: ")       # Enter the number of NICs you want to remove from Network 3
    for i in range(0, int(num4)):
        item = input("Enter the 6-digit NIC number to remove - ")                                   # Enter only the 6-digit NICs you want to remove 
        itemsremove.append(item)
    item4.removeItem(itemsremove)
    besthash4 = item4.bestHashing()                                                                 # Call the bestHashing() method for Network 4
    print(f'BestHashing() after removing {" and ".join(itemsremove)} returns {besthash4}')          # Print the best hashed table among the six tables for Network 4  
    print()

    # print('Network 1')
    # item1.printHash()
    # print('Network 2')
    # item2.printHash()
    # print('Network 3')
    # item3.printHash()
    # print('Network 4')
    # item4.printHash()