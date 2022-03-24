HashTables = [[[] for i in range(16)] for j in range(6)]

def Hashing(value):
    for i in range(6):
        HashTables[i][int(value[i], 16)].append(value)

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
            
def print_hash(hashTables):
    for i in range(6):
        print("HashTable" + str(i))
        display_hash(hashTables[i])


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
    
    for vl in list:
        Hashing(vl)
    
    i = 1
    for table in HashTables:
        diff = get_range(table)
        dict[i] = diff
        i = i+1

    print_hash(HashTables)
    print(dict)

    key = min(dict, key = dict.get)
    print(f'Balanced HashTable - clustering based on {key}nd digit')
