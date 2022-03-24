class HashTables:

    def __init__(self, data) -> None:
        self.numOfDigits = len(data[0])
        self.hashTables = [[[] for i in range(16)] for j in range(self.numOfDigits)]

    def generateHash(self, data):
        for val in data:
            for i in range(self.numOfDigits):
                self.hashTables[i][int(val[i], 16)].append(val)
        self.display_hashes()
        self.get_range()
    
    def display_hashes(self):
        for i in range(self.numOfDigits):
            for j in range(len(self.hashTables[i])):
                print(j, end = " ")
                for k in self.hashTables[i][j]:
                    print("-->", end = " ")
                    print(k, end = " ")
                print()

    def get_range(self):
        
        dict = {}
        j = 1
        for table in self.hashTables:
            maxcount = 0
            mincount = 100
            for i in table:
                count = len(i)
                # print(f'j = {j}, count = {len(i)}')
                
                if count < mincount:
                    mincount = count
                
                if count > maxcount:
                    maxcount = count
            
            diff = maxcount - mincount
            # print(f'j = {j} , maxcount = {maxcount}, mincount = {mincount}')
            dict[j] = diff
            j = j+1
        print(dict)
        key = min(dict, key = dict.get)
        print(f'Balanced HashTable - clustering based on {key}nd character.')
        


# HashTables = [[[] for i in range(16)] for j in range(6)]

# def Hashing(value):
#     for i in range(6):
#         HashTables[i][int(value[i], 16)].append(value)

# def display_hash(HashTable):
#     for i in range(len(HashTable)):
#         print(i, end = " ")
    
#         for j in HashTable[i]:
#             print("-->", end = " ")
#             print(j, end = " ")
#         print()

# def get_range(HashTable):
#     maxcount = 0
#     mincount = 100
#     for i in HashTable:
#         count = len(i)
#         if count < mincount:
#             mincount = count
        
#         if count > maxcount:
#             maxcount = count
    
#     diff = maxcount - mincount
#     # print(f'Difference = {diff}')
#     return diff
            
# def print_hash(hashTables):
#     for i in range(6):
#         print("HashTable" + str(i))
#         display_hash(hashTables[i])


if __name__ == '__main__':
    flname = input("Enter the data file you want to process: ")
    fl = open(flname, "r")
    datainput = fl.read()
    datainput = datainput.split('\n')
    fl.close()
    list = []
    for vl in datainput:
        list.append(vl[-6:])
    print(list)
    Tab = HashTables(list)
    Tab.generateHash(list)

    # i = 1
    # for table in HashTables:
    #     diff = get_range(table)
    #     dict[i] = diff
    #     i = i+1

    # print_hash(HashTables)
    # print(dict)

    # key = min(dict, key = dict.get)
    # print(f'Balanced HashTable - clustering based on {key}nd digit')
