aws cloudwatch put-dashboard \
    --dashboard-name "MyDashboard" \
  --dashboard-body '{
    "widgets": [
        {
            "type": "metric",
            "x": 0,
            "y": 0,
            "width": 6,
            "height": 6,
            "properties": {
                "metrics": [["AWS/EC2", "CPUUtilization", "InstanceId", "i-1234567890abcdef0"]],
                "period": 300,
                "stat": "Average",
                "title": "EC2 CPU Utilization"
            }
        }
    ]
}'