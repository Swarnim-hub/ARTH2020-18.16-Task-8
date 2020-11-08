import os
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
		





		
	
	
