# hashing-NIC-addressses

Group members:

1. Shivangi Shakya shivangishakya@csu.fullerton.edu
2. Saoni Mustafi saonimustafi@csu.fullerton.edu
3. Nick Bidler Nbidler@csu.fullerton.edu

Communication is paramount on sensor networks and it relies on grouping sensors into clusters, and providing code to be executed distributively at the sensors to maximize coverage and extend lifetime of the network, thus minimizing energy consumption for transmission. Clustering is not only important for communication but also for other distributed algorithms.

We are given a sensor network with a fairly small number of MAC addresses, one for each sensor, and we would like to group the sensors to form several clusters of sensors based on their MAC address. A MAC address (Media Access Control address) is a unique identifier assigned to a network interface controller (NIC) for a network. A MAC Address is often referred to as a hardware address. The MAC addresses are unique and they are used for communication between components or computers. MAC addresses take the form of alphanumeric numbers in hexadecimal format arranged in groups of 2 (usually) separated by a colon.

This  project is about reading a fairly small number of distinct Network Interface Controllers (NICs), each being a 6-digit number in hexadecimal, and deciding which digit among the six gives the best balanced distribution of the NICs.

<b>Essentially, the objective is to find an algorithm that functions similarly to a Bucket Sort, such that when inputs are evenly distributed in a hash table with chaining, any non-insertion operations have an average O(n) time class.</b>

The first thing the program does is to initialize one ItemCollection object for each network: each ItemCollection will hold all the HashTables and member functions for its assigned network.

Example 1: demonstrating that the program output for hashed inputs and outputs is the same as the sample outputs
Shown in the screenshots below, the example calls a function that returns the decimal value of the hex digit at the appropriate location, i.e., hashfct4() returns the decimal value of the hex digit at position 4.

![image](https://user-images.githubusercontent.com/9604309/166585785-19253df8-dab4-4f81-95b6-701a17049a7e.png)

![image](https://user-images.githubusercontent.com/9604309/166596241-b55ed4d6-c5e8-4187-bfe0-45b205b06189.png)

Example 2: demonstrating that the program evaluation to find the most even distribution is the same as the sample cases
After this, the program allows the user to manually enter a network: the number of NICs to be entered, followed by the 6-digit NICs.

![image](https://user-images.githubusercontent.com/9604309/166613442-7ccff116-a72c-4923-b396-e96e05e3d4f0.png)

This creates a "network" and runs the BestHashing<network number> function, which finds the smallest and largest entry on each hash table, takes the difference of each, and returns the hash table with the smallest difference.
  
![image](https://user-images.githubusercontent.com/9604309/166616146-2c99049c-a6ef-416c-8001-3cf210ea99c8.png)

![image](https://user-images.githubusercontent.com/9604309/166616163-ea2b71f9-a322-43aa-a6db-6a27736d82b1.png)

Example 3: showing the network can be interacted with in a way that changes the Best Hashing calculation
  
![image](https://user-images.githubusercontent.com/9604309/166616450-8b4a1d8a-744e-4669-bbe4-35dcbf9a3c40.png)
```
Before deletion (result of 2): 
|123456 | 234567 | 345678 | 456789 | 56789A | 6789AB | 789ABC
|89ABCD | 9ABCDE | ABCDEF | BCDEF0 | CDEF01 | DEF012 | EF0123
|F01234 | 543210 | 43210F | 3210FE | 210FED | 10FEDC | FEDCBA
|EDCBA9 | DCBA98 | CBA987 | BA9876 | A98765 | 987654 | 876543
|765432 | 654321 | 776543 | 887654 | 998765 | 110987 | 221098
|332109 | 443210
```
```
After deletion:
|123456 | 234567 | 345678 | 456789 | 56789A | 6789AB | 789ABC
|89ABCD | 9ABCDE | ABCDEF | BCDEF0 | CDEF01 | DEF012 | EF0123
|F01234 | 543210 | 43210F | 3210FE |        | 10FEDC | FEDCBA
|EDCBA9 | DCBA98 | CBA987 | BA9876 | A98765 | 987654 | 876543
|765432 | 654321 | 776543 | 887654 | 998765 |        | 221098
|332109 | 443210
```
digit count at positions:

| Count of: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
| --------- |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pos. 1    | 0 | 2 | 2 | 3 | 4 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 2 |
| Pos. 2    | 2 | 0 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 1 |
| Pos. 3    | 1 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 2 |
| Pos. 4    | 2 | 3 | 3 | 1 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 |
| Pos. 5    | 3 | 3 | 2 | 2 | 1 | 3 | 3 | 2 | 2 | 3 | 2 | 2 | 1 | 2 | 1 | 2 |
| Pos. 6    | 2 | 2 | 2 | 2 | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 1 | 2 | 1 | 2 | 2 |

As shown by the above table, position 1 and 2 have a maximum difference of 3, while 3 through 6 have a difference of 2 - as tie-breaker, the first position encountered is the one that is used for the hash table. In this case, the result is position 3, which matches the program's output.
