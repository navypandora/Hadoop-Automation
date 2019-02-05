#!/usr/bin/python2
import os
import getpass
import paramiko

ip = raw_input("Enter ip address: ")
username = raw_input("Enter Username: ")
password = raw_input("Enter the password of {}: ".format(ip))
junk = """<?xml version="1.0"?>\n\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> \n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n"""

while True: 
	os.system("tput setaf 4")
	print "\t\t\t\t Welcome to the Hadoop Installation"
	os.system("tput setaf 0")
	print"""
	Press 1: To install jdk
	Press 2: To make it permanent
	Press 3: To install hadoop
	Press 4: To setup HDFS
	Press 5: To setup MapReduce
	Press 6: To setup Client
	Press 7: Exit \n\n """
	i=raw_input("Enter you choice: ")
	if int(i)==1:
		os.system("sshpass -p {0} scp /root/Desktop/jdk.rpm {1}:/tmp/jdk.rpm".format(password,ip))
		os.system("sshpass -p {0} ssh {1} rpm -ivh /tmp/jdk.rpm".format(password,ip))
		os.system("sshpass -p {0} ssh {1} export JAVA_HOME=/usr/java/jdk1.7.0_79".format(password,ip))
		os.system("sshpass -p {0} ssh {1} export PATH=/usr/java/jdk1.7.0_79/bin/:$PATH".format(password,ip))
	elif int(i)==2:
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
		ftp = ssh.open_sftp()
		file=ftp.file('/root/.bashrc',"a",-1)
		file.write("""export JAVA_HOME=/usr/java/jdk1.7.0_79/\nexport PATH+/usr/java/jdk1.7.0_79/bin/:$PATH\n""")
		file.flush()
		ftp.close()
		ssh.close()
	elif int(i)==3:
		os.system("sshpass -p {0} scp /root/Desktop/hadoop.rpm {1}:/tmp/hadoop.rpm".format(password,ip))
		os.system("sshpass -p {0} ssh {1} rpm -ivh /tmp/hadoop.rpm --replacefiles".format(password,ip))
	elif int(i)==4:
		print""" Setting up HDFS

		Press 1: To Setup Namenode
		Press 2: To Setup Datanode
		Press 3: Exit \n\n"""
		m_ip = raw_input("Enter Master's IP:")
		j=raw_input("Enter your choice: ")
		while True:
			if int(j)==1:
				print"""
				Press 1: To configure Namenode
				Press 2: To create folder
				Press 3: format namenode folder 
				Press 4: firewall off
				Press 5: To start Service
				Press 6: Check namenode connections
				Press 7: Exit \n\n """
				k=raw_input("Enter your choice: ")
		
				if int(k)==1:
					ssh=paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
					ftp = ssh.open_sftp()
					file=ftp.file('/etc/hadoop/hdfs-site.xml',"w")			
					file.write("""{0}<property>
<name>dfs.name.dir</name>
<value>/master</value>
</property>

</configuration>""".format(junk))
					file=ftp.file('/etc/hadoop/core-site.xml',"w")			
					file.write("""{0}<property>
<name>fs.default.name</name>
<value>hdfs://{1}:9001</value>
</property>

</configuration>""".format(junk,m_ip))
					file.flush()
					ftp.close()
					ssh.close()
				elif int(k)==2: 
					os.system("sshpass -p {0} ssh {1} mkdir /master ".format(password,ip))
				elif int(k)==3:
					os.system("sshpass -p {0} ssh {1} hadoop namenode -format".format(password, ip))
				elif int(k)==4:
					os.system("sshpass -p {0} ssh {1} iptables -F".format(password,ip))
				elif int(k)==5:
					os.system("sshpass -p {0} ssh {1} hadoop-daemon.sh start namenode".format(password,ip))
				elif int(k)==6:
					os.system("sshpass -p {0} ssh {1} hadoop dfsadmin -report".format(password,ip))
				elif int(k)==7:
					break
		
			elif int(j)==2:
				print"""
				Press 1: To configure Datanode
				Press 2: Make data folder
				Press 3: To turn off firewall
				Press 4: To start service
				Press 5: exit \n\n """
				l = raw_input("Enter your Choice: ")
				if int(l)==1:
					ssh=paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
					ftp = ssh.open_sftp()
					file=ftp.file('/etc/hadoop/hdfs-site.xml',"w")
					file.write("""{0}<property>
<name>dfs.data.dir</name>
<value>/data</value>
</property>

</configuration>""".format(junk))
					file=ftp.file('/etc/hadoop/core-site.xml',"w")
					file.write("""{0}<property>
<name>fs.default.name</name>
<value>hdfs://{1}:9001</value>
</property>

</configuration>""".format(junk,m_ip))
					file.flush()
					ftp.close()
					ssh.close()
				elif int(l)==2: 
					os.system("sshpass -p {0} ssh {1} mkdir /data".format(password,ip))
				elif int(l)== 3:
					os.system("sshpass -p {0} ssh {1} iptables -F".format(password,ip))
				elif int(l)== 4:
					os.system("sshpass -p {0} ssh {1} hadoop-daemon.sh start datanode".format(password,ip))
				elif int(l)==5:
					break


			
			elif int(j)==3:
				break

	elif int(i)==5:
			print"""
			Press 1: To setup Job Tracker
			Press 2: To setup Task Tracker
			Press 3: Exit
			"""		
			j_ip= raw_input("Enter Job Tracker's IP: ")
			m_ip= raw_input("Enter Master's IP: ")
			n= raw_input("Enter Your Choice: ")
			while True:	
				if int(n)==1:
 					print"""
					Press 1: To configure Job Tracker
					Press 2: To Flush IP
					Press 3: Start Service
					Press 4: Exit\n\n
					"""
					o=raw_input("Enter your choice: ")
		
					if int(o)==1:
						ssh=paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())	
						ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
						ftp = ssh.open_sftp()
						file=ftp.file('/etc/hadoop/mapred-site.xml',"w")	
						file.write("""{0}<property>
<name>mapred.job.tracker</name>
<value>{1}:9002</value>
</property>

</configuration>""".format(junk,j_ip))
						file=ftp.file('/etc/hadoop/core-site.xml',"w")	
						file.write("""{0}<property>
<name>fs.default.name</name>
<value>hdfs://{1}:9001</value>
</property>

</configuration>""".format(junk,m_ip))
						file.flush()
						ftp.close()
						ssh.close()
					elif int(o)==2: 
						os.system("sshpass -p {0} ssh {1} iptables -F".format(password,ip))
					elif int(o)==3:
						os.system("sshpass -p {0} ssh {1} hadoop-daemon.sh start jobtracker".format(password,ip)	)
					elif int(o)==4:
						break
	
			
				elif int(n)==2:
					print"""
					Press 1: To configure Task Tracker
					Press 2: Flush IP
					Press 3: Start Service
					Press 4: Exit\n\n"""
					p= raw_input("Enter your choice: ")

					if int(p)==1:
 						ssh=paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
						ftp = ssh.open_sftp()
						file=ftp.file('/etc/hadoop/mapred-site.xml',"w")	
						file.write("""{0}<property>
<name>mapred.job.tracker</name>
<value>{1}:9002</value>
</property>

</configuration>""".format(junk,j_ip))
						file.flush()
						ftp.close()
						ssh.close()
					elif int(p)==2:
						os.system("sshpass -p {0} ssh {1} iptables -F".format(password,ip))
					elif int(p)==3: 
						os.system("sshpass -p {0} ssh {1} hadoop-daemon.sh start tasktracker".format(password,ip))
					elif int(p)==4:
						break
				elif int(n)==3:
					break

	elif int(i)==6:
		
		m_ip = raw_input("Enter Masters IP: ")
		j_ip = raw_input("Enter Job Tracker's IP: ")
		while True:
			print """
			Press 1: To configure Client
			Press 2: To exit\n\n"""
			m = raw_input("Enter your choice:")					
		
	
			if int(m)==1: 
				ssh=paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect('{}'.format(ip), username='{}'.format(username), password= '{}'.format(password))
				ftp = ssh.open_sftp()
				file=ftp.file('/etc/hadoop/core-site.xml',"w")
				file.write("""{0}<property>
<name>fs.default.name</name>
<value>hdfs://{1}:9001</value>
</property>

</configuration>""".format(junk,m_ip))
				file.flush()
				file=ftp.file('/etc/hadoop/mapred-site.xml',"w")	
				file.write("""{0}<property>
<name>mapred.job.tracker</name>
<value>{1}:9002</value>
</property>

</configuration>""".format(junk,j_ip))
				file.flush()
				ftp.close()
				ssh.close()
			elif int(m)==2:
				break
	elif int(i)==7:
		exit()
raw_input()