import os
os.system("tput setaf 3")
print("\t\t\tWELCOME TO DOCKER")
print("\t\t\t------------------")
os.system("espeak-ng welcome_to_docker")
os.system("tput setaf 2")
os.system("espeak-ng Starting_docker_services")
print("Starting docker services...")
os.system("systemctl start docker")
print("List of all the existing container")
os.system("espeak-ng List_of_all_the_existing_container")
os.system("docker ps -a")
print('''
Press 1 to create a new container
Press 2 to run your existing container
Press 3 to delete your container''')
while True:
	i=int(input("Please enter your choice:"))
	if i==1:
		a=input("Please enter your container name:")
		b=input("please enter your conntainer img name:")
		os.system("docker run -it --name {} -p 99:80 {}".format(a,b))
	elif i==2:
		c=input("please enter your container name/ID:")
		os.system("docker start {}".format(c))
		os.system("docker attach {}".format(c))
	elif i==3:
		print('''
Press 1 to delete a perticular container
Press 2 to delete all container''')
		i=int(input("Please enter your choice:"))
		if i==1:
			d=input("Please enter container Name/ID which you want to delete? :")
			os.system("docker rm {}".format(d))
		elif i==2:
			os.system("docker ps -a -q")
			print("Start deleting")
			os.system("docker rm `docker pa --a -q`")
