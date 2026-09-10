from botocore.exceptions import ClientError


def ensure_subscription_table(dynamodb_resource):
    table_name = "dev_subscriptions"
    table = dynamodb_resource.Table(table_name)

    try:
        table.meta.client.describe_table(TableName=table_name)
        return table
    except ClientError as exc:
        if exc.response["Error"]["Code"] != "ResourceNotFoundException":
            raise

    dynamodb_resource.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "subscriptionId", "KeyType": "HASH"}],
        AttributeDefinitions=[
            {"AttributeName": "subscriptionId", "AttributeType": "S"}
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )

    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
    return dynamodb_resource.Table(table_name)
