#Function to upload a file to an S3 bucket
import boto3
import os

#write function to upload file to s3 bucket
def upload_file(file_name, bucket):
    object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response


