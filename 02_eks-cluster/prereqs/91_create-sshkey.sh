#!/bin/bash
ssh-keygen
aws ec2 import-key-pair --key-name "eksworks" --public-key-material file://~/.ssh/id_rsa.pub
# if error, do below
# aws ec2 import-key-pair --key-name "eksworks" --public-key-material fileb://~/.ssh/id_rsa.pub
