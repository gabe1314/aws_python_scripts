import boto3
import botocore
import os

ec2_client = boto3.client('ec2', region_name='us-east-1')
response = ec2_client.describe_volumes(Filters=[{'Name': 'tag:Application', 'Values': ['NAME']}])



for result in response['Volumes']:
    VolumeId = result['VolumeId']
    VolumeType = result['VolumeType']
    try:
        if VolumeType == 'gp2':
            modify = ec2_client.modify_volume(VolumeId=VolumeId,VolumeType='gp3')
            print(f"{VolumeId} changed to gp3")
        else:
            print(f"{VolumeId} doesn't fit the requirements") 
    except boto.execptions.ClientError as error:
        print(error)    

