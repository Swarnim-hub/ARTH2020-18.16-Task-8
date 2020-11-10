import os
import getpass
import pyaudio
import speech_recognition as sr
r=sr.Recognizer()
os.system("tput setaf 3")
print("\t\t\tWelcome To My Menu!!!")
os.system("espeak-ng Welcome__To__My__Menu")
os.system("tput setaf 7")
print("*------------------------------------------------------------------------------*")
os.system("espeak-ng before_entering")
os.system("espeak-ng please__tell__me__your__password")
os.system("tput setaf 5")
os.system("espeak-ng i_am_listening")
with sr.Microphone() as source:
    print("I am listening...")
    x=r.listen(source)
    print("Speech done")
    password=r.recognize_google(x)
if (password=='hello'):
    os.system("espeak-ng Where_do_you_want_to_login__this_menu") 
    os.system("espeak-ng local________or________remote")
    os.system("espeak-ng I_am_listening")
    with sr.Microphone() as source:
        print("I am listening...")
        choice=r.listen(source)
        print("Speech done")
    login=r.recognize_google(choice)
    while True:
        if(login=="local"):
            print('''
	       [1] View date 
	       [2] View calender
	       [3] Run  Firebox
	       [4] Open your text editor
	       [5] Configure Docker Container
               [6] Configure Hadoop Cluster
               [7] Configure AWS CLI
               [8] Configure Cloud Front
               [9] Configure webserver
               [10] EXIT''')
            os.system("espeak-ng Please_tell__me__your__requirement")
            print(" Please_tell__me__your__requirement")
            os.system("espeak-ng i__am__listening")
            with sr.Microphone() as source:
                print("I am listening...")
                l=r.listen(source)
                print("Speech done")
            login_choice=r.recognize_google(l)
            if ( ("date" in login_choice) or ("run date" in  login_choice) or ("show me the date" in  login_choice) or ("view date" in  login_choice)):
                os.system("date")
            elif(("calender " in login_choice) or ("run calender " in  login_choice) or ("show me the calender " in  login_choice) or ("view calender" in  login_choice)):
                os.system("cal")
            elif (("firefox" in login_choice) or ("run firefox" in  login_choice) or ("web browser " in  login_choice) or ("open web browser" in  login_choice)):
                os.system("firefox")
            elif (("text editor" in login_choice) or ("notepad" in  login_choice) or ("gedit " in  login_choice)): 
                os.system("gedit")
            elif (("start docker " in login_choice) or ("docker" in  login_choice) or ("container " in  login_choice) or ("docker container" in login_choice)):
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
                            os.system("docker rm `docker pa --a -q` ")
            elif ( ("webserver" in login_choice) or ("apache webserver" in  login_choice) or ("httpd" in  login_choice)):
                os.system("date")
                os.system("espeak-ng installing_h_t_t_p_d")
                os.system("yum install httpd")
                os.system("espeak-ng opening_h_t_m_l_directory")
                os.system("cd /var/www/html")
                os.system("espeak-ng opening_gedit")
                os.system("cd /var/www/html/ && gedit myweb.html")
                os.system("espeak-ng start__h_t_t_p_d_service")
                os.system("systemctl start httpd")
                os.system("ifconfig enp0s3")
                os.system("espeak-ng please_copy_the_ip_address____")
                os.system("espeak-ng opening_firefox")
                os.system("firefox")
            elif ( ("cloud service" in login_choice) or ("amazon cloud  " in  login_choice) or ("aws" in  login_choice)):
                os.system("date")
                print("Login  details")
                os.system("aws configure")

                print("Choose a choice")
                print(" 1. EC2")
                print(" 2. EBS")
                print(" 3. IAM")
                print(" 4. S3")
                i = input("Choice: ")

                if int(i)==1:
                    print(" Choose an option")
                    print(" 1. Launch an instance")
                    print(" 2. Start an instance")
                    print(" 3. Stop an instance")
                    print(" 4. Attach EBS")
                    print(" 5. Create Key")
                    print(" 6. Desribe key")
                    j = input("Choice: ")
                    if int(j)==1:
                        print("Operating system :")
                        print("1. Amazon linux")
                        print("2. Redhat Linux")
                        print("3. Widnows")
                        ch=input("Choice:")
                        if int(ch)==1:
                            osami="ami-0e306788ff2473ccb"
                        elif int(ch)==2:
                            osami="ami-052c08d70def0ac62"
                        elif int(ch)==3:
                            osami="ami-0b2f6494ff0b07a0e"
                        count=input("Count: ")
                        sg=input("Security Group id: ")
                        ec2key=input("Key for authentication:")
                        os.system("aws ec2 run-instances --image-id    {} --instance-type    t2.micro --count {} --subnet-id subnet-329ae47e --security-group-ids {} --key-name {}".format(osami,count,sg,ec2key))
                elif int(j)==2:
                    ec2id=input("Instance Id:")
                    os.system("aws ec2 start-instances --instance-ids {}".format(ec2id))
                elif int(j)==3:
                    ec2id=input("Instance Id:")
                    os.system("aws ec2 stop-instances --instance-ids {}".format(ec2id))
                elif int(j)==4:
                    ec2id=input("Instance Id:")
                    volumeid=input("Volume Id:")
                    os.system ("aws ec2 attach-volume --volume-id {} --instance-id {} -device /dev/sdf("")".format(volumeid,ec2id))
                elif int(j)==5:	
                     key=input ("Key name:")
                     os.system("aws ec2 create-key-pair --key-name {}".format(key)) 
                elif int(j)==6:
                     os.system("aws ec2 describe-key-pairs") 
                elif int(i)==2:
                    print(" Choose an option")
                    print(" 1. Launch an EBS volume")
                    print(" 2. Attach an EBS volume")
                    print(" 3. Delete Volume")
                    j = input("Choice: ")
                    if int(j)==1:
                        size=input("Size:") 
                        os.system("aws ec2 create-volume  --volume-type gp2  --size {} --availability-zone ap-south-1b".format(size))
                    elif int(j)==2:
                        ec2id=input("Instance Id:")
                        volumeid=input("Volume Id:")
                        os.system ("aws ec2 attach-volume --volume-id {} --instance-id {} -device /dev/sdf("")".format(volumeid,ec2id))
                    elif int(j)==3:
                        volumeid=input("Volume Id:")
                        os.system ("aws ec2 attach-volume --volume-id {}".format(volumeid))
                elif int(i)==3:
                    print(" Choose an option")
                    print(" 1. Create a user")
                    print(" 2. Control protocols for user")
                elif int(i)==4:
                    print(" Choose an option")
                    print(" 1. Launch a bucket")
                else:
                    print("Invalid Option!")
            elif ("cloud front" in local_choice):
                print("press1: to login to your AWS Account")
                r=input(": ")
                if int(r)==1:
                    r=os.system("aws configure")
                    os.system("tput setaf 3")
                    print("\t\t\tWELCOME TO YOUR AWS ACCOUNT")
                    print("\t\t\t\t------------")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    press1 : to create an S3 bucket
                    press2 : to upload file
                    press3 : to allow public access
                    press4 : to create cloudfront distribution
                    """)
                    os.system("tput setaf 7")
                    ch=input("Enter your choice: ")
                    if int(ch)==1:
                        buckname=input("Bucket name: ")
                        regname=input("Region: ")
                        os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(buckname,regname,regname))
                    elif int(ch)==2:
                        filename=input("Enter the filename: ")
                        s3buck=input("Enter the s3_bucket_name: ")
                        os.system("aws s3 cp {} s3://{}/{}".format(filename,s3buck,filename))
                    elif int(ch)==3:
                        fn=input("Enter the File_name: ")
                        s3b=input("Enter the s3_bucket_name: ")
                        os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(s3b,fn))
                    elif int(ch)==4:
                        odomain=input("Enter the s3_bucket_name: ")
                        fn1=input("Enter the filename: ")
                        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(odomain,fn1))
            elif (("hadoop cluster" in login_choice) or ("hadoop configuration" in  login_choice) or ("apache hadoop configure" in  login_choice)):
                os.system("")   
       	    elif (("close" in login_choice) or ("exit" in  login_choice)):
                os.system("exit")
            else:
                print("Sorry! Your Entry is not valid")
            
        else:
           
            ip=input("Enter Your IP Here :")
            print(ip)
            os.system("ssh {}".format(ip))
            os.system("espeak-ng Welcome")
            print('''
	       [1] View date 
	       [2] View calender
	       [3] Run  Firebox
	       [4] Open your text editor
	       [5] Configure Docker Container
               [6] Configure Hadoop Cluster
               [7] Configure AWS CLI
               [8] Configure Cloud Front
               [9] Configure webserver
               [10] EXIT''')
            os.system("espeak-ng Please_tell__me__your__requirement")
            print(" Please_tell__me__your__requirement")
            os.system("espeak-ng i__am__listening")
            with sr.Microphone() as source:
                print("I am listening...")
                l=r.listen(source)
                print("Speech done")
            login_choice=r.recognize_google(l)
            if ( ("date" in login_choice) or ("run date" in  login_choice) or ("show me the date" in  login_choice) or ("view date" in  login_choice)):
                os.system("date")
            elif(("calender " in login_choice) or ("run calender " in  login_choice) or ("show me the calender " in  login_choice) or ("view calender" in  login_choice)):
                os.system("cal")
            elif (("firefox" in login_choice) or ("run firefox" in  login_choice) or ("web browser " in  login_choice) or ("open web browser" in  login_choice)):
                os.system("firefox")
            elif (("text editor" in login_choice) or ("notepad" in  login_choice) or ("gedit " in  login_choice)): 
                os.system("gedit")
            elif (("start docker " in login_choice) or ("docker" in  login_choice) or ("container " in  login_choice) or ("docker container" in login_choice)):
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
                            os.system("docker rm `docker pa --a -q` ")
            elif ( ("webserver" in login_choice) or ("apache webserver" in  login_choice) or ("httpd" in  login_choice)):
                os.system("date")
                os.system("espeak-ng installing_h_t_t_p_d")
                os.system("yum install httpd")
                os.system("espeak-ng opening_h_t_m_l_directory")
                os.system("cd /var/www/html")
                os.system("espeak-ng opening_gedit")
                os.system("cd /var/www/html/ && gedit myweb.html")
                os.system("espeak-ng start__h_t_t_p_d_service")
                os.system("systemctl start httpd")
                os.system("ifconfig enp0s3")
                os.system("espeak-ng please_copy_the_ip_address____")
                os.system("espeak-ng opening_firefox")
                os.system("firefox")
            elif ( ("cloud service" in login_choice) or ("amazon cloud  " in  login_choice) or ("aws" in  login_choice)):
                os.system("date")
                print("Login  details")
                os.system("aws configure")

                print("Choose a choice")
                print(" 1. EC2")
                print(" 2. EBS")
                print(" 3. IAM")
                print(" 4. S3")
                i = input("Choice: ")

                if int(i)==1:
                    print(" Choose an option")
                    print(" 1. Launch an instance")
                    print(" 2. Start an instance")
                    print(" 3. Stop an instance")
                    print(" 4. Attach EBS")
                    print(" 5. Create Key")
                    print(" 6. Desribe key")
                    j = input("Choice: ")
                    if int(j)==1:
                        print("Operating system :")
                        print("1. Amazon linux")
                        print("2. Redhat Linux")
                        print("3. Widnows")
                        ch=input("Choice:")
                        if int(ch)==1:
                            osami="ami-0e306788ff2473ccb"
                        elif int(ch)==2:
                            osami="ami-052c08d70def0ac62"
                        elif int(ch)==3:
                            osami="ami-0b2f6494ff0b07a0e"
                        count=input("Count: ")
                        sg=input("Security Group id: ")
                        ec2key=input("Key for authentication:")
                        os.system("aws ec2 run-instances --image-id    {} --instance-type    t2.micro --count {} --subnet-id subnet-329ae47e --security-group-ids {} --key-name {}".format(osami,count,sg,ec2key))
                elif int(j)==2:
                    ec2id=input("Instance Id:")
                    os.system("aws ec2 start-instances --instance-ids {}".format(ec2id))
                elif int(j)==3:
                    ec2id=input("Instance Id:")
                    os.system("aws ec2 stop-instances --instance-ids {}".format(ec2id))
                elif int(j)==4:
                    ec2id=input("Instance Id:")
                    volumeid=input("Volume Id:")
                    os.system ("aws ec2 attach-volume --volume-id {} --instance-id {} -device /dev/sdf("")".format(volumeid,ec2id))
                elif int(j)==5:	
                     key=input ("Key name:")
                     os.system("aws ec2 create-key-pair --key-name {}".format(key)) 
                elif int(j)==6:
                     os.system("aws ec2 describe-key-pairs") 
                elif int(i)==2:
                    print(" Choose an option")
                    print(" 1. Launch an EBS volume")
                    print(" 2. Attach an EBS volume")
                    print(" 3. Delete Volume")
                    j = input("Choice: ")
                    if int(j)==1:
                        size=input("Size:") 
                        os.system("aws ec2 create-volume  --volume-type gp2  --size {} --availability-zone ap-south-1b".format(size))
                    elif int(j)==2:
                        ec2id=input("Instance Id:")
                        volumeid=input("Volume Id:")
                        os.system ("aws ec2 attach-volume --volume-id {} --instance-id {} -device /dev/sdf("")".format(volumeid,ec2id))
                    elif int(j)==3:
                        volumeid=input("Volume Id:")
                        os.system ("aws ec2 attach-volume --volume-id {}".format(volumeid))
                elif int(i)==3:
                    print(" Choose an option")
                    print(" 1. Create a user")
                    print(" 2. Control protocols for user")
                elif int(i)==4:
                    print(" Choose an option")
                    print(" 1. Launch a bucket")
                else:
                    print("Invalid Option!")
            elif ("cloud front" in local_choice):
                print("press1: to login to your AWS Account")
                r=input(": ")
                if int(r)==1:
                    r=os.system("aws configure")
                    os.system("tput setaf 3")
                    print("\t\t\tWELCOME TO YOUR AWS ACCOUNT")
                    print("\t\t\t\t------------")
                    os.system("tput setaf 2")
                    print("""
                    \n
                    press1 : to create an S3 bucket
                    press2 : to upload file
                    press3 : to allow public access
                    press4 : to create cloudfront distribution
                    """)
                    os.system("tput setaf 7")
                    ch=input("Enter your choice: ")
                    if int(ch)==1:
                        buckname=input("Bucket name: ")
                        regname=input("Region: ")
                        os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(buckname,regname,regname))
                    elif int(ch)==2:
                        filename=input("Enter the filename: ")
                        s3buck=input("Enter the s3_bucket_name: ")
                        os.system("aws s3 cp {} s3://{}/{}".format(filename,s3buck,filename))
                    elif int(ch)==3:
                        fn=input("Enter the File_name: ")
                        s3b=input("Enter the s3_bucket_name: ")
                        os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(s3b,fn))
                    elif int(ch)==4:
                        odomain=input("Enter the s3_bucket_name: ")
                        fn1=input("Enter the filename: ")
                        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(odomain,fn1))
            elif (("hadoop cluster" in login_choice) or ("hadoop configuration" in  login_choice) or ("apache hadoop configure" in  login_choice)):
                os.system("")   
       	    elif (("close" in login_choice) or ("exit" in  login_choice)):
                os.system("exit")
            else:
                print("Sorry! Your Entry is not valid")
            
else:
        os.system("espeak-ng you__say__a__wrong__password__please__try__again")
        print("Wrong Password (X) Please Try Again!!")


  
