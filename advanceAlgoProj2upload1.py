HashTable1 = [[] for _ in range(16)]
HashTable2 = [[] for _ in range(16)]
HashTable3 = [[] for _ in range(16)]
HashTable4 = [[] for _ in range(16)]
HashTable5 = [[] for _ in range(16)]
HashTable6 = [[] for _ in range(16)]

def Hashing(value):
    HashTable1[int(value[0], 16)].append(value)
    HashTable2[int(value[1], 16)].append(value)
    HashTable3[int(value[2], 16)].append(value)
    HashTable4[int(value[3], 16)].append(value)
    HashTable5[int(value[4], 16)].append(value)
    HashTable6[int(value[5], 16)].append(value)
    
    
def display_hash(HashTable):
    for i in range(len(HashTable)):
        print(i, end = " ")
    
        for j in HashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
            
        print()

def get_range(HashTable):
    maxcount = 0
    mincount = 100
    for i in HashTable:
        count = len(i)
        if count < mincount:
            mincount = count
        
        if count > maxcount:
            maxcount = count
    
    diff = maxcount - mincount
    # print(f'Difference = {diff}')
    return diff
            
def print_hash():
    print("HashTable1")
    display_hash(HashTable1)
    print("HashTable2")
    display_hash(HashTable2)
    print("HashTable3")
    display_hash(HashTable3)
    print("HashTable4")
    display_hash(HashTable4)
    print("HashTable5")
    display_hash(HashTable5)
    print("HashTable6")
    display_hash(HashTable6)


if __name__ == '__main__':
    flname = input("Enter the data file you want to process: ")
    fl = open(flname, "r")
    datainput = fl.read()
    datainput = datainput.split('\n')
    print(datainput)
    fl.close()
    dict = {}
    list = []

    for val in datainput:
        list.append(val[-6:])
    print(list)

    for val in list:
        Hashing(val)

    i = 1
    for table in [HashTable1,HashTable2,HashTable3,HashTable4,HashTable5,HashTable6]:
        diff = get_range(table)
        dict[i] = diff
        i = i+1

    print_hash()
    print(dict)

    key = min(dict, key = dict.get)
    print(f'Balanced HashTable - clustering based on {key}nd digit')
