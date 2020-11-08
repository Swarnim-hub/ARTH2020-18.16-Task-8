import os
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
