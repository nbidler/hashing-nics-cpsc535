# Both Files Execution
# Does not take user input

# Class Item
class Item:
    def __init__(self) -> None:
        self.item= {}
        
    # Method to insert the keys and values into the item dict and return the list of keys
    def itemKeys(self,data):
        self.item[data[-6:]] = data[0:-7]
        keys = []
        if len(keys) != 0:
            keys.pop()
        for i in self.item.keys():
            keys.append(i)
        return keys

# Class ItemCollection
class ItemCollection():
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
    def addItem1(self, data):
        i = Item()
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])
        self.HashTable11[k1].append(i.item)
        k2 = self.hashfct2(key[0])
        self.HashTable21[k2].append(i.item)
        k3 = self.hashfct3(key[0])
        self.HashTable31[k3].append(i.item)
        k4 = self.hashfct4(key[0])
        self.HashTable41[k4].append(i.item)
        k5 = self.hashfct5(key[0])
        self.HashTable51[k5].append(i.item)
        k6 = self.hashfct6(key[0])
        self.HashTable61[k6].append(i.item)
    

    def addItem2(self, data):
        i = Item()
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])
        self.HashTable12[k1].append(i.item)
        k2 = self.hashfct2(key[0])
        self.HashTable22[k2].append(i.item)
        k3 = self.hashfct3(key[0])
        self.HashTable32[k3].append(i.item)
        k4 = self.hashfct4(key[0])
        self.HashTable42[k4].append(i.item)
        k5 = self.hashfct5(key[0])
        self.HashTable52[k5].append(i.item)
        k6 = self.hashfct6(key[0])
        self.HashTable62[k6].append(i.item)
        
        return bool

    def addItem3(self, data):
        i = Item()
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0])
        self.HashTable13[k1].append(i.item)
        k2 = self.hashfct2(key[0])
        self.HashTable23[k2].append(i.item)
        k3 = self.hashfct3(key[0])
        self.HashTable33[k3].append(i.item)
        k4 = self.hashfct4(key[0])
        self.HashTable43[k4].append(i.item)
        k5 = self.hashfct5(key[0])
        self.HashTable53[k5].append(i.item)
        k6 = self.hashfct6(key[0])
        self.HashTable63[k6].append(i.item)

    def addItem4(self, data):
        i = Item()
        key = i.itemKeys(data)
        k1 = self.hashfct1(key[0]) 
        self.HashTable14[k1].append(i.item)
        k2 = self.hashfct2(key[0])
        self.HashTable24[k2].append(i.item)
        k3 = self.hashfct3(key[0])
        self.HashTable34[k3].append(i.item)
        k4 = self.hashfct4(key[0])
        self.HashTable44[k4].append(i.item)
        k5 = self.hashfct5(key[0])
        self.HashTable54[k5].append(i.item)
        k6 = self.hashfct6(key[0])
        self.HashTable64[k6].append(i.item)
    

    # Method displayHash() to display the HashTables   
    def displayHash(self,HashTable):
        for i in range(len(HashTable)):
            print(i, end = " ")
        
            for j in HashTable[i]:
                print("-->", end = " ")
                print(j, end = " ")
                
            print()

    # Method removeItem() to remove items from the six HashTables
    def removeItem(self, remlist):
        self.readText4("in2.txt")
        # self.printHash4()
        print(remlist)            

        for nic in remlist:             
            key1 = self.hashfct1(nic)  
            for i in self.HashTable14[key1]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable14[key1].remove({})

            key2 = self.hashfct2(nic)
            for i in self.HashTable24[key2]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable24[key2].remove({})
                
            key3 = self.hashfct3(nic)
            for i in self.HashTable34[key3]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable34[key3].remove({})
                
            key4 = self.hashfct4(nic)
            for i in self.HashTable44[key4]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable44[key4].remove({})

            key5 = self.hashfct5(nic)
            for i in self.HashTable54[key5]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable54[key5].remove({})
            
            key6 = self.hashfct6(nic)
            for i in self.HashTable64[key6]:
                if nic in i.keys():
                    i.pop(nic)
                    break
            self.HashTable64[key6].remove({})

        # Calculate the size of one of the HashTables after removing the nics
        sum = 0
        for i in range(len(self.HashTable14)):
            sum = sum + len(self.HashTable14[i])
        
        print(f'Remove NICs {" and ".join(remlist)}. Size becomes {sum}')

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
    # return the digit based on which outputs the Hash Table with uniform load distribution
    def bestHashing1(self):
        dict = {}
        j=1
        for table in [self.HashTable11,self.HashTable21,self.HashTable31,self.HashTable41,self.HashTable51,self.HashTable61]:
            maxcount = 0
            mincount = 100
            for i in table:
                count = len(i)
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
                diff = maxcount - mincount
            dict[j] = diff 
            j= j+1
        print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing2(self):
        dict = {}
        j=1
        for table in [self.HashTable12,self.HashTable22,self.HashTable32,self.HashTable42,self.HashTable52,self.HashTable62]:
            maxcount = 0
            mincount = 100
            for i in table:
                count = len(i)
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
                diff = maxcount - mincount
            dict[j] = diff 
            j= j+1
        print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing3(self):
        dict = {}
        j=1
        for table in [self.HashTable13,self.HashTable23,self.HashTable33,self.HashTable43,self.HashTable53,self.HashTable63]:
            maxcount = 0
            mincount = 100
            for i in table:
                count = len(i)
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
                diff = maxcount - mincount
            dict[j] = diff 
            j= j+1
        print(dict)
        key = min(dict, key = dict.get)
        return key

    def bestHashing4(self):
        dict = {}
        j=1
        for table in [self.HashTable14,self.HashTable24,self.HashTable34,self.HashTable44,self.HashTable54,self.HashTable64]:
            maxcount = 0
            mincount = 100
            for i in table:
                count = len(i)
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
                diff = maxcount - mincount
            dict[j] = diff 
            j= j+1
        print(dict)
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
    
    # readText() method that takes file name as the input and calls addItem()
    # method for every item in the file and adds them to the six HasTables
    def readText(self, flname):
        list = []
        #flname = input("Enter the data file you want to process: ")
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
        # input("Enter the data file you want to process: ")
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

    items = ['123456', '6789AB']
    for nic in items:
    # nic = input("Enter the 6-digit NIC number to find the hash functions: ")    # Enter a NIC to know what the six hashfct methos return
        k1 = item1.hashfct1(nic)
        print(f'hash function 1 on item {nic} returns {k1}')
        k2 = item1.hashfct2(nic)
        print(f'hash function 2 on item {nic} returns {k2}')
        k3 = item1.hashfct3(nic)
        print(f'hash function 3 on item {nic} returns {k3}')
        k4 = item1.hashfct4(nic)
        print(f'hash function 4 on item {nic} returns {k4}')
        k5 = item1.hashfct5(nic)
        print(f'hash function 5 on item {nic} returns {k5}')
        k6 = item1.hashfct6(nic)
        print(f'hash function 6 on item {nic} returns {k6}')

    print('Network 1')
    items = ['Velocity sensor 123456', 'Particle sensor 234567']
    for item in items:
        item1.addItem1(item)
    print(f'Size is {len(items)} after adding {" and ".join(items)}')
    besthash1 = item1.bestHashing1()
    print(f'BestHashing() for Network 1 {items} returns {besthash1}')
    print()
    
    
    print('Network 2') 
    flname = item2.readText("in1.txt") 
    # item2.printHash2()                  # Call the printHash() method to print the six HashTables
    besthash2 = item2.bestHashing2()            # Call the bestHashing() method and print the best HashTable among six of them
    print(f'BestHashing2() for {flname[0]} returns {besthash2}')
    print()

    print('Network 3')
    flname = item3.readText("in2.txt")
    # item3.printHash3()
    besthash3 = item3.bestHashing3()
    print(f'BestHashing3() for {flname[0]} returns {besthash3}')
    print()

    print('Network 4')
    remlist = ["110987","210FED"]
    item4.removeItem(remlist)
    # item4.printHash4()
    besthash4 = item4.bestHashing4()   
    print(f'BestHashing() after removing {" and ".join(remlist)} returns {besthash4}')
    print()