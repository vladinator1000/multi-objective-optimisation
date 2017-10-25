Description of the Next Release Problem (NRP) Instance File
Jifeng Xuan
School of Software, Dalian University of Technology
E-mail: xuan(at)mail.dlut.edu.cn
Nov. 16, 2011

This document is to show the details of the NRP instance file.
Each file indicates a group of instances. To generate an NRP instance, a cost ratio should be pointed out. The typical value of the cost ratio in these instances (realistic-nrp.zip) may be 0.3 or 0.5 (Do not use 0.7 since the cost ratio of 0.7 may lead to a very easy instance). Based on a cost ratio and an instance file, an NRP instance can be generated. 

1. The predefined budget bound is calculated as the cost ratio multiplied the sum of all the requirements costs. 
2. The format of this file is as follows. An example can be found as example.txt .

If you are interested in the generation of instances, please check [1] for details.


1 (Exact number, 1) 
Number of requirements in Level 1, t1
Costs of requirements in Level 1 (the number is t1)
0 (Exact number, 0) 
Number of customers, n
Profit of Customer1	Number of requests by Customer1, q1	Requirements List (the size is q1)
Profit of Customer2	Number of requests by Customer2, q2	Requirements List (the size is q2)
бн
Profit of CustomerN	Number of requests by CustomerN, qN	Requirements List (the size is qN)

3. All the values in a file is 1-base value. For example, the Ids of requirements are 1, 2, бн, m.
4. The separating character in the instance files is one space mark or one line break mark.


References
[1] J. Xuan, H. Jiang, Z. Ren, Z. Luo, "Solving the Large Scale Next Release Problem with a Backbone Based Multilevel Algorithm," IEEE Transactions on Software Engineering, 31 Aug. 2011, doi: 10.1109/TSE.2011.92. <http://doi.ieeecomputersociety.org/10.1109/TSE.2011.92>


