import boto3 # type: ignore

def create_instance():
    # Correct region_name syntax
    ec2 = boto3.resource("ec2", region_name="us-west-2")  # Specify the correct region

    # Create EC2 instance
    instances = ec2.create_instances(
        ImageId="ami-*****",  # Replace with the correct AMI ID
        InstanceType="t2.micro",  # Instance type
        MinCount=1,  # Minimum number of instances
        MaxCount=1,  # Maximum number of instances
        KeyName="your-key-pair",  # Replace with your key pair name
        SecurityGroupIds=["sg-*****"],  # Replace with your security group ID
        SubnetId="subnet-*****"  # Replace with your subnet ID
    )

    # Output the instance ID of the created instance
    print(f"EC2 Instance created with ID: {instances[0].id}")

if __name__ == "__main__":
    create_instance()
