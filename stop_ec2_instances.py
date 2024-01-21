import boto3

def stop_ec2_instances():
    ec2 = boto3.client('ec2')
    
    # Get all running instances
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    # Stop each running instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping EC2 instance: {instance_id}")

if __name__ == "__main__":
    stop_ec2_instances()
