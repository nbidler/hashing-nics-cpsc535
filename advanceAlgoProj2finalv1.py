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
class ItemCollection():
    # Initialize all the 24 hash tables for the four networks
    def __init__(self) -> None:
        self.HashTable11 = [[] for _ in range(16)]
        self.HashTable21 = [[] for _ in range(16)]
        self.HashTable31 = [[] for _ in range(16)]
        self.HashTable41 = [[] for _ in range(16)]
        self.HashTable51 = [[] for _ in range(16)]
        self.HashTable61 = [[] for _ in range(16)]
        self.HashTable12 = [[] for _ in range(16)]
        self.HashTable22 = [[] for _ in range(16)]
        self.HashTable32 = [[] for _ in range(16)]
        self.HashTable42 = [[] for _ in range(16)]
        self.HashTable52 = [[] for _ in range(16)]
        self.HashTable62 = [[] for _ in range(16)]
        self.HashTable13 = [[] for _ in range(16)]
        self.HashTable23 = [[] for _ in range(16)]
        self.HashTable33 = [[] for _ in range(16)]
        self.HashTable43 = [[] for _ in range(16)]
        self.HashTable53 = [[] for _ in range(16)]
        self.HashTable63 = [[] for _ in range(16)]
        self.HashTable14 = [[] for _ in range(16)]
        self.HashTable24 = [[] for _ in range(16)]
        self.HashTable34 = [[] for _ in range(16)]
        self.HashTable44 = [[] for _ in range(16)]
        self.HashTable54 = [[] for _ in range(16)]
        self.HashTable64 = [[] for _ in range(16)]

    # Method addItem() to add keys and values to the six HashTables

    # 1. The items are being inserted into their respective hash tables of a network by first computing the keys using the 
    # itemKeys() of 'Item' class and then finding out their correct position in the hash tables using the six hashfct methods
    # 2. An object of the 'Item' class is first created and then the six hashfct() methods are called by passing this key as the
    # argument and then insert the item in its correct position in the hash tables using the result returned by the hashfct() methods.
    
    def addItem1(self, data):                   # Add item for Network 1
        i = Item()                              # Create an object of the Item class 
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])              # Call hashfct1() 
        self.HashTable11[k1].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable11 for Network 1
        k2 = self.hashfct2(key[0])              # Call hashfct2() 
        self.HashTable21[k2].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable21 for Network 1
        k3 = self.hashfct3(key[0])              # Call hashfct3() 
        self.HashTable31[k3].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable31 for Network 1
        k4 = self.hashfct4(key[0])              # Call hashfct4() 
        self.HashTable41[k4].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable41 for Network 1
        k5 = self.hashfct5(key[0])              # Call hashfct5()
        self.HashTable51[k5].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable51 for Network 1
        k6 = self.hashfct6(key[0])              # Call hashfct6()
        self.HashTable61[k6].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable61 for Network 1
    
    
    def addItem2(self, data):                   # Add item for Network 2
        i = Item()                              # Create an object of the Item class
        key = i.itemKeys(data)                  
        k1 = self.hashfct1(key[0])              # Call hashfct1()
        self.HashTable12[k1].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable12 for Network2
        k2 = self.hashfct2(key[0])              # Call hashfct2()
        self.HashTable22[k2].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable22 for Network2
        k3 = self.hashfct3(key[0])              # Call hashfct3()
        self.HashTable32[k3].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable32 for Network2
        k4 = self.hashfct4(key[0])              # Call hashfct4()
        self.HashTable42[k4].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable42 for Network2
        k5 = self.hashfct5(key[0])              # Call hashfct5()
        self.HashTable52[k5].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable52 for Network2
        k6 = self.hashfct6(key[0])              # Call hashfct6()
        self.HashTable62[k6].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable62 for Network2


    def addItem3(self, data):                   # Add item for Network 3
        i = Item()                              # Create an object of the Item class
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])              # Call hashfct1()
        self.HashTable13[k1].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable13 for Network 3
        k2 = self.hashfct2(key[0])              # Call hashfct2()
        self.HashTable23[k2].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable23 for Network 3
        k3 = self.hashfct3(key[0])              # Call hashfct3()
        self.HashTable33[k3].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable33 for Network 3
        k4 = self.hashfct4(key[0])              # Call hashfct4()
        self.HashTable43[k4].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable43 for Network 3
        k5 = self.hashfct5(key[0])              # Call hashfct5()
        self.HashTable53[k5].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable53 for Network 3
        k6 = self.hashfct6(key[0])              # Call hashfct6()
        self.HashTable63[k6].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable63 for Network 3

    def addItem4(self, data):                   # Add item for Network 4
        i = Item()                              # Create an object of the Item class
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])              # Call hashfct1()
        self.HashTable14[k1].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable14 for Network 4
        k2 = self.hashfct2(key[0])              # Call hashfct1()
        self.HashTable24[k2].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable24 for Network 4
        k3 = self.hashfct3(key[0])              # Call hashfct1()
        self.HashTable34[k3].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable34 for Network 4
        k4 = self.hashfct4(key[0])              # Call hashfct1()
        self.HashTable44[k4].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable44 for Network 4
        k5 = self.hashfct5(key[0])              # Call hashfct1()
        self.HashTable54[k5].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable54 for Network 4
        k6 = self.hashfct6(key[0])              # Call hashfct1()
        self.HashTable64[k6].append(i.item)     # Insert the item (key, value) in its correct position in the HashTable64 for Network 4
    

    # Method displayHash() to display the HashTables   
    def displayHash(self,HashTable):
        for i in range(len(HashTable)):
            print(i, end = " ")
        
            for j in HashTable[i]:
                print("-->", end = " ")
                print(j, end = " ")
                
            print()

    # Method removeItem() to remove items from the six Hash Tables of Network 3
    def removeItem(self, remlist):
        self.readText4("in2.txt")
        # self.printHash4()
        print("New network then read in2.txt")

        # Removes item from the HashTable based on first digit by calling hashfct1() method
        for nic in remlist:             
            key1 = self.hashfct1(nic)  
            for i in self.HashTable14[key1]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable14[key1].remove({})

            # Removes item from the HashTable based on second digit by calling hashfct2() method
            key2 = self.hashfct2(nic)
            for i in self.HashTable24[key2]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable24[key2].remove({})

            # Removes item from the HashTable based on third digit by calling hashfct3() method    
            key3 = self.hashfct3(nic)
            for i in self.HashTable34[key3]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable34[key3].remove({})

            # Removes item from the HashTable based on fourth digit by calling hashfct4() method     
            key4 = self.hashfct4(nic)
            for i in self.HashTable44[key4]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable44[key4].remove({})

            # Removes item from the HashTable based on fifth digit by calling hashfct5() method 
            key5 = self.hashfct5(nic)
            for i in self.HashTable54[key5]:
                if nic in i.keys():
                    del i[nic]
                    break
            self.HashTable54[key5].remove({})
            
            ## Removes item from the HashTable based on six digit by calling hashfct6() method 
            key6 = self.hashfct6(nic)
            for i in self.HashTable64[key6]:
                if nic in i.keys():
                    #i.pop(nic)
                    del i[nic]
                    break
            self.HashTable64[key6].remove({})

        # Calculate the size of one of the HashTables after removing the nics and print the size
        sum = 0
        for i in range(len(self.HashTable14)):
            sum = sum + len(self.HashTable14[i])
        
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
    def bestHashing1(self):     # Calculates bestHashing for Network 1
        dict = {}
        j=1
        for table in [self.HashTable11,self.HashTable21,self.HashTable31,self.HashTable41,self.HashTable51,self.HashTable61]:
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
        # print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing2(self):     # Calculates bestHashing for Network 2
        dict = {}
        j=1
        for table in [self.HashTable12,self.HashTable22,self.HashTable32,self.HashTable42,self.HashTable52,self.HashTable62]:
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
        # print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing3(self):     # Calculates bestHashing for Network 3
        dict = {}
        j=1
        for table in [self.HashTable13,self.HashTable23,self.HashTable33,self.HashTable43,self.HashTable53,self.HashTable63]:
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
        # print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing4(self):     # Calculates bestHashing for Network 4
        dict = {}
        j=1
        for table in [self.HashTable14,self.HashTable24,self.HashTable34,self.HashTable44,self.HashTable54,self.HashTable64]:
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
        # print(dict)
        key = min(dict, key = dict.get)
        return key

    # printHash() method calls the displayHash() method to print the six HashTables
    def printHash1(self):           # Display Network 1
        print("HashTable11")
        self.displayHash(self.HashTable11)
        print("HashTable21")
        self.displayHash(self.HashTable21)
        print("HashTable31")
        self.displayHash(self.HashTable31)
        print("HashTable41")
        self.displayHash(self.HashTable41)
        print("HashTable51")
        self.displayHash(self.HashTable51)
        print("HashTable61")
        self.displayHash(self.HashTable61)

    def printHash2(self):           # Display Network 2
        print("HashTable12")
        self.displayHash(self.HashTable12)
        print("HashTable22")
        self.displayHash(self.HashTable22)
        print("HashTable32")
        self.displayHash(self.HashTable32)
        print("HashTable42")
        self.displayHash(self.HashTable42)
        print("HashTable52")
        self.displayHash(self.HashTable52)
        print("HashTable62")
        self.displayHash(self.HashTable62)

    def printHash3(self):           # Display Network 3
        print("HashTable13")
        self.displayHash(self.HashTable13)
        print("HashTable23")
        self.displayHash(self.HashTable23)
        print("HashTable33")
        self.displayHash(self.HashTable33)
        print("HashTable43")
        self.displayHash(self.HashTable43)
        print("HashTable53")
        self.displayHash(self.HashTable53)
        print("HashTable63")
        self.displayHash(self.HashTable63)

    def printHash4(self):           # Display Network 4
        print("HashTable14")
        self.displayHash(self.HashTable14)
        print("HashTable24")
        self.displayHash(self.HashTable24)
        print("HashTable34")
        self.displayHash(self.HashTable34)
        print("HashTable44")
        self.displayHash(self.HashTable44)
        print("HashTable54")
        self.displayHash(self.HashTable54)
        print("HashTable64")
        self.displayHash(self.HashTable64)
    
    # readText() method that takes file name as the input and calls the respective addItem()
    # methods for every item in the file and adds them to the six HasTables. It calls addItem2()
    # to add items to Network 2 and addItem3() to add items to Network 3.
    def readText(self, flname):
        list = []
        if(flname == "in1.txt"):
            list.clear()
            fl = open(flname, "r")
            print(f'Successfully opened file {flname}')
            datainput = fl.read()
            datainput = datainput.split('\n')
            # print(datainput)
            fl.close()
            for val in datainput:
                list.append(val)
            # print(list)
            for l in list:
                self.addItem2(l)
            size = 0
            size = size + len(list)
            print(f'New network. Size is {size} after reading {flname}.')
        if(flname == "in2.txt"):
            list.clear()
            fl = open(flname, "r")
            print(f'Successfully opened file {flname}')
            datainput = fl.read()
            datainput = datainput.split('\n')
            # print(datainput)
            fl.close()
            for val in datainput:
                list.append(val)
            # print(list)
            for l in list:
                self.addItem3(l)
            size = 0
            size = size + len(list)
            print(f'New network. Size is {size} after reading {flname}.')
        return flname,size

    def readText4(self,flname):
        list = []
        fl = open(flname, "r")
        print(f'Successfully opened file {flname}')
        datainput = fl.read()
        datainput = datainput.split('\n')
        # print(datainput)
        fl.close()
        for val in datainput:
            list.append(val)
        # print(list)
        for l in list:
            self.addItem4(l)
        size = 0
        size = size + len(list)
        return flname,size


if __name__ == '__main__':
    
    item1 = ItemCollection()
    item2 = ItemCollection()
    item3 = ItemCollection()
    item4 = ItemCollection()

    #items = ['123456', '6789AB']
    itemsfind =[]
    num1 = input("Enter number of items to find what the six hash function returns: ")
    for i in range(0, int(num1)):
        item = input("Enter the 6-digit NIC number - ")     # Enter a 6-digit NIC number 
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

    print('Network 1')
    itemsadd = []
    num2 = input("Enter number of items to add to network 1 : ")        # Enter the number of records to add to form Network 1
    for i in range(0, int(num2)):
        item = input("Enter the full name of the sensor - ")            # Enter the full names of the sensor to add
        itemsadd.append(item)
    for item in itemsadd:
        item1.addItem1(item)                                                    # Call the addItem1() to add the items individually to the network
    print(f'Size is {len(itemsadd)} after adding {" and ".join(itemsadd)}')     # Print the size
    besthash1 = item1.bestHashing1()                                            # Call the bestHashing1() method for Network 2
    print(f'BestHashing() for Network 1 {itemsadd} returns {besthash1}')        # Print the best hashed table among the six tables for Network1
    print()
    
    
    print('Network 2') 
    flname = item2.readText("in1.txt")                                  # Call the readText function to read the sensors in file "in1.txt" and form Network 2
    # item2.printHash2()
    besthash2 = item2.bestHashing2()                                    # Call the bestHashing2() method for Network 2
    print(f'BestHashing() for {flname[0]} returns {besthash2}')        # Print the best hashed table among the six tables for Network 2
    print()

    print('Network 3')
    flname = item3.readText("in2.txt")                                  # Call the readText function to read the sensors in file "in2.txt" and form Network 3
    # item3.printHash3()
    besthash3 = item3.bestHashing3()                                    # Call the bestHashing3() method for Network 2 and 
    print(f'BestHashing() for {flname[0]} returns {besthash3}')        # Print the best hashed table among the six tables for Network 3
    print()

    print('Network 4')
    itemsremove = []
    num4 = input("Enter number of items to remove from network 3 and create a new network: ")       # Enter the number of NICs you want to remove from Network 3
    for i in range(0, int(num4)):
        item = input("Enter the 6-digit NIC number to remove - ")                                   # Enter only the 6-digit NICs you want to remove 
        itemsremove.append(item)
    item4.removeItem(itemsremove)                                                                   # Call the removeItem() and remove the items passed in the argument
    # item4.printHash4()
    besthash4 = item4.bestHashing4()                                                                # Call the bestHashing4() method for Network 4
    print(f'BestHashing() after removing {" and ".join(itemsremove)} returns {besthash4}')          # Print the best hashed table among the six tables for Network 4  
    print()