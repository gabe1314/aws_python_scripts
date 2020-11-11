import boto3





aws_mag_con_default=boto3.session.Session(profile_name="default")
sts_con_cli=aws_mag_con_default.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()

for each_item
  print(response)
