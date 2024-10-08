# Setting up CloudWatch Alarm
aws cloudwatch put-metric-alarm \
    --alarm-name "HighCPUUtilization" \
    --metric-name "CPUUtilization" \
    --namespace "AWS/EC2" \
    --statistic "Average" \
    --period 300 \
    --threshold 80 \
    --comparison-operator "GreaterThanOrEqualToThreshold" \
    --dimensions "Name=InstanceId, Value=i-1234567890abcdef0" \
    --evaluation-periods 2 \
    --alarm-actions arn:aws:sns-east-1:123456789012:NotifyMe