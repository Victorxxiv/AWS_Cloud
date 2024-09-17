aws ec2 run_instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --count 1 \
    --instance-type t2.micro \
    --key-name my-aws-key \
    security-group-ids sg-0123456789abcdef0 \
    --subner-id subnet-6e7f829e