import subprocess
import pyfiglet as pyg
import socket
i=0
while(i<100):
	res = pyg.figlet_format("Welcome to Lokimux", font = "digital")
	print(res)
	print("""
1.pwd
2.ls
3.cmatrix
4.mc
5.python
6.sl
7.cacafire
8.zphisher
9.server
10.ipscanner tool
_____________________________________________________
""")
	a=input("Enter : ")
	if(a==""):
		print("Enter something")
	elif (a=="1"):
		subprocess.call("pwd")
	elif (a=="2"):
		subprocess.call("ls")
	elif (a=="3"):
		subprocess.call("cmatrix")
	elif (a=="4"):
		subprocess.call("mc")
	elif (a=="5"):
		subprocess.call("python")
	elif (a=="6"):
		subprocess.call("sl")
	elif (a=="7"):
		subprocess.call("cacafire")
	elif (a=="8"):
		subprocess.call("zphisher")
	elif (a=="9"):
		subprocess.call("apachectl")
	elif (a=="10"):
		res = pyg.figlet_format("Welcome to IpScanner", font = "digital")
		print(res)
		print("                                     by Loki")

		def get_ip_address(website_name):
    			try:
        			ip_address = socket.gethostbyname(website_name)
        			return ip_address
    			except socket.gaierror:
        			print("Invalid website name or network not found")
        			return None

		website_name = input("Enter Website Name :")
		ip_address = get_ip_address(website_name)

		if ip_address:
    			print(f"The IP address of {website_name} is {ip_address}")	
		else:
			print("invaid input")
			i+=1

	print("-----------------------------------------------------")