class ItemCollection:
    def __init__(self) -> None:
        self.HashTable1 = [[] for _ in range(16)]
        self.HashTable2 = [[] for _ in range(16)]
        self.HashTable3 = [[] for _ in range(16)]
        self.HashTable4 = [[] for _ in range(16)]
        self.HashTable5 = [[] for _ in range(16)]
        self.HashTable6 = [[] for _ in range(16)]

    def addItem(self,data):
        bool = True
        if data in self.HashTable1[int(data[0],16)]:
            bool = False
        else:
            self.HashTable1[int(data[0], 16)].append(data)
            self.HashTable2[int(data[1], 16)].append(data)
            self.HashTable3[int(data[2], 16)].append(data)
            self.HashTable4[int(data[3], 16)].append(data)
            self.HashTable5[int(data[4], 16)].append(data)
            self.HashTable6[int(data[5], 16)].append(data)
        
        return bool
        

    def displayHash(self,HashTable):
        for i in range(len(HashTable)):
            print(i, end = " ")
        
            for j in HashTable[i]:
                print("-->", end = " ")
                print(j, end = " ")
                
            print()

    def hashfct1(self, nic):
        k = int(nic[0],16)
        print(f'hash function 1 on item {nic} returns {k}') 

    def hashfct2(self, nic):
        k = int(nic[1],16)
        print(f'hash function 2 on item {nic} returns {k}') 

    def hashfct3(self, nic):
        k = int(nic[2],16)
        print(f'hash function 3 on item {nic} returns {k}') 

    def hashfct4(self, nic):
        k = int(nic[3],16)
        print(f'hash function 4 on item {nic} returns {k}')

    def hashfct5(self, nic):
        k = int(nic[4],16)
        print(f'hash function 5 on item {nic} returns {k}')

    def hashfct6(self, nic):
        k = int(nic[5],16)
        print(f'hash function 6 on item {nic} returns {k}')

    def bestHashing(self):
        
        dict = {}
        j=1
        for table in [self.HashTable1,self.HashTable2,self.HashTable3,self.HashTable4,self.HashTable5,self.HashTable6]:
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
 
    def printHash(self):
        print("HashTable1")
        self.displayHash(self.HashTable1)
        print("HashTable2")
        self.displayHash(self.HashTable2)
        print("HashTable3")
        self.displayHash(self.HashTable3)
        print("HashTable4")
        self.displayHash(self.HashTable4)
        print("HashTable5")
        self.displayHash(self.HashTable5)
        print("HashTable6")
        self.displayHash(self.HashTable6)
    
    def reatText(self):
        list = []
        flname = input("Enter the data file you want to process: ")
        fl = open(flname, "r")
        print(f'Successfully opened file {flname}')
        datainput = fl.read()
        datainput = datainput.split('\n')
        print(datainput)
        fl.close()
        for val in datainput:
            list.append(val[-6:])
        print(list)
        for l in list:
            self.addItem(l)
        size = 0
        size = size + len(list)
        print(f'New network. Size is {size} after reading {flname}.')
        return flname


if __name__ == '__main__':
    
    item = ItemCollection()
    flname = item.reatText()
    item.printHash()
    key = item.bestHashing()
    print(f'BestHashing() for {flname} returns {key}')
    nic = input("Enter the 6-digit NIC number to find the hash functions: ")
    item.hashfct1(nic)
    item.hashfct2(nic)
    item.hashfct3(nic)
    item.hashfct4(nic)
    item.hashfct5(nic)
    item.hashfct6(nic)
    data = []
    choice = input("Do you want to add more items? Enter True or False: ")
    if(choice == str(True)):
        number = input("Enter number of items to add: ")
        for number in range(int(number)):
            v = input("Enter Sensor full name: ")
            data.append(v)
        print(data)
        print(len(data))
        list = []
        for dt in data:
            list.append(dt[-6:])
        
        count = 0

        for l in list:
            bool = item.addItem(l)
            if bool == True:
                count = count+1
            else:
                print(f'Can not add sensor - {l} in the tables as they already exist.') 

        if bool == True:
            print(f'New Network. Size is {count} after adding NICs: {" and ".join(data)}')

    else:
        print("Program completes here.")
