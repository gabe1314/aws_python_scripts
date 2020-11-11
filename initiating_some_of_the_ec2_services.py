import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")




'''
response=ec2_con_cli.describe_instances()['Reservations']
for each_item in response:
    for each in each_item['Instances']:
    	print("-----------------------------")
    	print("The Image Id is: {}\nThe Instance Id is: {}\nThe Instance Launch Time is:".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))
'''


response=ec2_con_cli.describe_volumes()['Volumes']
for each_item in response:
	print("The Volume ID is: {}\nIf the Volumes are Encrypted: {}\nThe Volume Type is: {}".format(each_item['VolumeId'],each_item['Encrypted'],each_item['VolumeType']))