# hashing-NIC-addressses

Group members:

1. Shivangi Shakya shivangishakya@csu.fullerton.edu
2. Saoni Mustafi saonimustafi@csu.fullerton.edu
3. Nick Bidler Nbidler@csu.fullerton.edu

Communication is paramount on sensor networks and it relies on grouping sensors into clusters, and providing code to be executed distributively at the sensors to maximize coverage and extend lifetime of the network, thus minimizing energy consumption for transmission. Clustering is not only important for communication but also for other distributed algorithms.

We are given a sensor network with a fairly small number of MAC addresses, one for each sensor, and we would like to group the sensors to form several clusters of sensors based on their MAC address. A MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller (NIC) for a network. A MAC Address is often referred to as a hardware address. The MAC addresses are unique and they are used for communication between components or computers. MAC addresses take the form of alphanumeric numbers in hexadecimal format arranged in groups of 2 (usually) separated by a colon.

This  project is about reading a fairly small number of distinct Network Interface Controllers (NICs), each being a 6-digit number in hexadecimal, and deciding which digit among the six gives the best balanced distribution of the NICs.

<b>Essentially, the objective is to find an algorithm to functions like a Bucket Sort, such that when inputs are evenly distributed, any non-insertion operations have an average O(n) time class.</b>

Also, please note that the naming conventions for the different hash tables is "HashTable<digit><network number>" - so the hash table based on the second digits of the third network would be "HashTable23"

The first thing the program does is to initilize one ItemCollection object for each network: each ItemCollection will hold all the HashTables and member functions for its assigned network.

Example 1: demonstrating that the program output for hashed inputs and outputs is the same as the sample outputs
Shown in the screenshots below, the example calls a function that returns the decimal digit at the appropriate location, i.e. hashfct4() returns the decimal value of the hex digit at position 4

![image](https://user-images.githubusercontent.com/9604309/166585785-19253df8-dab4-4f81-95b6-701a17049a7e.png)

![image](https://user-images.githubusercontent.com/9604309/166596241-b55ed4d6-c5e8-4187-bfe0-45b205b06189.png)

After this, the program allows the user to manually enter a network: the number of NICs to be entered, followed by the 6-digit NICs.

![image](https://user-images.githubusercontent.com/9604309/166613442-7ccff116-a72c-4923-b396-e96e05e3d4f0.png)
