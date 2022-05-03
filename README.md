# hashing-NIC-addressses

Group members:

1. Shivangi Shakya shivangishakya@csu.fullerton.edu
2. Saoni Mustafi saonimustafi@csu.fullerton.edu
3. Nick Bidler Nbidler@csu.fullerton.edu

Communication is paramount on sensor networks and it relies on grouping sensors into clusters, and providing code to be executed distributively at the sensors to maximize coverage and extend lifetime of the network, thus minimizing energy consumption for transmission. Clustering is not only important for communication but also for other distributed algorithms.

We are given a sensor network with a fairly small number of MAC addresses, one for each sensor, and we would like to group the sensors to form several clusters of sensors based on their MAC address. A MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller (NIC) for a network. A MAC Address is often referred to as a hardware address. The MAC addresses are unique and they are used for communication between components or computers. MAC addresses take the form of alphanumeric numbers in hexadecimal format arranged in groups of 2 (usually) separated by a colon.

This  project is about reading a fairly small number of distinct Network Interface Controllers (NICs), each being a 6-digit number in hexadecimal, and deciding which digit among the six gives the best balanced distribution of the NICs.

<b>Essentially, the objective is to find an algorithm to functions like a Bucket Sort, such that when inputs are evenly distributed, any non-insertion operations have an average O(n) time class.</b>

For example 1:

![image](https://user-images.githubusercontent.com/9604309/166574810-b169a946-0361-4ad9-ad99-b805420a3189.png)
