# Import required packages
import json
import math
import boto3
from time import gmtime, strftime

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PowerOfMathDatabase')

def lambda_handler(event, context):
    """
    AWS Lambda function to calculate base^exponent,
    store the result in DynamoDB, and return the result.
    """
    # Get current time
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    # Extract numbers from the event
    base = int(event['base'])
    exponent = int(event['exponent'])

    # Perform the calculation
    math_result = math.pow(base, exponent)

    # Store result and timestamp in DynamoDB
    table.put_item(
        Item={
            'ID': str(math_result),
            'LatestGreetingTime': now
        }
    )

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps(f'Your result is {math_result}')
    }
