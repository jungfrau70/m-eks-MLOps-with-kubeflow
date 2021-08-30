#!/bin/bash
source .env

mkdir -p ${KF_DIR}
cd ${KF_DIR}

wget -O kfctl_aws.yaml $CONFIG_URI
kfctl apply -f kfctl_aws.yaml
