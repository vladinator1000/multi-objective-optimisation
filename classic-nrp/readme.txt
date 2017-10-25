Description of the Next Release Problem (NRP) Instance File
Jifeng Xuan
School of Software, Dalian University of Technology
E-mail: xuan(at)mail.dlut.edu.cn
Nov. 16, 2011

This document is to show the details of the NRP instance file.
Each file indicates a group of instances. To generate an NRP instance, a cost ratio should be pointed out. The typical value of the cost ratio may be 0.3, 0.5, or 0.7. Based on a cost ratio and an instance file, an NRP instance can be generated. 

If you are interested in the generation of instances, please check [1] for details.


1. The predefined budget bound is calculated as the cost ratio multiplied the sum of all the requirements costs. 
2. The format of this file is as follows. An example can be found as example.txt .

Level of requirements, t
Number of requirements in Level 1, t1
Costs of requirements in Level 1 (the number is t1)
Number of requirements in Level 2, t2
Costs of requirements in Level 2 (the number is t2)
¡­
Number of requirements in Level t, tt
Costs of requirements in Level t (the number is tt)
Number of dependencies, d
Id of RequirementA1	Id of RequirementB1 
Id of RequirementA2	Id of RequirementB2
¡­
Id of RequirementAd	Id of RequirementBd
Number of customers, n
Profit of Customer1	Number of requests by Customer1, q1	Requirements List (the size is q1)
Profit of Customer2	Number of requests by Customer2, q2	Requirements List (the size is q2)
¡­
Weight of CustomerN	Number of requests by CustomerN, qN	Requirements List (the size is qN)

3. All the values in a file is 1-base value. For example, the Ids of requirements are 1, 2, ¡­, m.
4. The separating character in the instance files is one space mark or one line break mark.

The details of instance generation rules can also be found in [2].

References
[1] J. Xuan, H. Jiang, Z. Ren, Z. Luo, "Solving the Large Scale Next Release Problem with a Backbone Based Multilevel Algorithm," IEEE Transactions on Software Engineering, 31 Aug. 2011, doi: 10.1109/TSE.2011.92. <http://doi.ieeecomputersociety.org/10.1109/TSE.2011.92>

[2] A. Bagnall, V. Rayward-Smith, and I. Whittley, ¡°The Next Release Problem,¡± Information and Software Technology, vol. 43, no.14, pp. 883-890, Dec. 2001, doi:10.1016/S0950-5849(01)00194-X. 
