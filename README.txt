Hello Guys!
The following is a python code for automating task of hadoop cluster formation for both HDFS and Map Reduce build on a red hat platform.
Prerequisites before running this code-
* All the systems in which the following code is been run must be in a network and it is appreciated to note the IP of all the systems.
* Your python library should have paramiko module and your red hat base OS should have sshpass intalled.
* The one system on which the code is being run is a client machine and should have access of passwords of other systems.The client machine should have java jdk7(8) and haddop1(2) rpm installed on their desktop.


My repository also have my own build mapper and reducer python programs which can be used to test the map-reduce cluster. These programs are run on a random dataset(this file is also attached) which has some random company codes(made by me) followed by product they sold at a particular point of time. My mapper program runs on this file and filters a product from it(like smartphones here) and reducer program must run on output of mapper program and counts the results that a particular comapny sold how many smartphones.This is used to illustrate the fact that Hadoop MapReduce is used for OLAP operations only. 