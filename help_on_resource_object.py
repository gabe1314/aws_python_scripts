import boto3

aws_mag_con=boto3.session.Session(profile_name="default")
iam_con_re=aws_mag_con.resource(service_name="iam",region_name="us-east-1")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
s3_con_re=aws_mag_con.resource(service_name="s3",region_name="us-east-1")

for each_item in iam_con_re.users.limit(10):
	print(each_item.user_name)