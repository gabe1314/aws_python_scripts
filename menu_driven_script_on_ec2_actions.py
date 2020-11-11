import boto3
aws_mag_con=boto3.Session(profile_name='default')
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")


while True:
    print("This script performs the following actions on ec2 instances")
    print("""
    	1. start
    	2. stop
    	3. reboot
    	4. terminate
    	5. Exit
    	""")

    opt=int(input("Enter your option: "))
    if opt==1:
    	instance_id=input('Enter your Ec2 instance Id: ')
    	my_req_instance_object=ec2_con_re.Instance(instance_id)
    	print("Starting ec2 instances....")
    	my_req_instance_object.start()
    elif opt==2:
    	instance_id=input('Enter your Ec2 instance Id: ')
    	my_req_instance_object=ec2_con_re.Instance(instance_id)
    	print("Stopping Ec2 Instance...")
    	my_req_instance_object.stop()
    elif opt==3:
    	instance_id=input('Enter your Ec2 instance Id: ')
    	my_req_instance_object=ec2_con_re.Instance(instance_id)
    	print("Stopping Ec2 Instance...")
    	my_req_instance_object.reboot()	
    elif opt==4:
    	instance_id=input('Enter your Ec2 instance Id: ')
    	my_req_instance_object=ec2_con_re.Instance(instance_id)
    	print("terminate Ec2 Instance...")
    	my_req_instance_object.terminate()
    elif opt==5:
    	print("Thank you for using this script")
    	sys.exit()
    else:
    	print("Your option is invalid. Please try once again")