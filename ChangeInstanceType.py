import boto3
import time
import sys

instance = boto3.client('ec2')
instance_type = sys.argv[1]

def stop_instance():
	instance.stop_instances(InstanceIds=['i-c7755963'])
	#while stop_response['StoppingInstances'][0]['CurrentState']['Name']!='stopped':
	#instance_status = instance.describe_instance_status(InstanceIds=['i-c7755963'])

	#print instance_status
	#while instance_status['InstanceStatuses'][0]['InstanceState']['Name']!='stopped':
	#	print "Instance State:"
	#	instance_status = instance.describe_instance_status(InstanceIds=['i-c7755963'])
	#	print instance_status
	#	time.sleep(5)
	#	continue


def change_instance_type():
	modify_response = instance.modify_instance_attribute(InstanceId='i-c7755963', InstanceType={'Value':instance_type})


def start_instance():
	start_response = instance.start_instances(InstanceIds=['i-c7755963'])
	#while start_response['StartingInstances'][0]['CurrentState']['Name']!='running':

	#while instance.describe_instance_status(InstanceIds=['i-c7755963'])!='running':
	#	print "Instance State"
	#	print instance.describe_instance_status(InstanceIds=['i-c7755963'])
	#	time.sleep(5)
	#	continue


stop_instance()
time.sleep(30)
change_instance_type()
time.sleep(5)
start_instance()
print "Instance type changed successfully"
