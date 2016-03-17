import boto3
import time
import sys

instance = boto3.client('ec2')

#Command Line arguments
instance_id = sys.argv[1]
instance_type = sys.argv[2]


def stop_instance():
	instance.stop_instances(InstanceIds=[instance_id])

def change_instance_type():
	modify_response = instance.modify_instance_attribute(InstanceId=instance_id, InstanceType={'Value':instance_type})

def start_instance():
	start_response = instance.start_instances(InstanceIds=[instance_id])

def instance_status():
	status_response = instance.describe_instance_status(InstanceIds=[instance_id])
	#Using this hack since describe_instance_status() is not returning "stopped" status when instance is stopped
	if status_response['InstanceStatuses'] == []:
		instance_status = "stopped"
	#Here describe_instance_status() is returning "running" state as it should be
	else:
		instance_status = status_response['InstanceStatuses'][0]['InstanceState']['Name']
	return instance_status	

 
stop_instance()
#Waits until instance is completely stopped
while instance_status() != 'stopped'
	"Instance is being stopped..."
	time.sleep(3)

#Change instance type and waits for 5 seconds just to be on the safer side	
change_instance_type()
time.sleep(5)

start_instance()

#Waits until instance is running
while instance_status() != 'running'
	print "Waiting for instance to start..."
	time.sleep(3)

print "Instance type has been changed successfully"
