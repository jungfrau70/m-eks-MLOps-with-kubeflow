
import os

import mnist

def write_config():
    region = os.environ['AWS_REGION']
    os.unsetenv('AWS_REGION')
    contents = "[default]\nregion = %s\n" % region
    with open('/root/.aws/config', 'w') as myfile:
        myfile.write(contents)

def write_credentials():
    access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    os.unsetenv('AWS_ACCESS_KEY_ID')
    secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    os.unsetenv('AWS_SECRET_ACCESS_KEY')
    contents = "[default]\naws_access_key_id = %s\naws_secret_access_key = %s\n" % (access_key_id, secret_access_key)
    with open('/root/.aws/credentials', 'w') as myfile:
        myfile.write(contents)

if __name__ == "__main__":
    os.makedirs('/root/.aws')
    write_config()
    write_credentials()
    s3_bucket = os.environ['S3_BUCKET']
    mnist.main([
        "--model_export_path",
        "s3://%s/mnist/tf_saved_model" % s3_bucket,
        "--model_summary_path",
        "s3://%s/mnist/tf_summary" %s3_bucket,
        "--epochs",
        "1"])
