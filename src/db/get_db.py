import boto3


def get_dynamodb():
    """
    Get the DynamoDB resource pointing to Floci.
    """
    return boto3.resource(
        "dynamodb",
        endpoint_url="http://localhost:4566",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )
