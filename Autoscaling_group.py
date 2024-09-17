# Step 1: Create a Launch Template
aws ec2 create-launch-template \
  --launch-template-name my-template \
  --version-description "version1" \
  --launch-template-data '{
    "ImageId":"ami-0abcdef1234567890",
    "InstanceType":"t2.micro",
    "SecurityGroupIds":["sg-12345678"],
    "KeyName":"my-key"
}'

# Step 2: Create an Auto Scaling Group
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name my-asg \
  --launch-template "LaunchTemplateName=my-template,Version=1" \
  --min-size 1 \
  --max-size 5 \
  --desired-capacity 2 \
  --vpc-zone-identifier "subnet-12345678"
