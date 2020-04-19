import boto3
import json

# Create ACM client
acm = boto3.client('acm')

# Like this: arn:aws:acm:ap-south-1:032:certificate/a3f9
arn_key = 'your Arn Key'

response = acm.get_certificate(
    CertificateArn=arn_key
)

# Get certificate value from your Amazon Certificate Manager.
res = dict(
    (data, response[data])
    for data in ['Certificate', 'CertificateChain']
    if data in response
)

print(res['Certificate'])
print(res['CertificateChain'])