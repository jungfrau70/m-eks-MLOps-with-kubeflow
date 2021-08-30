#!/bin/bash

eksctl delete cluster -f cluster-mlops.yaml
#eksctl create fargateprofile --cluster aiplatform --name kubeflow --namespace kube-system
