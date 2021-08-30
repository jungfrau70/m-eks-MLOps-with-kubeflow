# KubeFlow

Example of GitLab CI for Tensorflow model training and inference in Kubernetes.

Despite the name, we aren't actually using KubeFlow. The only image that is required for this process is the TensorFlow images that we pull directly from DockerHub.

## Cleanup between runs

Right now this project is for demos only. The CI pipeline expects to deploy everything it needs, and does not clean up after itself. So if you run it a second time, you need to delete the output and the pods. Here's how to delete the training pod:

```
kubectl get pods --all-namespaces
```

Look for the pod called "mnist-training" and note its namespace. Then replace the blank with the namespace and do this:

```
kubectl delete pod mnist-training --namespace __________
```

Also have to delete the services 

To delete the output, go to the S3 bucket and remove the folder called "1".

```
aws s3 rm --profile kubeflow s3://2qb6eb-eks-ml-data/mnist/tf_saved_model/1
```

### Running it locally

You can easily run the TensorFlow container locally. Just do this:

```
docker run -it -v "$(pwd)":/app tensorflow/tensorflow:1.13.1
```

### Other notes

The S3 bucket we've been using for testing is s3://2qb6eb-eks-ml-data/ in us-east-1.

If you want a K8S pod to stay alive forever, put this line in the YAML:

```
command: ["/bin/sh", "-ec", "while :; do echo '.'; sleep 5 ; done"]
```

If a container is running (e.g. with the infinite loop above) then you can shell into it; replace the pod name and namespace

```
kubectl exec --namespace __________ -it __________ -- /bin/bash
```

Once in a pod, a quick way to confirm the connection to S3 from tensorflow -- go into Python and enter:

```
from tensorflow.python.lib.io import file_io
print file_io.stat('s3://2qb6eb-eks-ml-data/')
```

Need the AWS CLI?

```
apt update && apt install curl unzip
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
unzip awscli-bundle.zip
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
```

... though `apt install -y awscli` seems to work too.
